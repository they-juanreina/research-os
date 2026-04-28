import dataclasses
import gc
import json
import logging
import os
import re
import sys
import tempfile
import time
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

# torchcodec's dlopen of libavutil fails on macOS with Homebrew FFmpeg >= 8.
# Audio decode uses ffmpeg-via-PATH; this is benign. Silence the multi-line traceback.
logging.getLogger("torchcodec._core").setLevel(logging.CRITICAL)
logging.getLogger("torchcodec").setLevel(logging.CRITICAL)

import torch
import whisperx
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from whisperx.diarize import DiarizationPipeline

UI_DIR = Path(__file__).parent / "ui"

OUTPUTS_DIR = Path(os.environ.get("TRANSCRIBE_OUTPUTS_DIR", Path(__file__).parent / "outputs"))
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("transcribe")


def _resolve_diarize_device(requested: str | None) -> str:
    if requested:
        return requested
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


# Backend selection: "mlx" (Apple Silicon native, fastest) or "whisperx" (CPU-only via ctranslate2).
BACKEND = os.environ.get("TRANSCRIBE_BACKEND", "mlx").lower()

# Whisperx (fallback) settings — ctranslate2 supports CPU/CUDA, no Metal/MPS.
DEVICE = os.environ.get("TRANSCRIBE_DEVICE", "cpu")
COMPUTE_TYPE = os.environ.get("TRANSCRIBE_COMPUTE", "int8")
WHISPER_MODEL = os.environ.get("TRANSCRIBE_MODEL", "large-v3-turbo")

# MLX backend settings — runs on Apple GPU.
MLX_MODEL = os.environ.get("MLX_MODEL", "mlx-community/whisper-large-v3-turbo")

DIARIZATION_MODEL = os.environ.get("DIARIZATION_MODEL", "pyannote/speaker-diarization-community-1")
DIARIZE_DEVICE = _resolve_diarize_device(os.environ.get("DIARIZATION_DEVICE"))
DEFAULT_BATCH_SIZE = int(os.environ.get("TRANSCRIBE_BATCH_SIZE", "16"))
DEFAULT_ALIGN = os.environ.get("TRANSCRIBE_ALIGN", "false").lower() in {"1", "true", "yes"}
HF_TOKEN = os.environ.get("HF_TOKEN")

DEFAULT_HOTWORDS = (
    "Claude, Anthropic, Figma, MCP, Langflow, "
    "Kubernetes, Docker, CI/CD, DevOps, GraphQL, REST, TypeScript, "
    "Python, React, Next.js, PostgreSQL, Redis, Kafka, AWS, GCP, Azure, "
    "MLX, PyTorch, Whisper, pyannote, embeddings, "
    "RAG, LLM, prompt, fine-tuning, vector database, "
    "roadmap, sprint, backlog, stakeholder, KPI, OKR, MVP, POC, "
    "usability, affordance, mental model, pain point, user journey, "
    "persona, prototype, wireframe, information architecture, "
    "interview, observation, synthesis, insight, finding."
)

_models: dict[str, Any] = {}


def _progress(msg: str) -> None:
    """Print a boot-progress line to stderr immediately (bypasses uvicorn log buffering)."""
    print(f"[meeting-transcribe] {msg}", file=sys.stderr, flush=True)


def _load_models() -> None:
    if BACKEND == "mlx":
        import mlx_whisper
        from mlx_whisper import load_models

        _progress(f"loading MLX Whisper ({MLX_MODEL})…")
        _models["mlx_whisper_module"] = mlx_whisper
        _models["mlx_model"] = load_models.load_model(MLX_MODEL)
        _models["mlx_repo"] = MLX_MODEL
        log.info("MLX Whisper loaded model=%s", MLX_MODEL)
    elif BACKEND == "whisperx":
        _progress(f"loading WhisperX ({WHISPER_MODEL}, device={DEVICE}, compute={COMPUTE_TYPE})…")
        _models["whisper"] = whisperx.load_model(
            WHISPER_MODEL,
            DEVICE,
            compute_type=COMPUTE_TYPE,
            asr_options={"initial_prompt": DEFAULT_HOTWORDS, "hotwords": DEFAULT_HOTWORDS},
        )
        log.info("WhisperX loaded model=%s device=%s compute=%s", WHISPER_MODEL, DEVICE, COMPUTE_TYPE)
    else:
        raise RuntimeError(f"Unknown TRANSCRIBE_BACKEND: {BACKEND!r} (expected 'mlx' or 'whisperx')")

    _progress(f"loading diarization model ({DIARIZATION_MODEL}, device={DIARIZE_DEVICE})…")
    if not HF_TOKEN:
        log.warning("HF_TOKEN not set — diarization model load will fail until terms accepted + token provided")
    _models["diarize"] = DiarizationPipeline(model_name=DIARIZATION_MODEL, token=HF_TOKEN, device=DIARIZE_DEVICE)

    _models["align_cache"] = {}
    _progress("Ready (backend=%s)" % BACKEND)


