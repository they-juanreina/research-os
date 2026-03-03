# Saturation Analysis Reference Guide

## Theme Definition & Distinction

### What Counts as a New Theme
A **new theme** is a conceptually distinct finding, insight, or pattern not previously identified in prior sessions. Criteria:
- Introduces a novel problem, idea, or observation
- Addresses a dimension not covered by existing themes
- Represents a distinct stakeholder concern or mental model
- Cannot be logically subsumed under an existing theme

**Example**: "Users need offline functionality" is new if no prior session mentioned offline capability. Even if someone previously said "we work in remote areas," that's a connectivity issue, not functionality offline.

### What Counts as a Variant (Not New)
A **variant** reframes, deepens, or specifies an existing theme without changing its core concept. Examples:
- Same theme, different context: "Dark mode for low light" vs. "Dark mode preference"—both are appearance/customization
- Different phrase, same concept: "Difficult onboarding" vs. "Steep learning curve"—both concern initial user friction
- Elaboration of existing theme: "Dark mode helps eyes" expands on accessibility, not a new theme if accessibility already identified

**Decision rule**: If the core insight could be filed under an existing theme's label with minimal confusion, it's a variant.

### What Counts as Confirmation (Not New)
A **confirmation** is when a prior theme is reiterated without new dimension or evidence type. Examples:
- Session 2: "Users want dark mode"
- Session 5: "Participants also prefer dark mode"
→ If the underlying insight is identical, this is confirmation, not a new theme.

Record it as theme recurrence frequency, useful for strength/prevalence analysis, but do not count toward saturation emergence.

---

## Saturation Curve Interpretation

### Early Spike Phase (Sessions 1–3)
- **Pattern**: Steep climb in cumulative unique themes
- **Typical emergence rate**: 4–7 new themes per session
- **Meaning**: Participants are introducing diverse perspectives; the study is broad and exploratory
- **Action**: Continue—this is normal and expected

### Growth Phase (Sessions 4–8)
- **Pattern**: Moderating climb; curve slope flattens but still rising
- **Typical emergence rate**: 1–3 new themes per session
- **Meaning**: Core themes are stabilizing; new additions are nuanced or edge cases
- **Action**: Continue; saturation is approaching but not yet

### Plateau Phase (Sessions 9+)
- **Pattern**: Nearly flat curve; long stretches with minimal or zero new themes
- **Typical emergence rate**: 0–0.5 new themes per session
- **Meaning**: Most primary themes are identified; additional sessions confirm rather than extend
- **Action**: Consider concluding; assess confidence in coverage

### Flat with Spikes
- **Pattern**: Mostly flat, but occasional jump (e.g., new theme in Session 10)
- **Meaning**: Saturation is near but not absolute; rare outlier or previously missed angle
- **Action**: Decide if outlier is: (a) genuine discovery → continue; (b) researcher error → discard; (c) minor edge case → count but conclude

---

## Role-Specific vs. Global Saturation

### When to Assess by Role
Assess separately when:
- **Participant roles differ meaningfully** (e.g., users vs. developers, managers vs. staff)
- **Roles likely have different mental models** or priorities
- **Sample sizes per role are substantial** (n ≥ 3 per role recommended)

### Example: Three-Role Study (Users, Developers, Managers)
| Session | User Themes | Dev Themes | Manager Themes |
|---------|-------------|-----------|-----------------|
| 1–4     | Rapid growth | Rapid growth | Rapid growth |
| 5–7     | Plateauing (1 new/session) | Still growing (2 new/session) | Plateauing (0 new/session) |
| 8–10    | Flat | Growth slowing | Flat |

**Interpretation**: Developers are generating new insights longer than users/managers. Global saturation may not be reached even if user/manager saturation is evident.

**Decision**:
- If all roles must be equally represented: continue sampling developers
- If user/manager insights are priority: could pause for those roles but continue developer recruitment

