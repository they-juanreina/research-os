---
name: session-ingestion-examples
description: "Examples for running Teams HTML transcript ingestion and notes rendering."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-18
---

# Session Ingestion - Examples

## Example 1 - Standard Run

### Command

```bash
".venv/bin/python" "Seeds/[YourSeed]/02_Sessions/Output/normalize_sessions.py"
```

### Expected artifacts

- `Seeds/[YourSeed]/02_Sessions/Output/normalized/dim_studies.json`
- `Seeds/[YourSeed]/02_Sessions/Output/normalized/dim_participants.json`
- `Seeds/[YourSeed]/02_Sessions/Output/normalized/dim_actors.json`
- `Seeds/[YourSeed]/02_Sessions/Output/normalized/fact_utterances.json`
- `Seeds/[YourSeed]/02_Sessions/Output/normalized/master.json`
- `Seeds/[YourSeed]/02_Sessions/Output/normalized/sessions/*.json`
- `Seeds/[YourSeed]/02_Sessions/Output/notes/*_notes.md`

## Example 2 - Explicit Paths

### Command

```bash
".venv/bin/python" "Seeds/[YourSeed]/02_Sessions/Output/normalize_sessions.py" \
  --transcripts-dir "Seeds/[YourSeed]/02_Sessions/Transcripts" \
  --schema-dir "Seeds/[YourSeed]/02_Sessions/Output/schemas" \
  --template "Seeds/[YourSeed]/01_Plan/Interview_Notes_Template_Jinja2.md" \
  --out-dir "Seeds/[YourSeed]/02_Sessions/Output/normalized" \
  --notes-out "Seeds/[YourSeed]/02_Sessions/Output/notes"
```

### Expected terminal summary

```text
Processed sessions: <n>
Normalized utterances: <m>
JSON output: Seeds/[YourSeed]/02_Sessions/Output/normalized
Notes output: Seeds/[YourSeed]/02_Sessions/Output/notes
```

## Example 3 - Missing Template (Expected Stop)

If template path does not exist, stop execution and restore a valid template path before rerunning.

### Recovery

1. Ensure `Interview_Notes_Template_Jinja2.md` exists in the seed `01_Plan` folder.
2. Rerun with `--template` pointing to that file.
