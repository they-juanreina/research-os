---
name: meeting-transcription
description: "Converts raw meeting audio (mp3/wav/m4a/mp4) into a diarized JSON transcript using a local WhisperX + pyannote service. Use when you have a raw recording (Teams, Zoom, Meet, dictaphone) and need an analysis-ready transcript before ingesting into the research pipeline. Triggers: transcribe meeting, transcribe audio, diarize recording, raw audio to transcript, generate transcript from recording, speaker-labeled transcript, whisperx pipeline."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-04-27
---

# Meeting Transcription

> Apply `CORE.md` epistemic framework before processing. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: A single audio or video file (any codec ffmpeg can decode).
**Output**: One JSON file per recording with diarized segments, detected language, speaker list, and per-stage timings.

**Backend**: Defaults to MLX (Apple GPU native, RTF ~0.08–0.20× on M-series). Set `TRANSCRIBE_BACKEND=whisperx` to fall back to the CPU+ctranslate2 path if MLX is unavailable.

**Capability vs methodology**: The transcription *capability* is the `meeting-transcribe.transcribe_audio` MCP tool, exposed by the bundled service in `services/meeting-transcribe/`. This skill is the *methodology* layer — it decides parameters (hotwords by study, speaker hints, naming, output location, quality gates) and then calls the tool. If the service isn't running, instruct the user to start it before continuing.

This skill is the **upstream entry point** when sessions are recorded but no Teams HTML transcript is available. Its output replaces (or augments) the Teams HTML that `session-ingestion` consumes.

---

## Workflow

1. **Resolve recording path** — Confirm the audio file exists and locate the seed it belongs to (`Seeds/<seed>/02_Sessions/Recordings/`).

2. **Confirm transcript destination** — Default `Seeds/<seed>/02_Sessions/Transcripts/`. Create if missing.

3. **Service preflight** — Confirm the MCP tool `meeting-transcribe.transcribe_audio` is available (or `GET http://127.0.0.1:8787/health` returns 200). If neither responds, instruct the user:

   ```bash
   cd <plugin-root>/services/meeting-transcribe && ./run.sh
   ```

   Wait for the log line `Ready (backend=mlx)`. Do not attempt to start the service yourself unless explicitly asked.

4. **Decide alignment** — On the MLX backend, word timestamps are nearly free (same forward pass). On the whisperx fallback, alignment adds ~30–40% via a separate wav2vec2 model. Default `align=false`. Enable only when the downstream task needs word timestamps (e.g., highlight reels, sub-second cue extraction).

5. **Decide speaker hints** — If the moderator+participant count is known, pass `num_speakers` (or `min_speakers`/`max_speakers`). Better diarization, fewer phantom speakers.

6. **Decide hotwords** — If the recording mentions product/tool/team-specific terms not in the default dictionary, append them to the `hotwords` field. Default dictionary covers Valtech / John Deere / common tech vocabulary.

7. **Call the MCP tool** — Invoke `meeting-transcribe.transcribe_audio` with the parameters chosen above:

   ```
   transcribe_audio(
     audio_path="/abs/path/to/recording.m4a",
     language="es",
     num_speakers=2,
     hotwords="...optional override...",
     align=False,
   )
   ```

   The tool runs synchronously (a 1-hour recording takes ~5–12 min on Apple Silicon) and returns the full payload.

8. **Persist output** — The service writes the JSON to its own `outputs/` folder. Move/copy it into the seed's `02_Sessions/Transcripts/` folder, renamed `<sessionID>_<participant>.json`. The path is in the response's `saved_to` field.

9. **Quality check** — Verify diarization produced a plausible speaker count, language matches expectations, and `realtime_factor` is reasonable (see Reference for ranges).

10. **Handoff** — The diarized JSON feeds `session-ingestion` (which can be configured to consume this JSON shape directly) or, when ingestion is skipped, feeds `thematic-coding` directly through the `segments[]` field.

---

## Output Format

A single JSON object per recording:

```json
{
  "language": "es",
  "speakers": ["SPEAKER_00", "SPEAKER_01"],
  "source_filename": "lineage_p03.mp4",
  "created_at": "2026-04-27T14:22:01",
  "audio_seconds": 1830.42,
  "realtime_factor": 0.38,
  "timings": {
    "load_audio": 1.2,
    "asr": 612.4,
    "diarize": 84.1,
    "total": 697.7
  },
  "segments": [
    {
      "start": 0.20,
      "end": 0.94,
      "speaker": "SPEAKER_00",
      "text": "Hola, gracias por aceptar.",
      "words": []
    }
  ]
}
```

Required fields: `language`, `speakers`, `segments[]`, `source_filename`, `created_at`, `timings`, `audio_seconds`, `realtime_factor`.

`segments[].words[]` is empty unless `align=true` was requested.

---

## Invocation

**First-time setup** (once per machine — skip if the service has run before):

```bash
cd <plugin-root>/services/meeting-transcribe && ./setup.sh
```

`setup.sh` creates the `.venv` (Python env with MLX Whisper, pyannote, ffmpeg bindings) and a `.env` stub. After it finishes:

1. Accept model terms at <https://hf.co/pyannote/speaker-diarization-community-1>
2. Generate a token at <https://hf.co/settings/tokens> (read access)
3. Paste it into `.env`: `HF_TOKEN=hf_...`

**Start the service** (one-time per session):

```bash
cd <plugin-root>/services/meeting-transcribe && ./run.sh
```

**Primary path — MCP tool** (what this skill calls):

The tool `meeting-transcribe.transcribe_audio` is wired up via `.mcp.json` at the plugin root. Claude calls it directly with the resolved parameters. No curl needed. See `services/meeting-transcribe/README.md` for the full input/output contract.

**Escape hatches for human use** (not part of the skill flow):

- **Web UI:** `http://127.0.0.1:8787/` — drag-and-drop with all controls.
- **CLI:** `cd services/meeting-transcribe && ./cli_test.sh path/to/recording.mp4 [language]`
- **Raw HTTP:**
  ```bash
  curl -sS --fail-with-body http://127.0.0.1:8787/transcribe \
    -F "audio=@path/to/recording.mp4" \
    -F "language=es" -F "num_speakers=2" -F "align=false" \
    > path/to/transcript.json
  ```

All paths produce identical JSON output.

---

## Quality Gates

✓ `realtime_factor` < 1.0 on Apple Silicon (otherwise check Reference — likely model misconfigured)
✓ `speakers` count matches the actual conversation (within ±1)
✓ No segments with empty `text`
✓ `language` matches the language passed (or expected) for the recording
✓ Output file lives in the correct seed's `02_Sessions/Transcripts/`
✓ File naming follows `<sessionID>_<participant>.json` so downstream skills can correlate

---

## When To Skip This Skill

- **Teams HTML export already exists** — go straight to `session-ingestion`. This skill is for raw audio only.
- **Single speaker, no diarization needed** — a plain Whisper run is faster; this skill always pays for diarization.
- **Privacy / compliance constraint forbids local-only inference** — clarify with the user before sending audio anywhere.

---

## References

- `REFERENCE.md` — performance tuning, hotword strategy, troubleshooting, alignment trade-offs
- `services/meeting-transcribe/service.py` — service implementation (FastAPI + MCP)
- `services/meeting-transcribe/README.md` — service-level setup and configuration
- `services/meeting-transcribe/run.sh` — start command
- `.mcp.json` (plugin root) — MCP server registration consumed by Claude Code
- Downstream skill: `session-ingestion` (when Teams HTML exists or when a JSON-aware ingestor is wired)
- Downstream skill: `thematic-coding` (when ingestion is skipped)
