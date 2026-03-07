---
name: session-note-taking
description: "Generates structured session notes from moderated research sessions. Use when processing interview transcripts, usability test recordings, or live observation data into standardized note documents. Triggers: session notes, interview notes, observation notes, research session, moderated session, usability session, note-taking template."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-02-28
---

# Session Note-Taking

> Apply `CORE.md` epistemic framework before processing. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Transcript, recording notes, or raw observation data from a research session.
**Output**: Structured session notes with extracted quotes, observations, insights, and metadata.

---

## Workflow

1. **Parse input** — Identify session type (usability test / discovery interview / contextual inquiry / moderated workshop), date, duration, participant count, facilitator.

2. **Extract participants** — For each: name/ID, role (participant/moderator/observer), relevant background, prior product context.

3. **Establish scenario** — Session objective, task description, facilitator framing provided to participant.

4. **Map first actions** — Participant's exact first interaction with the stimulus. Treat as high-signal; do not skip.

5. **Chronological observations** — Timeline order: time markers, participant actions, facilitator interventions, notable pauses/hesitations, unexpected paths or workarounds.

6. **Pull quotes** — Verbatim statements that reveal emotion, unexpected framing, domain knowledge, mental models, or contradictions. Mark anything paraphrased explicitly.

7. **Identify pain points** — Each with: description, severity (minor / moderate / critical), context, affected task or feature.

8. **Extract timing** — Task or phase durations. Note moments of hesitation, searching, or recovery.

9. **Non-verbal signals** — Body language, tone shifts, expressions that add context beyond words. Do not speculate; note only observable signals.

10. **Post-session data** — Survey, questionnaire, or debrief results; self-reported satisfaction; follow-up comments.

11. **Synthesize 3–5 insights** — What did we learn? What surprised us? What needs to change? Each insight must be traceable to a quote or observation.

12. **Quality check** — Run quality gates below before finalizing.

---

## Output

Complete `TEMPLATE.md` with all sections filled:

- Session Meta | Participant Info | Scenario/Task | First Actions
- Chronological Observations | Key Quotes | Pain Points | Timing Data
- Non-Verbal Observations | Mini-Survey Results | Post-Session Debrief
- Key Insights | Notes for Future Sessions

---

## Quality Gates

✓ Participant IDs accurate and consistent throughout
✓ Quotes verbatim or explicitly marked as paraphrased
✓ Pain points specific, repeatable, and context-linked
✓ Timing data includes units (min/sec)
✓ Key insights evidence-based — each traces to a quote or observation
✓ Session objective explicitly stated and addressed
✓ Non-verbal observations add context, not speculation
✓ Document complete and ready for team distribution

---

## References

- `TEMPLATE.md` — blank template structure
- `EXAMPLES.md` — two complete worked examples
- `scripts/generate_notes.py` — Python pre-fill utility
