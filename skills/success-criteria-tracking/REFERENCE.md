# Success Criteria Tracking: Reference Guide

## Criterion Types: Detailed Definitions

### Quantitative Criteria

**Definition**: Success is measured by a numeric outcome. Results are objective and independent of observer.

**Characteristics**:
- Results can be repeated with minimal variation
- Thresholds are set as ranges or exact values
- Confidence in measurement is typically high

**Measurement Examples**:
- **Completion metrics**: Task completion rate (%), tasks completed per session, time to completion (seconds)
- **Performance metrics**: Error count, success-to-failure ratio, mean response time, throughput
- **Adoption metrics**: % of sessions using feature, adoption by week, user retention %
- **Quality metrics**: Code coverage (%), test pass rate (%), lines of code per function, cyclomatic complexity

**Setting Thresholds**:
- Minimum threshold: The lowest acceptable value (usually 70–80% for pass rates)
- Target threshold: The aspirational value (usually 90%+)
- Example: Q1 threshold is ≥80% task completion; target is 95%

**How to Measure**:
- Count: "5 out of 10 users completed the task" → 50%
- Time: Use stopwatch or logs; report mean, median, min, max
- Aggregate: Sum results across sessions, divide by total
- Automate: Use scripts, analytics dashboards, code metrics tools

---

### Qualitative Criteria

**Definition**: Success is assessed by human judgment on a scale or as yes/no. Results depend on the evaluator's interpretation.

**Characteristics**:
- Requires a rubric or scoring guide
- Confidence in measurement is typically medium (depends on rater consistency)
- More flexible than quantitative; captures nuance

**Measurement Examples**:
- **Scale-based**: Code clarity (1=unintelligible to 5=perfectly clear), explanation comprehensiveness (1–5 scale), design adherence (1–5 scale)
- **Checklist**: Does code follow style guide? (Yes/No), Is documentation complete? (Yes/No), Does design match brand? (Yes/No)
- **Ranking**: Rate user satisfaction (Very dissatisfied, Dissatisfied, Neutral, Satisfied, Very satisfied)
- **Expert review**: "Does this solution meet accessibility standards?" (Yes/No)

**Setting Thresholds**:
- Scale-based: Minimum score (e.g., ≥4 on 5-point scale)
- Checklist: % of items passing (e.g., ≥90% of checklist items met)
- Ranking: % of sessions meeting "Satisfied" or better (e.g., ≥80%)

**How to Measure**:
1. Create a rubric with clear definitions for each score level
2. Assign one evaluator per criterion (or average if multiple evaluators)
3. Apply rubric consistently to each session
4. Record score and any notes (e.g., "S3 was unclear due to time constraint")
5. Compute aggregate: mean score or % passing threshold

**Example Rubric: Code Clarity**:
```
1 = Unreadable; no comments; non-standard naming
2 = Difficult to follow; minimal comments
3 = Readable; adequate comments; mostly standard naming
4 = Clear; well-commented; consistent style
5 = Excellent; self-documenting code; comprehensive comments
```

---

### Behavioral Criteria