### Role-Specific Thresholds
For multi-role studies, recommend:
- **Minimum 3 sessions per role** before assessing saturation individually
- **Each role must meet saturation criteria independently** if representation is critical
- **Weight by research priority** (if developers are focus, reach full saturation for them; lighter for others)

---

## Edge Cases & Special Situations

### Outlier Sessions (Introducing New Themes Late)
**Scenario**: Session 10 introduces 3 novel themes after sessions 7–9 were flat.

**Possible explanations**:
1. **Genuine discovery**: Previously unsampled stakeholder type or lived experience
2. **Researcher drift**: Themes were mentioned earlier but not coded consistently
3. **Data quality issue**: Shallow or off-topic discussion reframed as themes

**Resolution**:
- Review session notes for context (participant type, discussion quality)
- If outlier is from new role/demographic → count it; saturation is role-specific
- If outlier duplicates or slightly renames prior themes → recode and discard
- If outlier is genuine but narrow → count it but note low prevalence

### Homogeneous Samples
**Scenario**: All participants share similar backgrounds, roles, or perspectives.

**Effect**: Saturation reached faster (typically 6–8 sessions) because diversity of viewpoints is limited.

**Implication**:
- Don't require 12 sessions if saturation is evident by session 8 in homogeneous sample
- Confidence in findings is high *within that population*
- Generalizability may be limited (homogeneity is a limitation)

### Small Populations
**Scenario**: Study recruiting from population of ~20 people total.

**Consideration**:
- Once > 50% of population is sampled, diminishing returns accelerate
- Saturation may be reached not by absolute theme count but by "nearly all variants from available population exhausted"
- Recommend quota sampling: aim for ≥ 6–8 sessions *or* > 30% of population, whichever is larger

### High-Variability Samples (Heterogeneous Perspectives)
**Scenario**: Participants are diverse (age, background, expertise, beliefs) and hold divergent views.

**Effect**: New themes may emerge longer (12–18 sessions) because heterogeneity sustains novelty.

**Decision**:
- Increase minimum session threshold to 12 before concluding saturation
- Continue if emergence rate is still > 10% per session
- Consider coding themes by "stance" or "perspective type" to track subsaturation

---

## Minimum Session Requirements by Role

### General Guidance
| Scenario | Min Sessions | Rationale |
|----------|--------------|-----------|
| Homogeneous, single role | 6 | Rapid stabilization expected |
| Mixed roles (2 types), balanced | 8–10 | Need coverage for both |
| Mixed roles (3+ types), balanced | 12 | More complexity requires more sessions |
| High heterogeneity | 12–15 | Diverse perspectives sustain novelty longer |
| Small population (< 30 total) | 6–8 or 30% of population (whichever greater) | Census-like approach limits saturation mathematically |

### Per-Role Breakdown
- **Primary role** (main focus): Reach full saturation threshold before conclusion
- **Secondary role** (supplementary): Can conclude at moderate threshold if emergence has stalled
- **Tertiary role** (check for outliers): Minimum 3 sessions; continue if showing growth

---

## Confidence Levels (High / Medium / Low)

### High Confidence
- ✓ Minimum session threshold exceeded (12 for conservative, 8 for moderate, 6 for aggressive)
- ✓ Theme extraction was rigorous (coding scheme pre-defined, dual-coded sample, inter-rater reliability documented)
- ✓ Saturation curve shows clear plateau with ≥ 4 sessions in plateau phase
- ✓ Emergence rate < 5% per session in final 3 sessions
- ✓ If multi-role study: all roles meet saturation independently
- ✓ No outlier sessions that introduce new themes late

**Conclusion**: "Saturation has been reached with high confidence."

### Medium Confidence
- ✓ Minimum session threshold met (8 sessions for moderate threshold)
- ✓ Theme extraction was documented but not rigorously inter-coded
- ✓ Saturation curve shows plateau but only 2–3 sessions in plateau phase
- ✓ Emergence rate 5–10% per session in final 3 sessions
- ✓ Most roles show saturation; 1 secondary role still growing slightly
- ✓ One potential outlier session but explained by shift in recruitment

