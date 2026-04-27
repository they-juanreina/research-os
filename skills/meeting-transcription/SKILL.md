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

**Backend**: Defaults to MLX (Apple GPU native, RTF ~0.10–0.20× on M-series). Set `TRANSCRIBE_BACKEND=whisperx` to fall back to the CPU+ctranslate2 path if MLX is unavailable.

This skill is the **upstream entry point** when sessions are recorded but no Teams HTML transcript is available. Its output replaces (or augments) the Teams HTML that `session-ingestion` consumes.

---

## Workflow

1. **Resolve recording path** — Confirm the audio file exists and locate the seed it belongs to (`Seeds/<seed>/02_Sessions/Recordings/`).

2. **Confirm transcript destination** — Default `Seeds/<seed>/02_Sessions/Transcripts/`. Create if missing.

3. **Service preflight** — `GET http://127.0.0.1:8787/health`. If down, instruct the user to run `meeting-transcribe/run.sh` and wait for "Ready". Do not attempt to start it yourself if the working directory is not the service repo.

4. **Decide alignment** — On the MLX backend, word timestamps are nearly free (same forward pass). On the whisperx fallback, alignment adds ~30–40% via a separate wav2vec2 model. Default `align=false`. Enable only when the downstream task needs word timestamps (e.g., highlight reels, sub-second cue extraction).

5. **Decide speaker hints** — If the moderator+participant count is known, pass `num_speakers` (or `min_speakers`/`max_speakers`). Better diarization, fewer phantom speakers.

6. **Decide hotwords** — If the recording mentions product/tool/team-specific terms not in the default dictionary, append them to the `hotwords` field. Default dictionary covers Valtech / John Deere / common tech vocabulary.

7. **POST to service** — Submit `audio` (multipart) plus the form fields chosen above.

8. **Persist output** — Move the returned JSON from the service `outputs/` folder into the seed's `02_Sessions/Transcripts/` folder, renamed `<sessionID>_<participant>.json`.

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

**Service:**

```bash
cd ~/dev/meeting-transcribe && ./run.sh
```

**Single file (CLI):**

```bash
./cli_test.sh path/to/recording.mp4 [language]
```

**Single file (HTTP):**

```bash
curl -sS --fail-with-body http://127.0.0.1:8787/transcribe \
  -F "audio=@path/to/recording.mp4" \
  -F "language=es" \
  -F "num_speakers=2" \
  -F "align=false" \
  > path/to/transcript.json
```

**UI:** Open `http://127.0.0.1:8787/` for drag-and-drop with full controls.

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
- `~/dev/meeting-transcribe/service.py` — service implementation
- `~/dev/meeting-transcribe/run.sh` — start command
- Downstream skill: `session-ingestion` (when Teams HTML exists or when a JSON-aware ingestor is wired)
- Downstream skill: `thematic-coding` (when ingestion is skipped)
