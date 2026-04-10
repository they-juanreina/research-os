---
name: session-ingestion-reference
description: "Reference details for Teams HTML transcript normalization and notes rendering workflow."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere - Internal Use Only"
last_updated: 2026-03-18
---

# Session Ingestion - Reference

## Parser Behavior

The ingestion utility uses a multi-pattern parser to recover utterances from Teams HTML exports.

Patterns supported:

1. Speaker plus timestamp lines:
   - `Speaker Name 10:31 AM`

2. Timestamp-prefixed lines:
   - `[10:31] Speaker Name: utterance text`
   - `10:31 AM Speaker Name: utterance text`

3. Speaker-colon lines:
   - `Speaker Name: utterance text`

When no explicit timestamp exists, `timestamp` may be empty and sequence order becomes the primary temporal source.

## Noise Filtering

The parser removes common transcript UI lines that are not utterances, including labels such as:

- `Live transcript`
- `Meeting transcript`
- `Transcript`
- `Recording`

If a participant export includes additional product chrome text, update noise filtering rules before rerunning.

## Actor Typing

Actor records are inferred from speaker labels and currently assign:

- `participant` when speaker matches participant folder name
- `other` for facilitator, observers, or unmatched names

If facilitator and note-taker are known upfront, enrich actor typing through a metadata file in a follow-up iteration.

## Part Guess Heuristics

Each utterance is tagged with `part_guess` (`part1`..`part7`) using keyword heuristics aligned to the discussion guide sections.

This is a routing hint, not a final coding truth. Downstream thematic coding should treat `part_guess` as suggestive metadata.

## Missing Template Behavior

This skill requires an existing Jinja2 notes template path.

- If present: render notes files as part of ingestion.
- If missing: stop execution and request generation via a separate template-generation skill (deferred by design).

## Failure Handling

When a source file cannot be parsed into utterances:

1. Session is marked `skipped` in `master.json` manifest.
2. Reason is captured (`no_utterances_extracted` or `no_html_found`).
3. Pipeline continues for remaining participants.

## Validation Checklist

Before handoff, verify:

1. Session counts in `master.json` match processed source files.
2. `fact_utterances.json` includes non-empty `text` for all rows.
3. Every `session_id` in fact table has matching per-session JSON.
4. Notes files exist for each processed session and contain evidence notes blocks.
