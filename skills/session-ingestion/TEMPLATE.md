---
name: session-ingestion-template
description: "Output contracts for normalized JSON and notes rendering."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-18
---

# Session Ingestion - Output Contract Template

## 1) Dimensional Outputs

### dim_studies.json

```json
[
  {
    "study_id": "seed_lineage",
    "study_name": "Data Lineage in UDP",
    "seed": "Lineage",
    "methodology": "Ad hoc interviews"
  }
]
```

### dim_participants.json

```json
[
  {
    "participant_id": "lineage-example-participant",
    "display_name": "Example Participant",
    "study_id": "seed_lineage",
    "session_id": "Lineage-INT-001"
  }
]
```

### dim_actors.json

```json
[
  {
    "actor_id": "actor-example-speaker",
    "session_id": "Lineage-INT-001",
    "display_name": "Example Speaker",
    "actor_type": "participant"
  }
]
```

## 2) Fact Output

### fact_utterances.json

```json
[
  {
    "utterance_id": "utt-001-0001",
    "study_id": "seed_lineage",
    "session_id": "Lineage-INT-001",
    "participant_id": "lineage-example-participant",
    "actor_id": "actor-example-speaker",
    "sequence": 1,
    "timestamp": "10:31:00",
    "speaker": "Example Speaker",
    "text": "I usually verify source tables in Databricks first.",
    "part_guess": "part2",
    "source_file": ".../Transcripts/Example Participant/transcript.html"
  }
]
```

## 3) Session Output

### sessions/Lineage-INT-001.json

```json
{
  "study": {
    "study_id": "seed_lineage",
    "study_name": "Data Lineage in UDP",
    "seed": "Lineage",
    "methodology": "Ad hoc interviews"
  },
  "session": {
    "session_id": "Lineage-INT-001",
    "session_key": "example-participant-transcript",
    "participant": "Example Participant",
    "source_file": ".../Transcripts/Example Participant/transcript.html",
    "ingested_at": "2026-03-18T00:00:00Z",
    "utterance_count": 42
  },
  "utterances": []
}
```

## 4) Master Manifest

### master.json

```json
{
  "study": {
    "study_id": "seed_lineage"
  },
  "counts": {
    "sessions": 7,
    "participants": 7,
    "actors": 15,
    "utterances": 1200
  },
  "generated_at": "2026-03-18T00:00:00Z",
  "manifest": [
    {
      "session_id": "Lineage-INT-001",
      "participant": "Example Participant",
      "source_file": "...",
      "status": "processed",
      "utterance_count": 42,
      "notes_file": ".../Output/notes/Lineage-INT-001_example-participant_notes.md"
    }
  ]
}
```

## 5) Notes Rendering Context Contract

Minimum context fields expected by the Lineage notes template:

- `session_id`
- `session_date`
- `session_start_time`
- `participant_name`
- `participant_pronouns`
- `participant_role_type`
- `part1_notes`..`part6_notes`
- `part1_quotes`, `part2_quotes`, `part4_quotes`
- `final_open_feedback`

If a field cannot be inferred from transcript text, preserve template-safe defaults rather than injecting assumptions.