# Forward-declared so lifespan can reference the FastMCP http_app's lifespan
_mcp_http_app = None


@asynccontextmanager
async def lifespan(_app: FastAPI):
    _load_models()
    log.info("Ready (backend=%s)", BACKEND)
    if _mcp_http_app is not None:
        async with _mcp_http_app.lifespan(_app):
            yield
    else:
        yield
    _models.clear()
    gc.collect()


app = FastAPI(lifespan=lifespan, title="Meeting Transcribe+Diarize")


def _get_align_model(language: str):
    cache = _models["align_cache"]
    if language not in cache:
        log.info("Loading alignment model for language=%s", language)
        model, metadata = whisperx.load_align_model(language_code=language, device=DEVICE)
        cache[language] = (model, metadata)
    return cache[language]


def _resolve_hotwords(prompt: str | None) -> str | None:
    resolved = prompt if prompt is not None else DEFAULT_HOTWORDS
    return resolved or None


def _is_intra_segment_hallucination(text: str, duration: float) -> bool:
    """Return True if a single token dominates the segment — Whisper repetition loop.

    large-v3-turbo sometimes enters a repetition loop inside a single long segment
    (e.g. 221× the same Cyrillic token on English audio). Cross-segment dedup doesn't
    catch these. Rule: one token > 50% of all word tokens AND segment > 5 s.
    """
    if duration <= 5.0:
        return False
    words = text.split()
    if len(words) < 10:
        return False
    counts: dict[str, int] = {}
    for w in words:
        key = w.lower().strip(".,!?\"'")
        counts[key] = counts.get(key, 0) + 1
    return max(counts.values()) / len(words) > 0.50


def _clean_asr_segments(segments: list[dict[str, Any]], audio_seconds: float) -> list[dict[str, Any]]:
    """Drop tail hallucinations, intra-segment repetition loops, and empty segments.

    Whisper-family models emit phantom segments past the real end of audio
    (especially MLX with condition_on_previous_text), zero-duration empties on
    silences, and intra-segment repetition loops (one token > 50% of the segment).
    All three produce corrupt or useless rows downstream.
    """
    tail_tolerance = 1.0  # seconds — keep last legit content even if slightly past audio end
    cleaned: list[dict[str, Any]] = []
    intra_dropped = 0
    for seg in segments:
        start = float(seg.get("start", 0.0))
        end = float(seg.get("end", start))
        text = (seg.get("text") or "").strip()
        if start >= audio_seconds + tail_tolerance:
            continue
        if end <= start and not text:
            continue
        if _is_intra_segment_hallucination(text, end - start):
            intra_dropped += 1
            continue
        cleaned.append(seg)
    if intra_dropped:
        log.warning("Dropped %d intra-segment repetition hallucination(s)", intra_dropped)
    return cleaned


def _run_asr_mlx(
    audio_array,
    language: str | None,
    hotwords: str | None,
    word_timestamps: bool,
) -> dict[str, Any]:
    mlx_whisper = _models["mlx_whisper_module"]
    kwargs: dict[str, Any] = {
        "path_or_hf_repo": _models["mlx_repo"],
        "initial_prompt": _resolve_hotwords(hotwords),
        "word_timestamps": word_timestamps,
        "verbose": None,
    }
    if language:
        kwargs["language"] = language
    result = mlx_whisper.transcribe(audio_array, **kwargs)
    return {
        "segments": result.get("segments", []),
        "language": result.get("language") or language or "en",
    }


def _run_asr_whisperx(
    audio_array,
    language: str | None,
    hotwords: str | None,
    batch_size: int,
) -> dict[str, Any]:
    pipeline = _models["whisper"]
    resolved = _resolve_hotwords(hotwords)
    pipeline.options = dataclasses.replace(
        pipeline.options,
        initial_prompt=resolved,
        hotwords=resolved,
    )
    transcribe_kwargs: dict[str, Any] = {"batch_size": batch_size}
    if language:
        transcribe_kwargs["language"] = language
    result = pipeline.transcribe(audio_array, **transcribe_kwargs)
    return {
        "segments": result.get("segments", []),
        "language": result.get("language") or language or "en",
    }


