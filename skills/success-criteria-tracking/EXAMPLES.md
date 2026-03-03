# Success Criteria Tracking: Complete Example

## Scenario: Collaborative Research Dashboard Study (5 Sessions)

A team ran 5 sessions testing a collaborative dashboard prototype. Success criteria were defined upfront to evaluate:
- Whether the dashboard meets user task completion targets
- Whether team collaboration features work as intended
- Whether code quality and documentation standards are met
- Whether stakeholders approve the design direction

---

## Success Criteria Definition Table

| Criterion_ID | Criterion_Name | Type | Must_Have | Description | Threshold | Target |
|---|---|---|---|---|---|---|
| Q1 | Task Completion Rate | Q | Yes | % of assigned tasks completed by users | ≥75% | ≥90% |
| Q2 | Average Session Duration | Q | No | Mean time spent per session (minutes) | ≥12 min | ≥20 min |
| C1 | Collaboration Feature Adoption | B | Yes | % of sessions where team used shared features | ≥70% | ≥90% |
| C2 | Design Alignment Rating | Q | Yes | Expert review of design (1–5 scale) | ≥3.5 | ≥4.5 |
| D1 | Code Quality Score | Q | No | Code clarity + maintainability (1–10 scale) | ≥7 | ≥8.5 |
| D2 | Documentation Completeness | Q | No | % of functions with docstrings | ≥80% | ≥95% |

---

## Session-by-Session Scoring

### Session 1 (Baseline)

| Criterion_ID | Metric | Result | Status | Confidence | Notes |
|---|---|---|---|---|---|
| Q1 | Task Completion | 6/10 tasks = 60% | Fail | High | Prototype stability issues; UX not intuitive |
| Q2 | Session Duration | 8 minutes (mean) | Fail | High | Users completed tasks faster than expected; may indicate issues |
| C1 | Collab Feature Use | 3/5 team members used shared features | 60% | High | Most users didn't discover collaboration panel |
| C2 | Design Alignment | 2.5/5 (expert review) | Fail | High | Layout doesn't match brand guidelines; color scheme off |
| D1 | Code Quality | 5.5/10 | Fail | High | Code readable but inconsistent naming; minimal comments |
| D2 | Documentation | 4/10 functions = 40% | Fail | High | Only core functions documented |

**Session 1 Summary**: Baseline poor across board. Multiple must-haves failing. Root causes identified: UX issues, design misalignment, incomplete documentation.

---

### Session 2 (After Design Revision)

| Criterion_ID | Metric | Result | Status | Confidence | Notes |
|---|---|---|---|---|---|
| Q1 | Task Completion | 8/10 tasks = 80% | Pass | High | UX improvements working; one task still confusing |
| Q2 | Session Duration | 15 minutes (mean) | Pass | High | Users spending more time exploring features |
| C1 | Collab Feature Use | 5/5 team members used shared features | 100% | High | Collaboration panel now visible; adoption strong |
| C2 | Design Alignment | 4.0/5 (expert review) | Pass | High | Layout revised; color scheme now compliant; minor spacing issues |
| D1 | Code Quality | 7.0/10 | Pass | High | Added comments; consistent naming applied |
| D2 | Documentation | 8/10 functions = 80% | Pass | High | Filled in docstrings; 2 functions still lack detail |

**Session 2 Summary**: Major improvement. Q1, C1, C2, D1, D2 all pass. Q2 passes new threshold. Revisions addressed root causes. Confidence high across board.

---

### Session 3 (Stress Test)

| Criterion_ID | Metric | Result | Status | Confidence | Notes |
|---|---|---|---|---|---|
| Q1 | Task Completion | 7/10 tasks = 70% | Fail | High | Edge case: users struggled with bulk operations (not in S1–S2) |
| Q2 | Session Duration | 18 minutes (mean) | Pass | High | Exploration time increased; power users investigating advanced features |
| C1 | Collab Feature Use | 4/5 team members used shared features | 80% | High | One user didn't open collab panel (individual working style) |
| C2 | Design Alignment | 4.2/5 (expert review) | Pass | High | Spacing fixed from S2 feedback; design now aligned |
| D1 | Code Quality | 7.5/10 | Pass | High | Code refactoring improved; complexity reduced |
| D2 | Documentation | 9/10 functions = 90% | Pass | High | Nearly complete; one legacy function pending rewrite |