**Conclusion**: "Saturation likely reached; consider 1–2 additional sessions for confirmation."

### Low Confidence
- ✗ Minimum session threshold not yet met (< 6 sessions)
- ✗ Theme extraction was ad-hoc or inconsistently applied
- ✗ Saturation curve is volatile or shows recent upward trend
- ✗ Emergence rate > 15% per session in recent sessions
- ✗ Multiple outlier sessions or unexplained spikes
- ✗ Unequal role representation; one role has very few sessions

**Conclusion**: "Insufficient evidence of saturation. Continue collecting data."

---

## Practical Interpretation: Three Scenarios

### Scenario A: Clear Plateau (High Confidence)
- Sessions 1–5: 5, 4, 3, 2, 1 new themes
- Sessions 6–10: 0, 0, 1, 0, 0 new themes
- Cumulative: 20 unique themes
- Curve: Steep rise, then flat for 5 sessions
- **Recommendation**: Conclude. High confidence saturation reached.

### Scenario B: Slow Growth (Medium Confidence)
- Sessions 1–5: 3, 2, 2, 2, 1 new themes
- Sessions 6–8: 1, 1, 0 new themes
- Cumulative: 12 unique themes
- Curve: Moderate climb, slight flattening in final 3 sessions
- **Recommendation**: Consider pausing; 1–2 more sessions recommended for confirmation.

### Scenario C: Continued Novelty (Continue)
- Sessions 1–8: 4, 3, 3, 2, 2, 2, 1, 2 new themes
- Sessions 9–10: 1, 2 new themes
- Cumulative: 22 unique themes
- Curve: Slope still noticeable; no clear plateau yet
- **Recommendation**: Continue. Emergence rate still meaningful; saturation not yet reached.

---

## Coding & Documentation Standards

### Theme Definition Document
Before saturation analysis, create a **theme codebook**:
- Theme name (short label)
- Definition (1–2 sentences)
- Inclusion criteria (what counts as this theme)
- Examples from sessions
- Exclusion criteria (what does NOT count)

**Example**:
- **Theme**: User Onboarding Friction
- **Definition**: Participants describe difficulty or frustration during initial learning or setup
- **Inclusion**: Time-to-competence complaints, confusion about features, steep learning curve
- **Exclusion**: Feature requests, preference for different design, performance complaints
- **Example**: "It took me an hour to figure out how to create a project"

### Session Notes Template
For each session, record:
1. Session number and date
2. Participant role/demographic
3. Themes identified (linked to codebook)
4. Which themes are new (not in prior sessions)
5. Session duration and depth (full/partial/rushed)
6. Any anomalies (off-topic, distracted participant, etc.)

### Tracking Table Format
```
Session | Date | Role | Themes Identified | New Themes | Cumulative Unique | Notes
1       | 1/15 | User | Onboarding, Dark Mode, Export | 2 | 2 | —
2       | 1/16 | Dev  | Dark Mode, API Limits, Offline | 2 | 4 | First mention of API constraints
3       | 1/17 | User | Onboarding, Mobile, Collaboration | 2 | 6 | Mobile use-case new
...
```

---

## When to Deviate from Standard Thresholds

**Acceptable reasons to conclude earlier than threshold**:
- Extremely homogeneous sample (e.g., all same role, organization, background)
- Saturation curve is unambiguous (flat for many sessions)
- Resource constraints are documented as study limitation
- Research question is narrow and exploratory (not comprehensive understanding)

**Acceptable reasons to continue past threshold**:
- High heterogeneity in sample
- Emergence rate remains > 15% per session
- New role or demographic becomes available mid-study
- Preliminary analysis reveals important gaps (e.g., negative cases underrepresented)
- Research question requires comprehensive understanding
