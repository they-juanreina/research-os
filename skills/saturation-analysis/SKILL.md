---
name: saturation-analysis
description: "Analyzes whether qualitative research has reached thematic saturation. Use when determining if additional research sessions are needed or if diminishing returns have been reached. Tracks new-theme emergence per session, computes saturation metrics, and recommends continue/pause/conclude. Triggers: saturation, enough sessions, diminishing returns, theme tracking, research completeness, stop collecting data, sufficient data."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-02-28
---

# Saturation Analysis

> Apply `CORE.md` epistemic framework before assessing. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Session notes in chronological order with dates and participant roles.
**Output**: Saturation report with theme tracking table, metrics, curve narrative, and recommendation.

---

## Theme Classification

- **New theme** — Concept or pattern not seen in any prior session.
- **Variant** — Reframing or subcategory of an existing theme (e.g., "dark mode in low-light" when "dark mode" already exists). Counts as partial emergence.
- **Confirmation** — Same theme expressed again; no new emergence.

---

## Workflow

1. **Read chronologically** — Extract date, participant role, and main themes per session. Note sessions with significant variation in depth or length.

2. **Define and extract themes** — Apply New / Variant / Confirmation classification. Themes must be distinct; check for duplicates under different names.

3. **Build tracking table** — Columns: Session # | Date | Role | Themes Identified | New Themes (count) | Cumulative Unique Themes.

4. **Compute metrics**:
   - Sessions since last new theme
   - 3-session rolling average (new themes/session, smooths noise)
   - Emergence rate: new themes ÷ total sessions (overall and by role)
   - Saturation %: `(unique themes) / (unique + estimated remaining) × 100`

5. **Examine the curve** — Plot cumulative unique themes over session number. Typical arc: sharp early climb → moderate growth → plateau. Saturation = significant, sustained flattening.

6. **Role-specific analysis** — If roles differ (users, developers, managers), compute saturation per role. A role may be saturated while others aren't; flag accordingly.

7. **Recommend** — Use the threshold table below. State which threshold was applied and why.

---

## Recommendation Thresholds

| Metric | Continue | Consider Pausing | Conclude |
|--------|----------|-----------------|----------|
| Sessions since last new theme | < 2 | 2–3 | ≥ 4 |
| 3-session rolling avg | ≥ 1.5 | 0.5–1.5 | < 0.5 |
| Emergence rate | > 20%/session | 10–20% | < 10% |
| Saturation % | < 70% | 70–85% | > 85% |

**Conservative** (high-stakes / comprehensive): ≥ 12 sessions, last 5 show 0 new themes, saturation > 90%, all roles flat.
**Moderate** *(recommended)*: ≥ 8 sessions, last 3 show ≤ 1 new theme total, saturation > 80%, most roles flat.
**Aggressive** (time-constrained): ≥ 6 sessions, last 2 show 0 new themes, saturation > 70%, emergence rate < 10%.

---

## Output Format

```
SATURATION ANALYSIS REPORT
===========================
Dataset: [name/study] | Sessions: [N] | Roles: [list] | Date: [date]

THEME TRACKING TABLE
[table]

METRICS
- Sessions since last new theme: X
- 3-session rolling avg: Y
- Emergence rate: Z%
- Saturation %: A%

CURVE NARRATIVE: [1–2 sentences describing shape — spike, growth phase, plateau behavior]

ROLE FINDINGS: [1–2 sentences per role, if applicable]

RECOMMENDATION: [Continue | Consider Pausing | Conclude]
Threshold applied: [Conservative / Moderate / Aggressive]
Rationale: [1–2 sentences citing specific metrics]
```

---

## Quality Gates

✓ All themes are distinct — no duplicates under different names
✓ New themes are truly novel, not minor variants
✓ Minimum session count met for the chosen threshold
✓ Curve shows consistent pattern, not random noise
✓ Role-specific analysis conducted if roles vary

---

## References

- `REFERENCE.md` — theme decision rules, curve interpretation, edge cases (outliers, homogeneous samples, late themes), confidence levels
- `EXAMPLES.md` — five complete examples: clear saturation, early stop, continue, late outlier, mixed-role recommendation
- `scripts/compute_saturation.py` — Python saturation computation utility
