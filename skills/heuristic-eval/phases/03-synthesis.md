---
name: heuristic-eval
description: >
  Phase 3 — Heuristic Synthesis. Synthesizes automated and visual findings into a severity-rated
  evaluation report with plural interpretations. Use after evidence collection is complete.
license: "Valtech / John Deere — Internal Use Only"
metadata:
  author: "Juan Reina (they/them)"
  phase: "03-synthesis"
  phase_name: "Heuristic Synthesis"
  inputs: heuristic-findings.json, discovery brief, screenshots
  outputs: evaluation report (markdown)
  feeds_into: phases/04-handoff.md
---

# Phase 3 — Heuristic Synthesis

**Goal:** Synthesize all evidence into a clear, honest, evidence-grounded evaluation report.
The report serves two simultaneous audiences: a designer or developer who needs to act on
specific findings, and a researcher or stakeholder who needs to understand patterns and prioritize.

> **Load `references/nng-heuristics-guide.md`** for per-heuristic severity calibration guidance.

---

## Step 1: Gather all inputs

Read:
- The `heuristic-findings.json` from Phase 2
- The discovery brief from Phase 1 (for user context, journey structure, and heuristic hypotheses)
- Screenshots from `artifacts/screenshots/` — look at them, do not just reference them

If no `heuristic-findings.json` exists (manual evaluation), ask the user to describe their
observations. Structure their notes using the finding format below and proceed.

---

## Step 2: Enrich findings with visual/AI judgment

The automated findings capture rule-based violations. Before scoring, enrich:

For each of the 10 heuristics, check whether there is evidence. If a heuristic has no
automated findings:
- Mark it **"No automated violations detected — visual review recommended"** (not "Passed")
- Only mark a heuristic as "No violations detected" if you have *positive* evidence — i.e.,
  you examined the product and it demonstrably passes

For heuristics that require visual/AI judgment (H2, H7, H8, H9, H10), add observations
based on screenshot review and product knowledge. Label these observations as
**Source: Visual review** to distinguish them from automated findings.

---

## Step 3: Calibrate severity *after* seeing the full set

Do not finalize severity ratings until all findings are collected. Severity is relative —
a Severity 3 in isolation may become Severity 4 when seen as part of a systemic pattern,
or become Severity 2 when the affected flow is low-frequency.

Apply severity calibration rules from `REFERENCE.md`:
- Increase by 1 for systemic patterns (≥ 3 screens), high-frequency tasks, or disproportionate
  impact on assistive technology users or non-primary language users
- Decrease by 1 for edge-case flows, expert user populations, or low-confidence evidence

For every Severity 3–4 finding: apply the **plural interpretations requirement** from `CORE.md`.
Provide ≥ 2 plausible interpretations, including at least one that differs from the most
obvious reading.

---

## Step 4: Score each heuristic

For each of the 10 heuristics, assign:

| Field | Options |
|-------|---------|
| Status | 🔴 Critical / 🟠 Issues found / 🟡 Minor issues / 🟢 No violations detected / ⚪ Not evaluated |
| Finding count | number |
| Max severity | 0–4 |
| Coverage | Automated / Visual review / Both / Not evaluated |

Use "🔴 Critical" only when Severity 4 findings exist. Use "⚪ Not evaluated" when
the heuristic was not covered in the evidence phase.

---

## Step 5: Write the report

Output file: `heuristic-report-[product]-[YYYY-MM-DD].md`

Use the template below. Do not skip sections — write "N/A — [reason]" for any section
that does not apply.

---

