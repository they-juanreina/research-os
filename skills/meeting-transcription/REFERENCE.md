---
name: meeting-transcription-reference
scope: meeting-transcription
last_updated: 2026-04-27
---

# Meeting Transcription — Reference

Detailed methodology, performance tuning, and edge-case handling. Load this only when the SKILL workflow does not cover the situation at hand.

---

## Performance: realtime factor (RTF) ranges on Apple Silicon (M-series)

`realtime_factor = total_processing_time / audio_duration`. Lower is faster.

| Configuration | Expected RTF | Notes |
|---|---|---|
| `mlx` backend + diarize on MPS, no alignment | 0.08–0.20× | Default, native Apple GPU |
| `mlx` backend + diarize on MPS, with word timestamps | 0.10–0.25× | Word timestamps are nearly free in MLX |
| `whisperx` backend + diarize on MPS, no alignment | 0.25–0.5× | Fallback (CPU ASR via ctranslate2) |
| `whisperx` backend + diarize on CPU, with alignment | 1.5–3.0× | Old default — investigate if you see this |

If RTF > 0.5 on the MLX backend, something is misconfigured. Check `/health`:
- `backend` should be `mlx`
- `whisper_model` should be `mlx-community/whisper-large-v3-turbo`
- `diarize_device` should be `mps` (not `cpu`)
- `default_align` should be `false`

---

## Backends: MLX (primary) and WhisperX (fallback)

The service supports two ASR backends, selected with `TRANSCRIBE_BACKEND` (default `mlx`):

- **`mlx`** — Apple's MLX framework. Runs Whisper natively on the Apple GPU (Metal). ~5-10× faster than the WhisperX fallback on this machine. Word timestamps come free as part of the same forward pass (no separate wav2vec2 alignment needed).

- **`whisperx`** — The original ctranslate2-based path. ctranslate2 supports CPU and CUDA only — **no Metal/MPS** on Apple Silicon — so it runs on CPU with `int8` quantization. Word-level alignment uses a separate wav2vec2 model. Use this only if MLX fails or for cross-machine consistency with a CUDA host.

Diarization (pyannote) always uses PyTorch on MPS regardless of ASR backend. With `PYTORCH_ENABLE_MPS_FALLBACK=1` set automatically, ops without an MPS kernel fall back to CPU silently.

To force the fallback: `TRANSCRIBE_BACKEND=whisperx ./run.sh`

---

## Hotwords / initial prompt

The service ships a default hotwords list covering Valtech / John Deere / common tech vocabulary (see `service.py::DEFAULT_HOTWORDS`). Pass a custom string in the `hotwords` field to **replace** (not append to) the default for a specific request.

**When to override:**
- Product names not in the default (e.g., "Lineage", "Verifier", "PartsHub")
- Names of specific people who appear repeatedly
- Industry jargon for the recording's domain

**Format:** Comma-separated list, ~50–80 terms max. More than that and Whisper starts hallucinating.

---

## Speaker hints

`num_speakers` / `min_speakers` / `max_speakers` are passed to pyannote. If you know the count, **pass it.** Diarization quality improves materially.

| Scenario | Recommendation |
|---|---|
| 1-on-1 interview | `num_speakers=2` |
| 1-on-1 with occasional observer chime-in | `min_speakers=2, max_speakers=3` |
| Group session, count known | `num_speakers=N` |
| Group session, count unknown | Leave blank — let pyannote decide |

Two common failure modes when speaker count is unset:
- **Over-segmentation:** One person split into 3+ speakers because they vary in tone or distance from mic.
- **Under-segmentation:** Two similar voices merged into one speaker.

Both improve dramatically with `num_speakers`.

---

## Alignment: when to enable

`align=false` (default) — segment-level timestamps only. Each segment has a start/end and one speaker. Sufficient for:
- Thematic coding
- Issue logging
- Journey mapping
- Synthesis reporting
- Any reading-oriented use

`align=true` — word-level timestamps via wav2vec2. Each word has its own start/end and assigned speaker. Required for:
- Sub-second highlight extraction
- Forced-alignment QA
- Generating captions with karaoke-style word highlighting

Cost: ~30–40% more total runtime. Skip unless the downstream consumer truly needs words.

---

## Language detection

Pass `language` if you know it (`es`, `en`). Otherwise the model auto-detects on the first ~30s of audio. Auto-detect is reliable for clean audio but can misfire when:
- Recording starts with silence or non-speech
- The first speaker code-switches
- Background music or noise dominates the opening

When in doubt, pass `language` explicitly.

---

## File handling

The service writes outputs to `meeting-transcribe/outputs/` automatically (timestamped). For research workflows, **copy or move** the JSON into the appropriate seed folder:

```
Seeds/<seed-name>/02_Sessions/Transcripts/<sessionID>_<participant>.json
```

This keeps the service's outputs folder as a working buffer and the seed folder as the source of truth.

---

## Troubleshooting

**`HF_TOKEN not set`** — Diarization will fail. Put `HF_TOKEN=hf_...` in `meeting-transcribe/.env` and restart. Token must have access to `pyannote/speaker-diarization-community-1` (accept terms on the model page first).

**Service slow to start (~30s+)** — Normal on first run after a model bump. Models download to `~/.cache/huggingface/`. Subsequent starts are seconds.

**Diarization produces only `SPEAKER_00`** — Either truly single-speaker audio, or the audio is silent/too quiet. Check the recording manually.

**ASR hallucinates content not in the audio** — Most often: hotwords list too long, or input audio is mostly silence. Try a shorter hotwords list and verify the recording.

**Out-of-memory on large files (>2h)** — Service holds the full audio array in memory. Split with `ffmpeg -i in.mp4 -f segment -segment_time 1800 -c copy out_%03d.mp4` and transcribe each chunk.

**MLX backend errors on first call (`unable to download model`)** — First run downloads ~600MB-1.5GB of MLX weights to `~/.cache/huggingface/`. Confirm internet access and HF cache is writable. If still failing, fall back with `TRANSCRIBE_BACKEND=whisperx`.

---

## Pitfalls

- **Don't run with `align=true` by default.** Word alignment is expensive and rarely consumed downstream. Make the requester justify it.
- **Don't trust auto-detected speaker counts in noisy audio.** Verify the count visually (UI or by inspecting `speakers[]`) and re-run with `num_speakers` if it's wrong.
- **Don't share the HF token.** It lives in `.env` (gitignored). If a transcript JSON is committed to a repo, ensure no token leaked into logs.
- **Don't paste sensitive recordings into a hosted service.** This pipeline is local-only by design; a research participant's recording must not be uploaded externally without consent.
