# meeting-transcribe service

Local FastAPI service that converts a recording into a diarized JSON transcript.
Powers the `/meeting-transcription` skill and the `meeting-transcribe` MCP tool.

Backend: MLX Whisper (Apple GPU) + pyannote diarization (MPS). Falls back to
WhisperX (CPU + ctranslate2) when MLX is unavailable.

## First-time setup

```bash
cd services/meeting-transcribe
./setup.sh
# edit .env and set HF_TOKEN (after accepting pyannote model terms)
./run.sh
```

Pre-reqs:
- Python 3.11+
- macOS arm64 for the MLX backend (any platform works on the WhisperX fallback)
- ffmpeg available on PATH (used by both backends to decode audio)
- A Hugging Face account with terms accepted for
  [pyannote/speaker-diarization-community-1](https://hf.co/pyannote/speaker-diarization-community-1)

## Running

```bash
./run.sh
```

Service listens on `http://127.0.0.1:8787`:

| Surface | Path | Use |
|---|---|---|
| Web UI | `/` | Drag-and-drop a file from the browser |
| HTTP API | `POST /transcribe` | Multipart upload from curl/scripts |
| MCP tool | `/mcp` | `streamable-http` transport — discovered automatically by Claude Code via `.mcp.json` at the plugin root |
| CLI smoke test | `./cli_test.sh path/to/audio.mp3 [language]` | Quick sanity check |
| Health | `GET /health` | Backend + model info |

## Configuration (env vars)

| Var | Default | Purpose |
|---|---|---|
| `TRANSCRIBE_BACKEND` | `mlx` | `mlx` or `whisperx` |
| `MLX_MODEL` | `mlx-community/whisper-large-v3-turbo` | MLX HF repo |
| `TRANSCRIBE_MODEL` | `large-v3-turbo` | WhisperX model name (fallback path) |
| `DIARIZATION_MODEL` | `pyannote/speaker-diarization-community-1` | |
| `DIARIZATION_DEVICE` | auto (`mps` on Apple Silicon) | Override if needed |
| `TRANSCRIBE_BATCH_SIZE` | `16` | WhisperX batch size |
| `TRANSCRIBE_ALIGN` | `false` | Default for word-level alignment |
| `TRANSCRIBE_OUTPUTS_DIR` | `./outputs` | Where transcripts are persisted |
| `HF_TOKEN` | — | Required for diarization model download |

## Output shape

Every call (HTTP, MCP, or UI) produces a JSON file in `outputs/` and returns the same payload:

```json
{
  "language": "en",
  "speakers": ["SPEAKER_00", "SPEAKER_01"],
  "source_filename": "p03.mp3",
  "created_at": "2026-04-27T16:02:16",
  "backend": "mlx",
  "audio_seconds": 2507.76,
  "realtime_factor": 0.08,
  "timings": { "load_audio": 1.1, "asr": 79.7, "diarize": 113.8, "total": 194.6 },
  "segments": [
    { "start": 0.20, "end": 0.94, "speaker": "SPEAKER_00", "text": "...", "words": [] }
  ],
  "saved_to": "/abs/path/outputs/2026-04-27T16-02-16_p03.json"
}
```

## Performance

On Apple M-series with MLX backend, expected RTF is **0.08–0.20×** real time (a 1-hour meeting transcribes in 5–12 min). See `skills/meeting-transcription/REFERENCE.md` for tuning notes.
