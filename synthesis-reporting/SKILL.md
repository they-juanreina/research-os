---
name: synthesis-reporting
description: "Packages synthesis outputs into a structured research report for stakeholders who need findings without raw data. Use after thematic coding, journey mapping, and HMW extraction are complete. Produces a confidence-rated, evidence-grounded narrative report with executive summary, theme findings, opportunities, and honest limitations. Triggers: research report, synthesis report, findings presentation, stakeholder summary, write up the research, report the findings, research deliverable, share findings."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-03-02
---

# Synthesis Reporting

> Apply `CORE.md` epistemic framework before writing. **A report represents real people to an audience that won't read the raw data. Every compression decision carries responsibility.** See `PIPELINE.md` for upstream inputs.

**Input**: Synthesis artifacts — codebook (`themes-[seed].md`), coded dataset, journey map, HMW statements, issue log. At minimum: a completed codebook from thematic-coding.
**Output**: A structured research report (`report-[seed].md`) in the seed's `04_Report/` directory.

---

## Workflow

### Step 0 — Define audience and purpose

Before writing a single sentence, answer:
- **Who is this report for?** (design team, product manager, leadership, research team, external stakeholders — each requires different depth and framing)
- **What decision does it inform?** Name the decision explicitly.
- **What action should readers be able to take after reading?** If you can't answer this, the report has no purpose yet.

Audience and purpose determine report length, technical depth, evidence visibility, and which findings to foreground. See `REFERENCE.md` → Audience Calibration.

---

### Step 1 — Audit available inputs

Inventory synthesis outputs before writing. Record what exists and what is absent:

| Artifact | Present? | Confidence coverage |
|---|---|---|
| Codebook (`themes-[seed].md`) | ✓ / ✗ | List TC-XX IDs and confidence levels |
| Coded dataset (`coded-[seed].csv`) | ✓ / ✗ | Evidence unit count |
| Journey map | ✓ / ✗ | Story shape, climax stage identified? |
| HMW statements | ✓ / ✗ | Count and priority range |
| Issue log | ✓ / ✗ | Severity distribution |
| Saturation analysis | ✓ / ✗ | Recommendation (Continue / Pause / Conclude) |
| Success criteria | ✓ / ✗ | Go / No-go status |

A synthesis report cannot make claims beyond what its input artifacts support. Flag what is missing explicitly in Step 6 (Limitations).

---

### Step 2 — Write the executive summary

3–5 key findings, one sentence each. Rules:

- **Draw only from high or medium confidence themes** — low-confidence findings belong in the body or limitations, not the summary
- **State findings, not recommendations** — `"Users cannot reliably locate work they have previously completed"` not `"We should add better navigation"`
- **Confidence-rate each finding**: append `[High]`, `[Medium]`, or `[Low]` after each sentence
- **Order by decision relevance**, not by theme frequency or codebook order

Apply **CORE.md Plural Interpretations**: for any finding likely to drive a significant decision, write ≥ 2 plausible interpretations in the body section — not just the primary reading.

---

### Step 3 — Write theme narratives

One section per TC-XX category in the codebook. Each narrative:

1. **Opening statement** — theme name + participant-framed description (2–3 sentences). Not evaluative.
2. **Evidence basis** — `n` evidence units from `x` sessions, `y` participants; which roles contributed
3. **Representative quotes** — 1–3 verbatim participant quotes. Label with `[participant role, session ID]`. Never paraphrase a quote presented as a quote.
4. **Edge and variance** — any minority finding, role-specific pattern, or outlier that complicates the dominant reading. Required — do not suppress.
5. **Implication** — what this theme means for the research question. Not a design recommendation. Framed as: `"This suggests that..."` or `"One reading of this pattern is..."` — never as a conclusion.

---

### Step 4 — Integrate journey arc

If a journey map was produced, include a one-page narrative summary:

- **Scope type**: Epic / Micro / Serial
- **Story shape**: Story with climax / Flat / Anticlimactic / Cliffhanger — and what that means for the experience
- **Value peak**: the stage where users most clearly experienced the product's value (or: `"No clear value peak identified — see limitations"`)
- **Crisis stage**: the moment of maximum friction
- **Cliffhanger flag**: if the journey ends without resolution, name it explicitly — do not reframe as a scope choice

