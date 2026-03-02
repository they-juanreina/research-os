---
name: thematic-coding
description: "Transforms raw session data into a validated codebook and coded evidence dataset. Use after session notes are complete and before journey mapping, HMW extraction, or saturation analysis. Converts observations, quotes, and pain points from multiple sessions into named, defined themes with inclusion/exclusion criteria, evidence counts, and cross-participant coverage. Triggers: affinity map, affinity mapping, thematic coding, code the data, theme extraction, cluster observations, analyze transcripts, synthesize sessions, group findings, open coding, axial coding, what themes emerged, identify patterns."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-03-02
---

# Thematic Coding

> Apply `CORE.md` epistemic framework before coding. **Categories are constructed, not discovered. Every theme name is an analytical decision — own it explicitly.** See `PIPELINE.md` for upstream/downstream handoffs.
>
> **Terminology note** (Saldaña, 2021): What this skill calls "themes" (TC-XX) are technically **categories** — groupings of similar codes. An interpretive *theme* is a propositional statement that emerges from categorization, not a category label. Step 9 covers themeing in this deeper sense. For most UX deliverables, category-level analysis (Steps 1–8) is sufficient.

**Input**: Session notes from `02_Sessions/` — observations, quotes, and pain points from ≥ 2 sessions.
**Output**: A codebook (`themes-[seed].md`) and a coded evidence dataset (`coded-[seed].csv`).

---

## Two modes — choose based on context

| Mode | When to use | What it produces |
|------|-------------|-----------------|
| **Affinity mapping** | Early-stage, exploratory data, no prior theory | Bottom-up clusters emerge freely from data; themes named after grouping |
| **Thematic coding** | Theory-informed or cross-study synthesis | Codebook drafted from prior knowledge, then applied to data; gaps documented |

Most studies use **affinity mapping as the entry point**, then formalize the clusters into a thematic coding codebook. The workflow below supports both modes; note where they diverge.

---

## Workflow

### Step 1 — Gather and audit inputs

Collect from the seed's `02_Sessions/` directory:
- All session note files (processed through `session-note-taking`)
- Extract three fields per session: `observations[]`, `quotes[]`, `pain_points[]`

For each session, record: session ID, date, participant ID(s), participant role(s).

**Input audit** (CORE.md — Audit Before Acting):
- How many sessions? How many participants? What roles are represented?
- Which sessions are missing, thin, or atypical (rushed, off-topic, technical failure)?
- Who is absent? Which roles, contexts, or demographics have no representation?

Flag any sessions excluded from coding and document the reason.

---

### Step 2 — Atomic decomposition

Break composite notes into **evidence units** — one unit = one thought.

**Pre-coding** (optional): Before decomposing, scan the full session corpus once without coding. Highlight passages that seem analytically significant ("codable moments"). Mark administrative or irrelevant passages `N/A` so they are explicitly out of scope rather than silently skipped.

**Rules:**
- Split on "and" when two distinct observations are joined: `"Found navigation confusing AND clicked the wrong button"` → two units
- Preserve the original wording; do not paraphrase at this stage
- Keep the source metadata: `[Session ID] | [Participant ID] | [Type: observation / quote / pain_point]`
- A verbatim quote is a single unit even if long — do not split quotes

**Output**: A flat list of evidence units. Typical yield: 8–15 units per session.

---

### Step 3 — First-pass clustering (affinity mapping mode)

Group evidence units by **meaning similarity** — not by topic, keyword, or surface feature.

**Rules:**
- Name nothing yet. Move units freely. Expect to reorganize several times.
- A unit that seems to belong in two places is a signal: note it, don't force a single home
- Outlier units that resist grouping are not errors — keep them as a separate "outliers" pile
- Typical cluster count: 10–20 clusters for a 5–8 session study. More clusters is fine at this stage.

