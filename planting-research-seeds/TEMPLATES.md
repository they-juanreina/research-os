# Seed File Templates

Templates for all files created by the `planting-research-seeds` skill.
Replace every `[BRACKETED_VALUE]` with actual content from Step 1 — leave no placeholder unfilled.

---

## Template A — `seed.md`

```markdown
---
seed_id: [SEED_ID]
seed_name: [SEED_NAME]
date_planted: [YYYY-MM-DD]
planted_by: [PLANTED_BY]
seed_type: [SEED_TYPE]
maturity: Planted
original_question: "[ORIGINAL_QUESTION]"
description: [ONE_SENTENCE_DESCRIPTION]
potential_impact: [POTENTIAL_IMPACT]
success_recognition: [SUCCESS_RECOGNITION]
timeline: [TIMELINE or "Not defined"]
related_seeds:
  [- seed_id(s), or leave empty]
related_research:
  [- reference(s), or leave empty]
stakeholders:
  [- name(s), or leave empty]
linked_sessions: []
methodology: []
status: Planted
---

# [SEED_NAME]

## Overview

[DESCRIPTION — 2–3 sentences expanding on the one-liner above. What is being explored and why it matters.]

## Provenance

| Attribute | Value |
|-----------|-------|
| **Date Planted** | [YYYY-MM-DD] |
| **Planted By** | [PLANTED_BY] |
| **Seed Type** | [SEED_TYPE] |
| **Maturity** | 🌱 Planted |
| **Timeline** | [TIMELINE or "Not defined"] |
| **Stakeholders** | [STAKEHOLDERS or "Not defined"] |

## Original Question

> [ORIGINAL_QUESTION]

## Potential Impact

[POTENTIAL_IMPACT — Which product, design, or user decisions this would inform. What changes if this question gets answered.]

## Success Recognition

*When is this seed ready to harvest?*

[SUCCESS_RECOGNITION — What artifacts will exist, what questions will be answered, what confidence level is needed to act on findings. Be specific.]

## Related Seeds

[List related seeds with a brief description of the relationship. Format: `[seed_id]` — [relationship description]. Or write "None identified yet."]

## Related Research

[List external references, prior studies, or artifacts relevant to this question. Or write "None identified yet."]

## Phase Structure

```
Seeds/[SEED_NAME]/
├── 01_Plan/       ← Research plan, success criteria, discussion guide
├── 02_Sessions/   ← Transcripts (DOCX), notes (MD), raw data (CSV)
├── 03_Synthesis/  ← Journey maps, HMW statements, thematic maps
└── 04_Evaluation/ ← Success criteria matrix, issue logs, metrics
```

## Notes

[NOTES — Any additional context, constraints, open hypotheses, or known unknowns. Or write "None."]

## Maturity Log

| Date | Maturity | Updated By | Note |
|------|----------|------------|------|
| [YYYY-MM-DD] | 🌱 Planted | [PLANTED_BY] | Seed created |
```

---

## Template B — `01_Plan/Research_Plan.md`

```markdown
---
author: [PLANTED_BY]
document type:
  - Research Plan
description: Starter research plan for [SEED_NAME]
date: [Month YYYY]
verified: false
---

# Research Plan — [SEED_NAME]

## Research Question

> [ORIGINAL_QUESTION]

## Background

[POTENTIAL_IMPACT — Expand on why this question matters and what decisions it will inform.]

## Proposed Methodology

*To be confirmed during planning.*

Suggested starting point based on seed type (**[SEED_TYPE]**):

[INSERT ONE OF THE FOLLOWING BASED ON SEED_TYPE:
- Research Direction → Semi-structured discovery interviews
- Feature Concept → Moderated concept evaluation or prototype testing
- Usability Finding → Moderated usability testing
- User Request → Contextual inquiry or diary study
- Tech Exploration → Technical interviews + concept validation
- Business Opportunity → Expert interviews + secondary research
- Competitive Intelligence → Desk research + heuristic analysis
- Desk Research → Document analysis + secondary research synthesis]

## Success Criteria

*What does this research need to achieve for the seed to be harvested?*

[SUCCESS_RECOGNITION]

## Proposed Participants

*To be defined during planning.*

- Target roles:
- Number of sessions:
- Recruitment criteria:

## Open Planning Questions

- [ ] What is the minimum evidence needed to act on findings?
- [ ] Who are the right participants to answer this question?
- [ ] What method best fits the question within the available timeline?
- [ ] Do any related seeds already provide partial evidence?

## Timeline

[TIMELINE or "Not defined — to be scoped during planning"]

## Related Seeds and Research

[List related seeds and prior research that inform the approach, or "None identified."]
```

---

## Template C — `02_Sessions/README.md`

```markdown
# Sessions — [SEED_NAME]

Place session materials here as research is conducted.

## What belongs here

- Transcripts: one `.docx` or `.md` file per session, named `[Participant Name or ID].[ext]`
- Session notes: one `.md` file per session (use the `session-note-taking` skill)
- Raw data: `.csv` exports, structured observations

## Naming convention

`[YYYY-MM-DD] [Participant Name or ID].[ext]`

## Status

🌱 No sessions conducted yet.
```

---

## Template D — `03_Synthesis/README.md`

```markdown
# Synthesis — [SEED_NAME]

Place synthesis artifacts here after sessions are complete.

## What belongs here

- Journey maps (use the `journey-mapping` skill)
- HMW opportunity statements (use the `hmw-extraction` skill)
- Thematic maps and pattern analyses
- Research reports and executive summaries

## Status

🌱 No synthesis conducted yet.
```

---

## Template E — `04_Evaluation/README.md`

```markdown
# Evaluation — [SEED_NAME]

Place evaluation artifacts here after synthesis is complete.

## What belongs here

- Issue logs as `.csv` (use the `issue-log` skill)
- Success criteria tracking matrix (use the `success-criteria-tracking` skill)
- Saturation analysis report (use the `saturation-analysis` skill)
- Final metrics and go/no-go assessments

## Status

🌱 No evaluation conducted yet.
```