If no journey map exists, omit this section and note in the limitations that journey-level experience was not mapped.

---

### Step 5 — Surface opportunities

List HMW statements organized by theme. For each:

- State the HMW statement verbatim from the HMW synthesis
- Link to the pain point it addresses: `(TC-02, 4 sessions, 6 participants)`
- Note priority score and confidence from the HMW output

Do not add HMW statements not present in the synthesis artifacts. Do not rewrite HMW statements to sound more solution-y.

---

### Step 6 — Write the limitations section

Required. Not boilerplate. This section is where the report earns trust.

Address each of these explicitly:

**Sample scope**: Which participant roles, contexts, and demographics were in the study? Who was not represented? What does absence from the sample mean for the findings?

**Evidence gaps**: Which themes have Low confidence (1 session or 1 participant)? Which research questions the study was meant to answer remain open? Where is more data needed before acting?

**Methodological boundaries**: What can this method establish? What can it not? (e.g., `"This qualitative study documents observed behavior and stated experience. It cannot establish statistical prevalence or causal relationships."`)

**Interpretation flags**: Where are findings inferred rather than directly observed? Label them. A statement like `"users appear to distrust the system"` needs a flag: `[Inferred from behavioral signals — explicit statements of distrust were not collected]`.

---

### Step 7 — Recommended next steps

Not design solutions. Structure as:

- **Seeds to plant**: research questions that emerged but were out of scope for this study
- **Themes to validate**: low-confidence findings worth probing in a follow-up study
- **Design handoff notes**: what the team is free to act on vs. what needs more research first — be explicit about the boundary
- **Open questions**: questions the data surfaced but did not answer

---

## Output Format

```markdown
# Research Synthesis Report — [Seed Name]

**Research question**: [from seed metadata]
**Study dates**: [start] – [end]
**Participants**: [n] participants — [roles] — [contexts]
**Methods**: [session types]
**Prepared by**: [author], [date]
**Status**: Draft — requires human review before distribution

---

## Executive Summary

- [Finding 1] [High]
- [Finding 2] [Medium]
- [Finding 3] [High]

---

## Key Findings

### TC-01: [Theme Name]
[Narrative...]

### TC-02: [Theme Name]
[Narrative...]

---

## Experience Arc

[Journey narrative if applicable...]

---

## Opportunities

### From TC-01
- **HMW [statement]** — (TC-01, n sessions, n participants) — Priority: [score]

---

## What This Research Does Not Answer

[Limitations — sample scope, evidence gaps, methodological boundaries, interpretation flags]

---

## Recommended Next Steps

[Seeds, open questions, design handoff notes]

---

## Research Appendix

- Codebook: `03_Synthesis/themes-[seed].md`
- Coded dataset: `03_Synthesis/coded-[seed].csv`
- Session notes: `02_Sessions/`
- Journey map: `03_Synthesis/journey-[seed].md` *(if produced)*
- HMW statements: `03_Synthesis/hmw-[seed].md` *(if produced)*
- Issue log: `03_Synthesis/issues-[seed].csv` *(if produced)*
```

---

## Quality Gates

- [ ] Audience and decision context documented before writing (Step 0 complete)
- [ ] Every executive summary finding is confidence-rated
- [ ] No finding presented without evidence source (theme ID, session count, participant count)
- [ ] All participant quotes are verbatim — no paraphrase presented as quote
- [ ] Plural interpretations applied for significant findings (≥ 2 readings)
- [ ] Edge and minority findings included in each theme narrative — not suppressed
- [ ] Limitations section is specific, honest, and non-boilerplate
- [ ] No design recommendations in findings sections — opportunities are HMW statements, not solutions
- [ ] Journey arc section names the story shape if journey map was produced
- [ ] Cliffhanger flagged explicitly if the experience ends without resolution
- [ ] Status field shows "Draft — requires human review" until reviewed by a human researcher

---

## References

- `REFERENCE.md` — audience calibration, confidence language, epistemic framing, writing minority findings, limitations section depth, common pitfalls
- `TEMPLATE.md` — blank report structure ready to fill
