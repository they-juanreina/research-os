---
name: journey-mapping
description: "Synthesizes qualitative research data into structured journey maps. Use when creating experience maps from session transcripts, interview notes, or observation data. Produces stage-by-stage maps with touchpoints, emotions, pain points, and opportunities per user type. Triggers: journey map, experience map, user journey, customer journey, touchpoint mapping, service blueprint."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-03-01
---

# Journey Mapping

> Apply `CORE.md` epistemic framework before mapping. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Qualitative research — transcripts, interview notes, observation data, field notes.
**Output**: Structured journey map(s) with stage-by-stage experience breakdown.

---

## Workflow

0. **Define goal and scope** — Before mapping: (a) State the user's primary goal in one sentence: "The user wants to [verb] [object] so they can [outcome]." (b) Choose journey scope: **Epic** (multi-stage lifecycle, weeks–months), **Micro** (single task or flow, minutes–one session), or **Serial** (repeating cycle). (c) Mark the journey's start and end points explicitly. Scoping before mapping prevents sprawl and ensures the map is answering a specific question. See `REFERENCE.md` → Journey Scope.

1. **Parse and segment** — Read all research material. Identify chronological or process-based stages. Mark transitions (decision points, state changes, role shifts). Note multiple personas separately.

2. **Extract 5–8 stages** — Translate experience into meaningful phases (e.g., Awareness → Discovery → Adoption → Mastery). Each stage must have observable actions or clear temporal boundaries.

3. **Map touchpoints** — For each stage: every interaction point with the product, service, team, or environment (digital, human, environmental, self-directed) in sequence within the stage.

4. **Extract user actions** — What the user *does* at each stage. Concrete verbs (reads, clicks, asks, searches, compares). Ground in research; do not infer beyond evidence.

5. **Capture emotional indicators** — From transcripts, tone, language, behavioral cues: emotional state with confidence score 1–3 (1=inferred, 2=contextual, 3=explicit statement). Prefer direct quotes.

6. **Map pain points** — Specific blockers or friction the user articulates or exhibits. Tie each to a stage and touchpoint.

7. **Identify opportunities** — Per pain point or stage: actionable intervention grounded in research. Bridge between current and desired state.

8. **Validate coverage** — All major stages represented. Flag low-confidence rows. Mark areas needing more research.

---

## Output Format

Markdown table:

| Stage | Touchpoint | User Action | Thought/Quote | Emotion | Pain Point | Opportunity | Confidence |
|---|---|---|---|---|---|---|---|
| Name | System/person/artifact | verb phrase | direct quote or inferred thought | state + intensity | specific friction | actionable improvement | 1–3 |

**Variants**:
- **Single-persona** — One table per persona.
- **Multi-persona overlay** — Separate tables + a divergence comparison section highlighting where experiences differ.
- **Service blueprint** — Add "Behind-the-Scenes Actions" and "Support Processes" rows above the user row.

---

## Quality Gates

- [ ] User's goal and journey scope documented before mapping (step 0 complete)
- [ ] Every stage has ≥ 1 touchpoint and user action
- [ ] Emotional states grounded in evidence (quote, explicit statement, or behavioral cue)
- [ ] Pain points specific, not generic ("form takes 15 min" not "process too slow")
- [ ] Opportunities actionable and tied to research findings
- [ ] Confidence levels reflect evidence quality, not assumptions
- [ ] No inferences beyond what research data supports
- [ ] Stages in chronological or logical sequence
- [ ] A value peak (climax) is identifiable — one stage where the user most clearly experiences the product's value
- [ ] The journey end leaves the user in a better state than they started, or is explicitly flagged as a cliffhanger
- [ ] CSV export (if used) matches markdown table exactly

---

## References

- `REFERENCE.md` — column schema, multi-persona guidance, journey scope, story structure analysis, pitfalls, coverage assessment, CSV export standards
- `EXAMPLES.md` — three complete worked examples + service blueprint variant
- `scripts/format_journey_map.py` — markdown ↔ CSV conversion utility