**For thematic coding mode**: Load the prior codebook or theoretical framework first. Apply existing codes in this step instead of free-clustering. Proceed to Step 4 after coding; use Step 5 to reconcile residuals.

**Analytic memo** (concurrent): As you cluster, record your reasoning. Why did you group these units together? What alternative groupings did you consider? What are you uncertain about? Save to `memos-[seed].md`. See `REFERENCE.md` → Analytic Memos.

---

### Step 4 — Name the clusters

Write a **2–5 word label** for each cluster.

**Naming rules:**
- Name the pattern, not the topic — `"Can't find saved work"` over `"Search and navigation"`
- Write from the participant's frame — `"Doesn't trust the system"` over `"Trust issues"`
- Avoid solution-implying names — `"Needs better search"` is a solution, not a theme
- Avoid evaluative names — `"Poor error handling"` describes a design failure, not a participant experience

**Run the CORE.md category audit on your names:**
- Are any names treating a spectrum as binary? (e.g., "Expert vs. novice" — is there a middle?)
- Are any names universalizing from one role's perspective?
- Do any names embed an assumption about causation? (Observed behavior ≠ known cause)

**Analytic memo** (concurrent): For each name chosen, note the alternatives rejected and why. If you renamed a cluster mid-analysis, document the reason.

---

### Step 5 — Write the codebook

For each named cluster, write a full theme definition before proceeding to second-pass coding.

**Codebook entry structure:**

```
THEME: [Name]
Definition: [1–2 sentences — what this theme captures, stated from participant perspective]
Inclusion: [What qualifies as this theme — be specific enough to decide edge cases]
Exclusion: [What is explicitly NOT this theme, especially if neighboring themes overlap]
Examples: [2–3 verbatim units from Step 2 that clearly belong here]
```

**Codebook quality checks:**
- Can you use the definition to decide a borderline case without asking the author?
- Do two different themes have overlapping inclusion criteria? If yes, clarify or merge.
- Does any theme definition smuggle in a design recommendation? Remove it.

