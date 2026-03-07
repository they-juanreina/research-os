---
name: success-criteria-tracking
description: "Tracks research success criteria against session outcomes. Use when evaluating whether research objectives are being met, computing pass/fail metrics per criterion, and generating go/no-go recommendations. Maps research plan criteria to measurable indicators and tracks progress per session. Triggers: success criteria, research objectives, pass fail, go no-go, criteria tracking, research success, acceptance criteria, metrics tracking."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-02-28
---

# Success Criteria Tracking

> Apply `CORE.md` epistemic framework before scoring. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Research plan (with success criteria defined), session notes or outcome data.
**Output**: Tracking matrix with per-criterion status, confidence levels, and Go/No-Go recommendation.

---

## Criterion Types

| Type | Measured By | Example |
|------|-------------|---------|
| **Quantitative** | Numbers, counts, rates | Task completion %, avg time on task, error count |
| **Qualitative** | Rubric or expert judgment (scale or Y/N) | Code clarity (1–5), design alignment (yes/no) |
| **Behavioral** | Observable action occurrence rate | User initiates session, team adopts tool |

---

## Workflow

1. **Extract criteria** — From the research plan. For each: ID (Q1, B1, C1), name, type, must-have status.

2. **Define measurable indicators** — The exact metric or evidence that demonstrates success for each criterion.

3. **Set thresholds** — Minimum acceptable value + optional aspirational target + required confidence level.

4. **Score each session** — For each criterion: raw result, Status (Pass / Fail / Partial), Confidence (High / Medium / Low), Notes.

5. **Compute aggregates** — Per criterion across all sessions: pass rate, trend (improving / stable / declining), overall status.

6. **Assess confidence** — Overall confidence = *lowest* of the three factors:
   - **Sample size**: High n ≥ 5 | Medium n = 3–4 | Low n < 3
   - **Consistency**: High < 10% variance | Medium 10–30% | Low > 30%
   - **Data quality**: High (objective metric) | Medium (minor ambiguity) | Low (subjective/conflicting)

7. **Root-cause failed criteria** — What caused the failure? Design flaw, implementation issue, measurement problem, or external factor? Is it fixable in remaining sessions?

8. **Go/No-Go recommendation**:
   - **Go** — All must-haves pass at high confidence; trends positive or stable.
   - **Caution** — Some must-haves pass with low confidence; significant unmet nice-to-haves; declining trends.
   - **No-Go** — Critical must-haves fail; unresolvable design issues; insufficient confidence in core metrics.

---

## Output Format

Tracking matrix (CSV or table):

```
Criterion_ID | Name | Type | Must_Have | S1 | S2 | S3 | S4 | S5 | Pass_Rate | Status | Confidence | Notes
Q1 | Task Complete | Q | Yes | P | P | F | P | P | 80% | Pass | High | S3 had significant distraction
B1 | User Adopts | B | Yes | Y | Y | N | Y | Y | 80% | Pass | Medium | n=5 only
C1 | Code Quality | Q | No | 9 | 8 | 8 | 7 | 8 | N/A | Pass | High | Mean 8/10, target ≥ 7
```

Per-session columns: P = Pass, F = Fail, numeric value, or Y/N.

---

## Quality Gates

✓ Every must-have criterion scored — if data is missing, note "Insufficient data" and plan to measure next session
✓ Partial passes explained in Notes
✓ Trends weighted more than single-session anomalies
✓ No Go/No-Go recommendation from Low-confidence must-haves — collect more data first
✓ Root causes are actionable, not situational ("instructions unclear — revise" not "participant was tired")

---

## References

- `REFERENCE.md` — threshold-setting strategies, confidence tables, root-cause framework, Go/No-Go decision trees, edge cases
- `EXAMPLES.md` — complete 5-session, 6-criterion worked example with failure-to-recovery arc
- `scripts/track_criteria.py` — Python tracking utility
