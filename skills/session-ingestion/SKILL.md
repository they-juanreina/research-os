---
name: session-ingestion
description: "Normalizes Teams HTML session transcripts into structured JSON and renders filled discussion notes from a Jinja2 template. Use when interview exports are HTML (not DOCX transcripts) and you need analysis-ready files for coding, issue logging, journey mapping, and synthesis. Triggers: session ingestion, normalize transcript html, teams transcript to json, render interview notes, transcript normalization pipeline."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-18
---

# Session Ingestion

> Apply `CORE.md` epistemic framework before processing. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Participant transcript folders with Teams HTML files and a notes template in Jinja2 markdown.
**Output**: Normalized JSON artifacts plus one rendered session notes document per processed session.

---

## Workflow

1. **Resolve paths** - Confirm transcripts root, output directory, schema directory, and notes template path.

2. **Preflight checks** - Verify at least one participant folder exists and contains HTML transcript exports.

3. **Template requirement** - Confirm notes template exists in the plan folder.
   - If present: continue.
   - If missing: stop and request template generation as a separate skill flow.

4. **Parse Teams HTML** - Strip UI noise and extract clean line blocks from each transcript.

5. **Extract utterances** - Detect speaker, timestamp, and utterance text using Teams-compatible patterns.

6. **Normalize entities** - Build dimensional records for study, participants, and actors.

7. **Write fact records** - Create utterance-level facts with session IDs, sequence, source file, and part guess.

8. **Render notes** - Fill the interview notes Jinja2 template with extracted session content.

9. **Emit per-session artifacts** - Write one session JSON file and one notes markdown file for each processed transcript.

10. **Emit aggregate artifacts** - Write dim and fact tables plus a master manifest with counts and statuses.

11. **Quality check** - Validate session counts, utterance counts, and traceability from notes quotes to utterance rows.

12. **Handoff** - Route outputs downstream to thematic-coding, issue-log, journey-mapping, and synthesis-reporting.

---

## Output Format

Write outputs to the configured output path with this structure:

- `normalized/dim_studies.json`
- `normalized/dim_participants.json`
- `normalized/dim_actors.json`
- `normalized/fact_utterances.json`
- `normalized/sessions/<session_id>.json`
- `normalized/master.json`
- `notes/<session_id>_<participant>_notes.md`

Key minimum fields:

- **dim_studies**: `study_id`, `study_name`, `seed`, `methodology`
- **dim_participants**: `participant_id`, `display_name`, `study_id`, `session_id`
- **dim_actors**: `actor_id`, `session_id`, `display_name`, `actor_type`
- **fact_utterances**: `utterance_id`, `study_id`, `session_id`, `participant_id`, `actor_id`, `sequence`, `timestamp`, `speaker`, `text`, `part_guess`, `source_file`
- **master**: `counts`, `generated_at`, `manifest[]`

---

## Invocation

Primary command (adapt the seed name and script path to your project):

```bash
".venv/bin/python" "Seeds/[YourSeed]/02_Sessions/Output/normalize_sessions.py"
```

Optional path overrides:

```bash
".venv/bin/python" "Seeds/[YourSeed]/02_Sessions/Output/normalize_sessions.py" \
  --transcripts-dir "Seeds/[YourSeed]/02_Sessions/Transcripts" \
  --schema-dir "Seeds/[YourSeed]/02_Sessions/Output/schemas" \
  --template "Seeds/[YourSeed]/01_Plan/Interview_Notes_Template_Jinja2.md" \
  --out-dir "Seeds/[YourSeed]/02_Sessions/Output/normalized" \
  --notes-out "Seeds/[YourSeed]/02_Sessions/Output/notes"
```

---

## Quality Gates

✓ At least one HTML transcript parsed per processed session
✓ No processed session has an empty `utterances[]` array
✓ Speaker and sequence fields populated for every fact record
✓ One rendered notes file exists per processed session
✓ Each rendered quote can be traced to source utterance text
✓ Manifest captures skipped files with explicit reason
✓ Output files available for downstream skills without manual reshaping

---

## References

- `REFERENCE.md` - parsing assumptions, edge cases, and failure handling
- `TEMPLATE.md` - normalized output contract and notes rendering contract
- `EXAMPLES.md` - end-to-end run examples and expected outputs
- `Seeds/[YourSeed]/02_Sessions/Output/normalize_sessions.py` - ingestion utility used by this skill (one per seed)
