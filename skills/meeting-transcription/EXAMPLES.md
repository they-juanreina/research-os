---
name: meeting-transcription-examples
scope: meeting-transcription
last_updated: 2026-04-27
---

# Meeting Transcription — Examples

Worked end-to-end runs. Use these to confirm output format and to lift command snippets when onboarding to the skill.

---

## Example 1 — 1-on-1 Spanish interview, no alignment

**Recording:** `~/Downloads/lineage_p03.m4a` (35 min, 1 moderator + 1 participant, mostly Spanish).

```bash
cd ~/dev/meeting-transcribe && ./run.sh &  # ensure service is up

curl -sS --fail-with-body http://127.0.0.1:8787/transcribe \
  -F "audio=@${HOME}/Downloads/lineage_p03.m4a" \
  -F "language=es" \
  -F "num_speakers=2" \
  > ~/dev/research-os/Seeds/Lineage/02_Sessions/Transcripts/p03.json
```

**Expected runtime on M4 Pro (MLX backend):** ~3-5 min total → `realtime_factor` ≈ 0.10-0.15×.

**Quality check:**
- `speakers` length = 2
- `language` = "es"
- `realtime_factor` < 0.2 on MLX (or < 0.5 on whisperx fallback)
- First few segments make sense when read aloud

---

## Example 2 — Group session with unknown speaker count

**Recording:** `~/Downloads/discovery_workshop.mp4` (90 min, 4–6 attendees).

```bash
curl -sS --fail-with-body http://127.0.0.1:8787/transcribe \
  -F "audio=@${HOME}/Downloads/discovery_workshop.mp4" \
  -F "language=en" \
  -F "min_speakers=4" \
  -F "max_speakers=6" \
  -F "hotwords=Lineage, PartsHub, dealer, OEM, telematics, JDLink, Operations Center" \
  > /tmp/workshop.json
```

**If diarization returns 8+ speakers:** Re-run with `num_speakers=5` (your best guess) — overshoot is worse than a slight under-count for downstream readability.

---

## Example 3 — Need word timestamps for highlight reel

```bash
curl -sS --fail-with-body http://127.0.0.1:8787/transcribe \
  -F "audio=@clip.wav" \
  -F "language=en" \
  -F "num_speakers=2" \
  -F "align=true" \
  > clip.json
```

Each `segments[].words[]` entry now contains `{"word", "start", "end", "speaker", "score"}`.

---

## Example 4 — Reading the timings field to spot regressions

```bash
jq '.timings, {audio_seconds, realtime_factor}' < transcript.json
```

```json
{
  "load_audio": 1.18,
  "asr": 152.30,
  "diarize": 84.07,
  "total": 237.55
}
{
  "audio_seconds": 1830.42,
  "realtime_factor": 0.13
}
```

If `asr` dominates (>70% of total) on the MLX backend, you're at the floor — the model is doing the only thing it can. Switch to `whisper-large-v3-turbo-q4` (smaller MLX quantization) if you need more speed, accepting a small quality drop.

If `diarize` dominates (>50%), something is off — diarization should be sub-30% on MPS. Likely fell back to CPU; check `/health` for `diarize_device`.

---

## Example 5 — Quick smoke test after restart

```bash
./cli_test.sh ~/dev/meeting-transcribe/test-2min.wav es
```

Prints a human-readable transcript and saves the full JSON to `/tmp/transcribe-last.json`. Use this to confirm the service is healthy before kicking off a long batch.