```markdown
---
document type: heuristic evaluation report
product: [product name]
url: [URL]
date: [Month YYYY]
evaluator: [name]
methodology: Nielsen Norman Group 10 Usability Heuristics
seed_connection: [seed name or "standalone"]
verified: false
---

# Heuristic Evaluation Report
## [Product Name]

**URL evaluated:** [URL]
**Evaluation date:** [date]
**Methodology:** Nielsen Norman Group 10 Usability Heuristics
**Evidence collection:** [Automated (Playwright) + Visual review / Manual only]
**Evaluator:** [name]

---

## Executive Summary

[Paragraph 1: What the product is and who it serves — be specific about the user range.]

[Paragraph 2: Overall UX quality assessment — be honest and specific. Avoid generic
statements like "the product has room for improvement." Name the 2–3 most significant
patterns.]

[Paragraph 3: Top priorities — name the specific heuristics or finding clusters that most
need attention, and why they matter now.]

**Overall UX Quality Score: [X]/10**

*Score formula: start at 10, subtract 1.0 per Severity-4, 0.5 per Severity-3,
0.25 per Severity-2, 0.1 per Severity-1. Minimum 1. Round to nearest 0.5.*

*Note: This score reflects the scope of this evaluation only. Coverage gaps are noted
below. The score should not be treated as a definitive measure of product quality.*

---

## Heuristic Scorecard

| # | Heuristic | Status | Findings | Max Severity | Coverage |
|---|-----------|--------|----------|--------------|---------|
| H1 | Visibility of System Status | [emoji] | [n] | [0–4] | [type] |
| H2 | Match Between System and Real World | [emoji] | [n] | [0–4] | [type] |
| H3 | User Control and Freedom | [emoji] | [n] | [0–4] | [type] |
| H4 | Consistency and Standards | [emoji] | [n] | [0–4] | [type] |
| H5 | Error Prevention | [emoji] | [n] | [0–4] | [type] |
| H6 | Recognition Over Recall | [emoji] | [n] | [0–4] | [type] |
| H7 | Flexibility and Efficiency | [emoji] | [n] | [0–4] | [type] |
| H8 | Aesthetic and Minimalist Design | [emoji] | [n] | [0–4] | [type] |
| H9 | Error Recovery | [emoji] | [n] | [0–4] | [type] |
| H10 | Help and Documentation | [emoji] | [n] | [0–4] | [type] |

**Total findings:** [n] | **Critical (Sev 3–4):** [n] | **Recommended (Sev 2):** [n] | **Low priority (Sev 0–1):** [n]

---

## Critical Findings (Severity 3–4)

*These findings directly impede task completion or severely degrade experience.
Address before the next release.*

### [Finding title — specific and descriptive]

**Heuristic:** [H# — Name]
**Severity:** [4 — Catastrophic / 3 — Major]
**Journey affected:** [journey name]
**URL:** [page URL]
**Evidence source:** [Automated / Visual review]

**What is happening:**
[1–2 sentences in plain language. What does the user experience? What fails to happen
that should happen?]

**Evidence:**
[Quote from findings JSON, or description of what the screenshot shows.
Include screenshot filename if available.]

**Why it matters — Interpretation 1 (primary):**
[Connect to user impact. Not "this is bad UX" but what specific consequence it creates:
abandonment, errors, task failure, exclusion of a user group.]

**Why it matters — Interpretation 2 (alternative):**
[A different reading: different user population, different root cause, or different
severity assessment. See REFERENCE.md for plurality guidance.]

**Uncertainty flag:** [Document what you don't know — does this affect all users or a subset?
Is the severity conditional on user context?]

---

[Repeat for all critical findings]

---

## Recommended Fixes (Severity 2)

*These create friction. Address in the next development cycle.*

[For each finding, a more concise version of the critical finding format.
3–4 sentences per finding. Group by heuristic if there are many.]

### [Finding title]

**Heuristic:** H[n] | **Severity:** 2 | **Journey:** [name] | **URL:** [URL]

[Description + evidence + recommended action in 3–4 sentences. Include a specific,
buildable recommendation — not generic guidance.]

---

[Repeat]

---

## Low Priority / Cosmetic (Severity 0–1)

*Nice to fix, minimal impact on task completion.*

- **H[n]** — [Brief description] — [One-line recommendation]

---

## Heuristic Deep-Dives

*One section per heuristic with findings. Skip heuristics with no findings.*

### H[n]: [Heuristic Name]

**Definition:** [One sentence — what this heuristic means in practice]
**What was evaluated:** [Which journeys / pages were covered]
**Findings summary:** [2–3 sentences synthesizing all findings for this heuristic]
**Systemic pattern:** [Does this appear across multiple screens / flows, or is it isolated?]

---

## User Journey Evaluation

*One section per journey.*

### Journey [n]: [Journey Name]

**Path evaluated:** [start URL → end URL]
**Overall assessment:** [Excellent / Good / Needs Work / Broken — with a one-sentence rationale]

[2–3 sentences: what works well, what doesn't, the single most impactful issue in this journey]

**Findings in this journey:**
[List of finding titles with severity]

---

## Recommendations Summary

### Immediate — fix before next release

[Numbered list of Sev 3–4 finding titles with one-line fix summaries]

### Next cycle

[Numbered list of Sev 2 findings]

### Backlog

[Bulleted list of Sev 0–1 cosmetic issues]

---

## Evaluation Coverage and Limitations

**What was evaluated:**
[List journeys, user flows, and viewports covered]

**What was NOT evaluated:**
[Be explicit. Use the standard coverage gaps from REFERENCE.md as a starting checklist.
For each gap, note the potential impact on findings: "Authenticated state not tested —
findings may not reflect the full logged-in experience."]

**Evaluator bias acknowledgment:**
[Who performed this evaluation, what background shaped the analysis,
and what a different evaluator might interpret differently.]

---

## Appendix: All Findings

*Full structured list for handoff and issue-log entry generation in Phase 4.*

| ID | Heuristic | Severity | Journey | Finding title | Evidence source |
|----|-----------|----------|---------|---------------|-----------------|
| HE-001 | H[n] | [0–4] | [name] | [title] | [source] |

```

---

## Handoff to Phase 4

After the report is saved:

1. Share the file location with the user.
2. Note how many Sev 3–4 findings need actions and how many reveal unresolved questions.
3. Say: "Phase 4 will convert these findings into designer action briefs, HMW statements,
   issue log entries, and research seed briefs for any findings that require follow-on
   investigation. Load `phases/04-handoff.md` with this report to continue."