**Definition**: Success is whether a specific action or behavior occurs. Results are binary (happened or didn't) but can be aggregated into adoption rates.

**Characteristics**:
- Observable and unambiguous
- Aggregated as occurrence rate (% of sessions where behavior was observed)
- Confidence can be high if measurement is systematic

**Measurement Examples**:
- **Adoption**: Researcher implements recommendation (Yes/No), team member uses tool (Yes/No), stakeholder approves design (Yes/No)
- **Engagement**: User initiates session without prompt (Yes/No), user returns in next week (Yes/No), user customizes settings (Yes/No)
- **Collaboration**: Team holds weekly sync (Yes/No), feedback is incorporated (Yes/No), knowledge is documented (Yes/No)

**Setting Thresholds**:
- Occurrence rate: % of sessions where behavior observed (e.g., ≥80% adoption)
- Example: B1 threshold is "behavior occurs in ≥4 out of 5 sessions" = 80%

**How to Measure**:
1. Define the behavior precisely (e.g., "team member attends 3+ of 4 scheduled syncs" counts as engaged)
2. Record per session: Yes or No
3. Compute rate: count Yes outcomes ÷ total sessions
4. Aggregate across users if multiple actors

---

## Threshold-Setting Guidelines

### Realistic Thresholds (What to Actually Expect)

**Quantitative**:
- Task completion: 70–80% is realistic in user research
- Error rates: Expect 5–15% errors in first session; decline to <5% by session 3+
- Performance: Improvement of 10–20% session-over-session is healthy
- Adoption: 50% adoption by session 2; 70%+ by session 4+

**Qualitative**:
- Scale-based scores: Mean of 3.5+ on 5-point scale is good
- Checklist pass rate: 80%+ of items met is realistic; 100% is rare
- Expert review: 70%–80% of sessions getting "approved" is typical

**Behavioral**:
- Single action: 60–70% per session is typical; 80%+ is strong
- Consistent behavior (repeated across sessions): 70%+ is realistic; 90%+ is excellent

### Aspirational Thresholds (What You'd Like to Achieve)

Set separate "target" thresholds for planning purposes:
- Quantitative: 90%+ for mission-critical; 85%+ for important
- Qualitative: 4.5+ on 5-point scale; 100% checklist pass (or 95% for complex checklists)
- Behavioral: 90%+ adoption; 100% engagement for critical actions

### Making Threshold Decisions

1. **Review historical data**: If you've run similar research, use baseline
2. **Benchmark against standards**: What do published studies achieve? (e.g., 80% task completion is typical for usability studies)
3. **Consider cost of failure**: Critical safety features need 95%+; nice-to-have features can be 70%+
4. **Build in buffer**: If you truly need 80%, set threshold at 75% to allow for measurement noise
5. **Distinguish must-have from nice-to-have**: Must-haves have strict thresholds; nice-to-haves can be more lenient

---

## Confidence Levels: Sample Size and Consistency

### Sample Size Requirements by Confidence Tier

| Confidence | Sample Size (n) | Interpretation | Use Cases |
|---|---|---|---|
| **High** | n ≥ 5 | Robust signal; results are reliable | Go/No-Go decisions on must-haves |
| **Medium** | n = 3–4 | Adequate signal; results are plausible | Decisions on nice-to-haves; plan follow-up |
| **Low** | n < 3 | Insufficient data; results are uncertain | Exploratory findings only; must collect more |

**Note**: A "session" is one complete observation (e.g., one user completing a task, one code review, one team meeting).

### Consistency Factors

**High Consistency** (low variance): All scores cluster within 10% of the mean
- Example: Scores are 78%, 79%, 80%, 82%, 81% → mean 80%, narrow range → High consistency

**Medium Consistency**: Scores vary 10–30% around the mean
- Example: Scores are 70%, 75%, 85%, 80%, 65% → mean 75%, moderate spread → Medium consistency

**Low Consistency** (high variance): Scores scatter >30% around the mean
- Example: Scores are 40%, 85%, 55%, 90%, 50% → mean 64%, wide spread → Low consistency

**High variance is a red flag**: It suggests measurement unreliability or contextual factors affecting results. Investigate before calling a criterion "Pass."

### Data Quality Factors

**High Quality**:
- Objective metric (e.g., code coverage %, task completion yes/no)
- Measurement is automated or standardized
- Clear, unambiguous scoring
- No missing data points

**Medium Quality**:
- Mostly objective with minor interpretation (e.g., code clarity rubric with clear definitions)
- Manual measurement with documented procedure
- 1–2 data points missing (noted)
- Minor measurement ambiguity

**Low Quality**:
- Subjective assessment (e.g., "overall quality," "vague impression")
- Measurement inconsistency across sessions
- Multiple data points missing
- Conflicting evidence or high measurement error

---

## Root-Cause Analysis Framework

When a criterion fails, dig into **why**. Use this framework:

### Step 1: Identify the Gap
- **What was measured?** (the metric)
- **What was the threshold?** (the requirement)
- **What was the result?** (the outcome)
- **By how much did it miss?** (gap size: critical if -50%, moderate if -10%)

### Step 2: Classify the Cause

| Cause Type | Definition | Examples |
|---|---|---|
| **Design flaw** | The criterion itself is misaligned with objectives | Measuring speed when effectiveness matters more |
| **Implementation issue** | The process/system doesn't support the criterion | Instructions unclear, tools missing, skill gaps |
| **Measurement problem** | The measurement itself is unreliable | Rubric is ambiguous, scorer is inconsistent |
| **External factor** | Out-of-scope conditions affected the result | Participant was fatigued, network was down, weather delayed testing |

### Step 3: Assess Fixability

- **Fixable**: Issue can be resolved before next session (e.g., clarify instructions)
- **Partially fixable**: Issue can be mitigated but not fully solved (e.g., complex skill takes 2 more sessions to develop)
- **Unfixable**: Issue reflects fundamental constraint (e.g., participant has physical limitation, requirement is impossible)

### Step 4: Plan Action

- **Fixable**: "In S3, revise instructions based on S1–S2 feedback; expect pass rate to jump to 85%"
- **Partially fixable**: "Expected improvement of 10–15% per session; will reach threshold by S5"
- **Unfixable**: "This criterion cannot be met; recommend removing or redefining"

---

## Must-Have vs. Nice-to-Have: Distinction and Thresholds

### Must-Have Criteria

**Definition**: Critical to success. Failing to meet these means the research has missed its core objective.

**Characteristics**:
- Directly tied to the research question or primary objective
- Failure has significant consequences
- Usually 2–5 per research initiative

**Threshold Setting**:
- More conservative (e.g., 80–85% for pass rate)
- Require **High confidence** to call "Pass"
- Example: "If task completion is <70%, the design is fundamentally broken"

**Go/No-Go Impact**:
- If all must-haves pass (High confidence): Likely **Go**
- If any must-have fails: **Caution** or **No-Go** (depending on cause and fixability)

### Nice-to-Have Criteria

**Definition**: Desirable to achieve but not essential. Missing these is acceptable; can improve in iteration.

**Characteristics**:
- Secondary objectives or enhancement goals
- Failure is a missed opportunity but doesn't undermine core value
- Usually 3–8 per research initiative

**Threshold Setting**:
- More lenient (e.g., 60–75% for pass rate)
- Can accept **Medium confidence** to call "Pass"
- Example: "If polish score is 6/10 instead of 8/10, we can refine later"

**Go/No-Go Impact**:
- If 50%+ of nice-to-haves pass: Doesn't affect Go decision
- If <50% of nice-to-haves pass: Flag as improvement opportunity but not blocker

---

## Go/No-Go Decision Framework

Use this logic to synthesize your tracking matrix into a recommendation:

### GO: Proceed Confidently
**Conditions** (all must be true):
1. All must-have criteria pass
2. Pass rate on must-haves ≥80% at High confidence
3. Positive or stable trend (not declining)
4. At least 50% of nice-to-haves pass
5. Root causes for any failures are understood and fixable

**Recommendation**: "Proceed to next phase. Core objectives met. Plan to address nice-to-have gaps in iteration."

### CAUTION: Proceed with Conditions
**Conditions** (at least one is true):
1. All must-haves pass but at Medium confidence (n=3–4 sessions)
2. 80%+ of must-haves pass at High confidence, but 1 is borderline
3. Must-have criterion shows declining trend (but hasn't failed yet)
4. <50% of nice-to-haves pass, indicating scope misalignment
5. Root causes for failures are partially addressable

**Recommendation**: "Proceed but mitigate risk. Collect 2 more sessions on high-risk must-haves. Plan remediation for failing criteria in next iteration."

### NO-GO: Stop and Pivot
**Conditions** (at least one is true):
1. Any must-have criterion fails at High confidence
2. 2+ must-haves pass at Low confidence (n<3)
3. Must-have criterion shows strong declining trend
4. Root cause is unfixable (fundamental design flaw, impossible requirement)
5. Measurement is unreliable (confidence too low to even diagnose issue)

**Recommendation**: "Do not proceed. Core objective is at risk. Options: (a) redesign and retest, (b) redefine criterion, (c) cancel initiative."

---

## Edge Cases and Special Situations

### Conditional Criteria

**Definition**: A criterion only applies if a prior condition is met.

**Example**: "If the user has programming experience, code clarity (C1) applies. If no experience, explanation clarity (C2) applies."

**How to Handle**:
1. Track which sessions meet the condition
2. Score only applicable sessions (e.g., C1 scored in 3 of 5 sessions)
3. Report as: "C1: 3/3 sessions pass (applies to experienced users only)"
4. In go/no-go decision, weight by applicability

### Role-Specific Criteria

**Definition**: Different stakeholders have different success criteria.

**Example**:
- Developer success: Code quality, performance
- End-user success: Task completion, satisfaction
- Manager success: Timeline met, budget on target

**How to Handle**:
1. Track criteria separately by role
2. Create separate tracking matrices for each role
3. In go/no-go, note which roles pass/fail
4. Example: "Go for end-users (95% satisfaction), Caution for developers (code quality 6/10)"

### Partial Pass Scenarios

**Definition**: A criterion is neither fully passing nor fully failing (e.g., 50% pass rate, borderline score).

**How to Handle**:
1. Use status "Partial" explicitly
2. In tracking matrix: "Partial | Medium confidence | needs 1 more session"
3. Root cause: Why is it stuck in middle? Fixable?
4. Decision impact: Treat as Caution unless root cause is understood and fixable

### Missing Data

**Definition**: A session couldn't be measured for a criterion (e.g., participant dropped out, metric wasn't logged).

**How to Handle**:
1. Mark as "Insufficient data" (not as Fail)
2. Reduce sample size: If n=5 total but 1 is missing, n=4 for confidence calculation
3. Plan to remeasure in next session
4. If multiple criteria are missing: Confidence drops to Low for any calculations

### Outliers and Anomalies

**Definition**: One session's score is dramatically different from others (e.g., 85%, 88%, 12%, 86%, 87%).

**How to Handle**:
1. Investigate the outlier: Was it a measurement error, external factor, or real variation?
2. If **measurement error** (e.g., wrong scorer used): Exclude and remeasure
3. If **external factor** (e.g., participant was sick): Note and consider excluding with justification
4. If **real variation** (e.g., task varies in difficulty): Keep and note in tracking matrix
5. Recalculate consistency and confidence if excluding data
6. Always document why outliers were included or excluded

---

## Quick Reference: Decision Checklist

Before calling a criterion "Pass":
- [ ] Threshold is clear and justified
- [ ] Sample size ≥3 (ideally ≥5)
- [ ] Consistency is acceptable (variance <30% for High, <50% for Medium)
- [ ] Measurement procedure was consistent across sessions
- [ ] Any missing data is documented
- [ ] Outliers are explained

Before recommending Go:
- [ ] All must-haves pass at High confidence
- [ ] Trends are stable or improving (not declining)
- [ ] Root causes for any Caution items are understood
- [ ] At least 50% of nice-to-haves pass
- [ ] Next steps are clear if issues remain