**Session 3 Summary**: Mostly stable. Q1 fails (regression), discovered new edge case. Other criteria hold or improve. Q2, C2, D1, D2 improving. Investigate Q1 drop.

---

### Session 4 (After Edge Case Fix)

| Criterion_ID | Metric | Result | Status | Confidence | Notes |
|---|---|---|---|---|---|
| Q1 | Task Completion | 9/10 tasks = 90% | Pass | High | Bulk operation flow fixed; clarity improved |
| Q2 | Session Duration | 22 minutes (mean) | Pass | High | Users now exploring advanced workflows; higher engagement |
| C1 | Collab Feature Use | 5/5 team members used shared features | 100% | High | Previous non-adopter now regularly using collab features |
| C2 | Design Alignment | 4.4/5 (expert review) | Pass | High | Minor polish remaining; design essentially ready |
| D1 | Code Quality | 8.0/10 | Pass | High | Refactoring complete; code now maintainable and clear |
| D2 | Documentation | 10/10 functions = 100% | Pass | High | All functions now fully documented; criteria met |

**Session 4 Summary**: Strong pass across all criteria. Q1 recovered. Q2, C2, D1, D2 trending positive. Confidence high across board. Most criteria now exceeding target.

---

### Session 5 (Final Validation)

| Criterion_ID | Metric | Result | Status | Confidence | Notes |
|---|---|---|---|---|---|
| Q1 | Task Completion | 9/10 tasks = 90% | Pass | High | Consistent high performance; one edge case task remains challenging |
| Q2 | Session Duration | 25 minutes (mean) | Pass | High | Users deeply engaged; exploring multiple workflows |
| C1 | Collab Feature Use | 5/5 team members used shared features | 100% | High | Consistent adoption; collab is central to workflow |
| C2 | Design Alignment | 4.5/5 (expert review) | Pass | High | Design approved; minor polish suggestions documented for v2 |
| D1 | Code Quality | 8.2/10 | Pass | High | Code remains maintainable; consistent refactoring throughout |
| D2 | Documentation | 10/10 functions = 100% | Pass | High | All functions fully documented; documentation quality excellent |

**Session 5 Summary**: Sustained excellence. All criteria pass. Trends stable or improving. High confidence across board. Dashboard ready for launch.

---

## Aggregate Tracking Matrix

| Criterion_ID | Criterion_Name | Type | Must_Have | S1 | S2 | S3 | S4 | S5 | Pass_Rate | Status | Confidence | Overall Trend | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | Task Completion | Q | Yes | 60% | 80% | 70% | 90% | 90% | 80% | Pass | High | Recovering | Initial UX issues fixed by S2; slight dip S3 (edge case); stable S4–S5 at 90% |
| Q2 | Session Duration | Q | No | 8m | 15m | 18m | 22m | 25m | N/A | Pass | High | Strong↑ | Steady increase indicates higher user engagement |
| C1 | Collab Adoption | B | Yes | 60% | 100% | 80% | 100% | 100% | 88% | Pass | High | Recovering | Feature discovery improved S2; one outlier in S3 (user preference) |
| C2 | Design Alignment | Q | Yes | 2.5 | 4.0 | 4.2 | 4.4 | 4.5 | 80% | Pass | High | Strong↑ | Steady improvement; achieved target 4.5 in S5 |
| D1 | Code Quality | Q | No | 5.5 | 7.0 | 7.5 | 8.0 | 8.2 | 80% | Pass | High | Strong↑ | Consistent improvement; exceeded target 8.5 by S4+ |
| D2 | Documentation | Q | No | 40% | 80% | 90% | 100% | 100% | 100% | Pass | High | Strong↑ | Achieved 100% by S4; sustained in S5 |