**Coding method**: Note which coding method generated most of the evidence for each category. Common UX choices: Descriptive (topic noun phrases), In Vivo (participant's own words), Process (gerund action phrases), Versus (tension pairs — `EFFICIENCY VS. CONTROL`). See `REFERENCE.md` → Coding Method Selection.

**Analytic memo** (concurrent): Document the reasoning behind each codebook entry — especially inclusion/exclusion boundaries. What would have to be true for a borderline unit to qualify?

---

### Step 6 — Second-pass coding

Re-read every evidence unit with the codebook open. Apply codes:

- **Single code**: Unit clearly belongs to one theme
- **Multi-code**: Unit genuinely belongs to ≥ 2 themes — record both; do not force a primary
- **Residual**: Unit fits no theme — flag as `RESIDUAL`. Do not discard. Accumulate residuals; if ≥ 3 residuals share a pattern, add a new theme to the codebook.
- **Contradicting**: Unit actively contradicts a theme's dominant pattern — flag as `CONTRADICTS:[ThemeName]`. Record under that theme's negative cases.

Apply the **CORE.md edge and variance scan** during this pass:
- Which themes appear only in one role's data? Note the role explicitly.
- Which participants appear in no theme's evidence? Flag their sessions for review.
- Which themes overrepresent one session or one participant? Note the concentration.

---

### Step 7 — Negative case analysis

For each theme, search deliberately for evidence that contradicts or complicates it.

**Negative case protocol:**
1. State the dominant pattern of the theme in one sentence
2. Search all coded units for any that undercut, complicate, or invert that pattern
3. Record them explicitly under each theme in the codebook — do not suppress
4. If a negative case is strong enough to reshape the theme definition, revise it
5. If multiple negative cases cluster into a pattern, consider adding an alternative theme

A theme with zero negative cases is usually an under-examined theme, not a robust one.

---

### Step 8 — Produce the theme summary

For each theme in the final codebook:

| Field | Content |
|-------|---------|
| Theme ID | TC-01, TC-02, … |
| Theme Name | Short label from Step 4 |
| Definition | From codebook |
| Evidence Count | Total coded units |
| Sessions | How many sessions contributed evidence |
| Participants | How many distinct participants contributed |
| Roles | Which participant roles are represented |
| Confidence | High (≥ 3 sessions, multiple participants) / Medium (2 sessions or single-role) / Low (1 session or 1 participant) |
| Negative Cases | Count of contradicting evidence units |
| Feeds Into | journey-mapping / hmw-extraction / issue-log / saturation-analysis |

---

### Step 9 — Theme the Data (optional, depth mode)

TC-XX categories name patterns — they are descriptive. Themeing produces a higher-order interpretive statement that answers: *what does this pattern mean for the user's experience?*

For each category (or cluster of related categories), write a propositional theme statement:
- Not: `"TC-02: Cannot locate previous work"` (category label)
- Yes: `"Users' sense of competence in the product erodes because work they cannot locate becomes work they stop trusting the product to hold."` (interpretive theme)

**Criteria for a valid theme statement:**
- It makes a claim, not a description
- It could be argued against (it is falsifiable in principle)
- It is grounded in evidence from multiple categories
- It illuminates something not visible at the category level alone

Use Step 9 when producing a synthesis report, building a strategic narrative for stakeholders, or grounding design principles in evidence. For direct handoffs to journey-mapping, hmw-extraction, or issue-log, category-level output (TC-XX) is sufficient. See `REFERENCE.md` → Saldaña's Three Levels.

---

## Output

**Codebook**: `themes-[seed].md` — save to seed's `03_Synthesis/` directory.

**Coded dataset**: `coded-[seed].csv` — save to seed's `03_Synthesis/` directory.

CSV format:
```
Unit_ID | Session_ID | Participant_ID | Role | Type | Evidence_Unit | Theme_Codes | Multi_Code | Confidence | Notes
U-001 | S01 | P1 | Designer | quote | "I never know if my changes saved" | TC-02 | — | High | Strong example of TC-02
U-015 | S02 | P2 | Admin | observation | Clicked back button three times without finding previous screen | TC-01,TC-04 | TC-01+TC-04 | Medium | Belongs to both; spatial disorientation + lost state
U-023 | S03 | P3 | User | pain_point | Cannot export report without admin access | RESIDUAL | — | — | Possible new theme: permission barriers
```

---

## Quality Gates

✓ All sessions included — exclusions documented with reason
✓ Every evidence unit assigned a code, RESIDUAL tag, or CONTRADICTS tag — nothing silently dropped
✓ Every theme has: name, definition, inclusion criteria, exclusion criteria, ≥ 2 examples
✓ No theme defined by evidence from a single participant
✓ Multi-codes documented — not collapsed or hidden
✓ Negative cases listed for every theme (≥ 1 per theme, or explicitly note "none found, reason: [X]")
✓ Theme names describe participant-frame patterns — not topics, solutions, or design judgments
✓ CORE.md edge scan completed — participant/role gaps noted in codebook header
✓ Analytic memos maintained — at minimum one memo entry per clustering decision and one per codebook definition written
✓ Residuals reviewed — clusters of ≥ 3 resolved into new themes or documented as outliers
✓ Codebook and coded dataset saved to `03_Synthesis/`

---

## References

- `REFERENCE.md` — affinity vs. thematic coding depth, atomic decomposition edge cases, inter-rater reliability, codebook evolution, cross-persona analysis; Saldaña's three levels (code/category/theme), analytic memos, coding method selection, code mapping
- `EXAMPLES.md` — one complete worked example from raw session data to codebook to coded dataset
- `TEMPLATE.md` — blank codebook entry, blank coded CSV headers, blank theme summary table
- `scripts/code_themes.py` — Python utility: extracts evidence units from session note CSVs and produces a blank coding workspace