@app.get("/health")
def health():
    info: dict[str, Any] = {
        "status": "ok",
        "backend": BACKEND,
        "diarization_model": DIARIZATION_MODEL,
        "diarize_device": DIARIZE_DEVICE,
        "default_batch_size": DEFAULT_BATCH_SIZE,
        "default_align": DEFAULT_ALIGN,
    }
    if BACKEND == "mlx":
        info["whisper_model"] = MLX_MODEL
        info["device"] = "mps"
        info["compute_type"] = "fp16"
    else:
        info["whisper_model"] = WHISPER_MODEL
        info["device"] = DEVICE
        info["compute_type"] = COMPUTE_TYPE
    return info


@app.get("/", response_class=HTMLResponse)
def index():
    html_path = UI_DIR / "index.html"
    if not html_path.exists():
        return HTMLResponse("<h1>UI missing</h1>", status_code=500)
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


@app.get("/outputs")
def list_outputs():
    files = sorted(OUTPUTS_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return [
        {"name": p.name, "size": p.stat().st_size, "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(timespec="seconds")}
        for p in files
    ]


@app.get("/outputs/{name}")
def get_output(name: str):
    safe = re.sub(r"[^A-Za-z0-9_.\-]", "", name)
    path = OUTPUTS_DIR / safe
    if not path.exists() or not path.is_file():
        raise HTTPException(status_code=404, detail="not found")
    return FileResponse(path, media_type="application/json", filename=safe)


def _process_audio(
    audio_path: str,
    *,
    language: str | None = None,
    hotwords: str | None = None,
    num_speakers: int | None = None,
    min_speakers: int | None = None,
    max_speakers: int | None = None,
    batch_size: int = DEFAULT_BATCH_SIZE,
    align: bool = DEFAULT_ALIGN,
    source_filename: str | None = None,
) -> dict[str, Any]:
    """Run ASR + diarization on a local audio path. Returns the payload dict (also writes to OUTPUTS_DIR)."""
    log.info("Transcribing %s (backend=%s, lang=%s, batch=%d, align=%s)", audio_path, BACKEND, language, batch_size, align)
    timings: dict[str, float] = {}
    t0 = time.perf_counter()
    audio_array = whisperx.load_audio(audio_path)
    audio_seconds = len(audio_array) / 16000.0
    timings["load_audio"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    if BACKEND == "mlx":
        asr_result = _run_asr_mlx(audio_array, language, hotwords, word_timestamps=align)
    else:
        asr_result = _run_asr_whisperx(audio_array, language, hotwords, batch_size)
    timings["asr"] = time.perf_counter() - t0
    detected_lang = asr_result["language"]
    raw_segment_count = len(asr_result["segments"])
    cleaned_segments = _clean_asr_segments(asr_result["segments"], audio_seconds)
    dropped = raw_segment_count - len(cleaned_segments)
    log.info(
        "ASR done in %.1fs, lang=%s, segments=%d (dropped %d hallucinations)",
        timings["asr"], detected_lang, len(cleaned_segments), dropped,
    )

    segments_for_speakers: dict[str, Any] = {"segments": cleaned_segments}
    if align and BACKEND == "whisperx":
        t0 = time.perf_counter()
        align_model, align_meta = _get_align_model(detected_lang)
        segments_for_speakers = whisperx.align(
            cleaned_segments, align_model, align_meta, audio_array, DEVICE, return_char_alignments=False
        )
        timings["align"] = time.perf_counter() - t0
        log.info("Alignment done in %.1fs", timings["align"])

    t0 = time.perf_counter()
    diarize_kwargs: dict[str, Any] = {}
    if num_speakers is not None:
        diarize_kwargs["num_speakers"] = num_speakers
    if min_speakers is not None:
        diarize_kwargs["min_speakers"] = min_speakers
    if max_speakers is not None:
        diarize_kwargs["max_speakers"] = max_speakers
    diarize_segments = _models["diarize"](audio_array, **diarize_kwargs)
    timings["diarize"] = time.perf_counter() - t0
    log.info("Diarization done in %.1fs", timings["diarize"])

    final = whisperx.assign_word_speakers(diarize_segments, segments_for_speakers, fill_nearest=True)

    segments: list[dict[str, Any]] = []
    for seg in final["segments"]:
        segments.append(
            {
                "start": float(seg.get("start", 0.0)),
                "end": float(seg.get("end", 0.0)),
                "speaker": seg.get("speaker", "UNKNOWN"),
                "text": (seg.get("text") or "").strip(),
                "words": [
                    {
                        "word": w.get("word"),
                        "start": float(w["start"]) if w.get("start") is not None else None,
                        "end": float(w["end"]) if w.get("end") is not None else None,
                        "speaker": w.get("speaker"),
                        "score": float(w["score"]) if w.get("score") is not None else (float(w["probability"]) if w.get("probability") is not None else None),
                    }
                    for w in seg.get("words", [])
                ],
            }
        )

    speakers = sorted({s["speaker"] for s in segments if s.get("speaker") and s["speaker"] != "UNKNOWN"})

    name_for_file = source_filename or Path(audio_path).name
    source_name = Path(name_for_file).stem or "audio"
    safe_stem = re.sub(r"[^A-Za-z0-9_-]+", "-", source_name)[:60].strip("-") or "audio"
    ts = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    out_path = OUTPUTS_DIR / f"{ts}_{safe_stem}.json"

    total = sum(timings.values())
    rtf = total / audio_seconds if audio_seconds > 0 else None
    payload: dict[str, Any] = {
        "language": detected_lang,
        "speakers": speakers,
        "source_filename": name_for_file,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "backend": BACKEND,
        "segments": segments,
        "timings": {k: round(v, 2) for k, v in timings.items()} | {"total": round(total, 2)},
        "audio_seconds": round(audio_seconds, 2),
        "realtime_factor": round(rtf, 2) if rtf is not None else None,
        "saved_to": str(out_path),
    }
    out_path.write_text(json.dumps({k: v for k, v in payload.items() if k != "saved_to"}, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info(
        "Saved %s — %.1fs audio in %.1fs (rtf=%.2fx)",
        out_path.name, audio_seconds, total, rtf or 0.0,
    )
    return payload


@app.post("/transcribe")
async def transcribe(
    audio: UploadFile = File(...),
    language: str | None = Form(default=None),
    hotwords: str | None = Form(default=None),
    num_speakers: int | None = Form(default=None),
    min_speakers: int | None = Form(default=None),
    max_speakers: int | None = Form(default=None),
    batch_size: int = Form(default=DEFAULT_BATCH_SIZE),
    align: bool = Form(default=DEFAULT_ALIGN),
):
    suffix = Path(audio.filename or "audio").suffix or ".wav"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(await audio.read())
        tmp_path = tmp.name
    try:
        payload = _process_audio(
            tmp_path,
            language=language,
            hotwords=hotwords,
            num_speakers=num_speakers,
            min_speakers=min_speakers,
            max_speakers=max_speakers,
            batch_size=batch_size,
            align=align,
            source_filename=audio.filename,
        )
        return JSONResponse(payload)
    except Exception as e:
        log.exception("Transcription failed")
        raise HTTPException(status_code=500, detail=str(e)) from e
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def _relabel_transcript(data: dict[str, Any], mapping: dict[str, str]) -> dict[str, Any]:
    """Apply a speaker mapping to a transcript dict in-place and return it.

    Touches every place a speaker label appears: top-level `speakers` list,
    `segments[].speaker`, and `segments[].words[].speaker`.
    Unknown labels (not in mapping) are left unchanged.
    """
    data["speakers"] = [mapping.get(s, s) for s in data.get("speakers", [])]
    for seg in data.get("segments", []):
        if seg.get("speaker"):
            seg["speaker"] = mapping.get(seg["speaker"], seg["speaker"])
        for word in seg.get("words", []):
            if word.get("speaker"):
                word["speaker"] = mapping.get(word["speaker"], word["speaker"])
    return data


class RelabelRequest(BaseModel):
    transcript_path: str
    mapping: dict[str, str]  # e.g. {"SPEAKER_00": "Moderator", "SPEAKER_01": "Ana"}
    output_path: str | None = None  # None = overwrite in place


@app.post("/relabel")
async def relabel(req: RelabelRequest):
    """Remap generic SPEAKER_XX labels to real names throughout a transcript JSON.

    Reads the transcript at `transcript_path`, applies `mapping`, and writes
    the result to `output_path` (or overwrites in place if omitted).
    Returns the updated transcript.
    """
    src = Path(req.transcript_path).expanduser()
    if not src.is_file():
        raise HTTPException(status_code=404, detail=f"transcript not found: {req.transcript_path}")
    data = json.loads(src.read_text(encoding="utf-8"))
    _relabel_transcript(data, req.mapping)
    dest = Path(req.output_path).expanduser() if req.output_path else src
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info("Relabeled %s → %s (mapping: %s)", src.name, dest.name, req.mapping)
    return JSONResponse({"saved_to": str(dest), **data})


# -----------------------------------------------------------------------------
# MCP layer — exposes the same processing pipeline as a typed tool over
# streamable-http. Mounted on /mcp so the FastAPI service stays a single process.
# -----------------------------------------------------------------------------
from fastmcp import FastMCP  # noqa: E402

mcp = FastMCP(
    name="meeting-transcribe",
    instructions=(
        "Local transcription + diarization service. Use transcribe_audio when you "
        "have an audio/video file path on this machine and need a speaker-labeled "
        "transcript. Use relabel_speakers to remap SPEAKER_XX labels to real names "
        "after transcription. The service runs on Apple Silicon GPU via MLX Whisper + pyannote."
    ),
)


@mcp.tool()
def transcribe_audio(
    audio_path: str,
    language: str | None = None,
    hotwords: str | None = None,
    num_speakers: int | None = None,
    min_speakers: int | None = None,
    max_speakers: int | None = None,
    align: bool = False,
) -> dict[str, Any]:
    """Transcribe and diarize a meeting recording from a local file path.

    Args:
        audio_path: Absolute path to a local audio/video file (mp3/wav/m4a/mp4/etc).
            Must be a file the running service process can read.
        language: ISO 639-1 code like 'es' or 'en'. None = auto-detect.
        hotwords: Comma-separated terms to bias ASR toward (names, products, jargon).
            Replaces the service default dictionary for this call.
        num_speakers: Exact speaker count if known. Improves diarization quality.
        min_speakers: Lower bound on speaker count (use with max_speakers).
        max_speakers: Upper bound on speaker count.
        align: Word-level timestamps. Cheap on MLX backend, ~30-40% extra on whisperx.
            Only enable if a downstream consumer needs sub-second word boundaries.

    Returns:
        A dict with keys: language, speakers, segments[], timings, audio_seconds,
        realtime_factor, backend, saved_to (path of the persisted JSON).
    """
    path = Path(audio_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"audio_path not found or not a file: {audio_path}")
    return _process_audio(
        str(path),
        language=language,
        hotwords=hotwords,
        num_speakers=num_speakers,
        min_speakers=min_speakers,
        max_speakers=max_speakers,
        align=align,
        source_filename=path.name,
    )


@mcp.tool()
def relabel_speakers(
    transcript_path: str,
    mapping: dict[str, str],
    output_path: str | None = None,
) -> dict[str, Any]:
    """Remap generic SPEAKER_XX labels to real names throughout a transcript JSON.

    Call this after transcribe_audio once you know who was speaking.
    The mapping is applied to every place a speaker label appears: the top-level
    `speakers` list, `segments[].speaker`, and `segments[].words[].speaker`.
    Unknown labels (not in mapping) are left unchanged.

    Args:
        transcript_path: Absolute path to a transcript JSON produced by transcribe_audio.
        mapping: Dict of SPEAKER_XX → real name. E.g. {"SPEAKER_00": "Moderator", "SPEAKER_01": "Ana"}.
            You only need to map the speakers you know — unmapped labels stay as-is.
        output_path: Where to write the relabeled JSON. Omit to overwrite transcript_path in place.

    Returns:
        The updated transcript dict with real names everywhere, plus `saved_to` field.
    """
    src = Path(transcript_path).expanduser()
    if not src.is_file():
        raise FileNotFoundError(f"transcript not found: {transcript_path}")
    data = json.loads(src.read_text(encoding="utf-8"))
    _relabel_transcript(data, mapping)
    dest = Path(output_path).expanduser() if output_path else src
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info("Relabeled %s → %s (mapping: %s)", src.name, dest.name, mapping)
    return {"saved_to": str(dest), **data}


@mcp.tool()
def health_check() -> dict[str, Any]:
    """Return service health and active backend info.

    Use to confirm the transcription service is up and which model is loaded
    before calling transcribe_audio."""
    return health()


# Build the MCP HTTP app and stitch its lifespan into the FastAPI lifespan above.
_mcp_http_app = mcp.http_app(path="/", transport="streamable-http")
app.mount("/mcp", _mcp_http_app)