---

## Root-Cause Analysis for Failures

### Q1 (Task Completion) - Session 1 Failure

**What failed**: 60% completion; threshold ≥75%

**Root cause analysis**:
- **Primary**: UX unclear on bulk operations (users didn't understand how to select multiple items)
- **Secondary**: Prototype stability issues caused some tasks to fail at the system level
- **Measurement**: Clear and reliable (observed directly during sessions)

**Fixability**: High
- Clarify bulk operation UX in prototype
- Fix stability bugs
- Expected improvement: 15–20% (to 75–80%)

**Action taken**: Redesigned bulk operation panel, simplified interaction model
**Result**: Q1 improved to 80% in S2 ✓

---

### Q2 (Session Duration) - Session 1 Failure

**What failed**: 8 min average; threshold ≥12 min

**Root cause analysis**:
- **Primary**: Users completed tasks quickly; may indicate tasks were too simple or UX was too obvious
- **Secondary**: Users exited when they encountered confusing bulk operations (S1 issue)
- **Measurement**: Reliable (timer logs)

**Interpretation**: This is not a user failure but a design interpretation issue. Users completing tasks quickly could be positive (efficient UX) or negative (missing features). Stakeholders clarified: want 12+ min because users should explore advanced features.

**Action taken**: Added richer task scenarios in S2+ to encourage deeper exploration
**Result**: Q2 improved to 15 min in S2, steady increase thereafter ✓

---

### C1 (Collab Feature Adoption) - Session 1 Failure

**What failed**: 60% adoption; threshold ≥70%

**Root cause analysis**:
- **Primary**: Collaboration panel was hidden behind a menu; users didn't discover it
- **Secondary**: UX flow prioritized individual work before collaboration
- **Measurement**: Clear (observed which users clicked collab features)

**Fixability**: High
- Make collaboration panel visible by default
- Redesign workflow to introduce collaboration earlier
- Expected improvement: 30–40% (to 90%+)

**Action taken**: Added collaboration panel to main dashboard; prompted users to try shared features
**Result**: C1 jumped to 100% in S2 ✓

---

### C2 (Design Alignment) - Session 1 Failure

**What failed**: 2.5/5 rating; threshold ≥3.5

**Root cause analysis**:
- **Primary**: Layout didn't follow brand guidelines (spacing, proportions off)
- **Secondary**: Color palette didn't match brand identity
- **Measurement**: Expert review (design expert rating; medium reliability due to subjectivity)

**Fixability**: High
- Audit design against brand guidelines
- Apply correct spacing and colors
- Expected improvement: 1.0–1.5 points (to 3.5–4.0)

**Action taken**: Brand audit conducted; design refreshed to match guidelines
**Result**: C2 improved to 4.0 in S2, reached 4.5 target in S5 ✓

---

### D1 (Code Quality) - Session 1 Failure

**What failed**: 5.5/10 rating; threshold ≥7

**Root cause analysis**:
- **Primary**: Inconsistent naming conventions (mix of camelCase and snake_case)
- **Secondary**: Minimal comments; logic not explained
- **Measurement**: Code review rubric (mostly objective with minor interpretation)

**Fixability**: High
- Apply naming conventions consistently
- Add inline comments for non-obvious logic
- Expected improvement: 1.5–2.0 points (to 7.0–7.5)

**Action taken**: Code style guide created; team applied refactoring; review process added
**Result**: D1 improved to 7.0 in S2, exceeded 8.0+ by S4 ✓

---

### D2 (Documentation) - Session 1 Failure

**What failed**: 40% functions documented; threshold ≥80%

**Root cause analysis**:
- **Primary**: Time pressure; developers documented core functions only
- **Secondary**: No documentation standard defined
- **Measurement**: Clear (counted functions with docstrings)

**Fixability**: High
- Require docstrings as part of code review
- Define documentation template
- Expected improvement: 40% per session until 100%

**Action taken**: Added docstring requirement to code review checklist; template created
**Result**: D2 steadily improved to 100% by S4 ✓

---

## Summary Metrics and Decisions

### Per-Criterion Analysis

**Must-Have Criteria** (required for Go decision):
- **Q1 (Task Completion)**: Pass at High confidence (80% pass rate across 5 sessions) ✓
- **C1 (Collab Adoption)**: Pass at High confidence (88% pass rate; 4/5 sessions 100%) ✓
- **C2 (Design Alignment)**: Pass at High confidence (80% sessions ≥3.5; upward trend) ✓

**Nice-to-Have Criteria**:
- **Q2 (Session Duration)**: Pass at High confidence (all 5 sessions exceed 12 min; strong↑ trend) ✓
- **D1 (Code Quality)**: Pass at High confidence (80% sessions ≥7; strong↑ trend) ✓
- **D2 (Documentation)**: Pass at High confidence (100% sessions reach 80%+ by S4) ✓

### Confidence Assessment

| Factor | Assessment | Confidence |
|---|---|---|
| Sample size | n=5 for all criteria | High |
| Consistency | Low variance S2–S5; S1 outlier explained | High |
| Data quality | Objective metrics + expert review; measurement reliable | High |
| **Overall** | | **High** |

---

## Go/No-Go Recommendation

### Decision Logic

**Criteria for Go**:
1. ✓ All must-haves pass (Q1, C1, C2 all pass)
2. ✓ Pass rate ≥80% at High confidence (Q1=80%, C1=88%, C2=80%)
3. ✓ Positive or stable trends (Q1 recovering, C1 stable, C2 strong↑)
4. ✓ ≥50% of nice-to-haves pass (100% pass; Q2, D1, D2 all exceed targets)
5. ✓ Root causes understood and fixed (all S1 failures fixed by S2–S3)

**Result**: All 5 conditions met

---

## RECOMMENDATION: GO ✓

**Summary**: Dashboard is ready for launch. All must-have success criteria pass at high confidence with strong trends.

**Key Findings**:
- **Task completion** stabilized at 90% (threshold ≥75%) after UX fixes in S2
- **Collaboration adoption** strong at 88% average; feature discovery improved once made visible
- **Design alignment** achieved target 4.5/5 by S5; brand compliance confirmed
- **Code quality** improved consistently; now 8.2/10 (exceeds 7.0 threshold; approaches 8.5 target)
- **Documentation** achieved 100% by S4; sustained in S5

**Next Steps**:
1. **Launch to production** with confidence in quality
2. **Monitor post-launch** task completion and collaboration adoption in live usage
3. **Document minor issues** for v2 iteration:
   - One bulk operation edge case (90% vs 100% completion) — minor impact
   - Design polish suggestions from final expert review — purely aesthetic
4. **Plan iteration 2** to address nice-to-have enhancements (target Q2 ≥25 min, D1 ≥8.5)

**Risk Level**: Low. All must-haves pass; root causes of early failures were understood and fixed; sustained performance through final session.

---

## Template: Adapting This Example to Your Research

Use this structure for your own success criteria tracking:

1. **Define criteria table** (6–8 criteria; 2–4 must-have)
2. **Run 5+ sessions** (collect n≥5 for High confidence)
3. **Score each session** using consistent measurement procedure
4. **Aggregate results** with pass rates, trends, confidence
5. **Root-cause failures** to understand fixability
6. **Synthesize into Go/No-Go** using decision logic above

Key principles from this example:
- **Early failures are normal**: S1 had 4 failures; all were addressed by S2–S3
- **Trends matter**: Q1 dropped S3 but recovered S4–S5; showed issue was fixable
- **Confidence increases with sample size**: High confidence only after n≥5
- **Nice-to-haves inform iteration**: Not blockers, but reveal improvement opportunities
