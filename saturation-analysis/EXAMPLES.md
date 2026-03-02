# Saturation Analysis Examples

## Example 1: Complete 8-Session Saturation Analysis Report

### Study Overview
**Dataset**: Mobile Productivity App User Research
**Total Sessions**: 8
**Study Period**: January 15 – February 3, 2024
**Participant Roles**: Users (non-technical), Developers, Product Managers
**Analysis Date**: February 5, 2024

---

### Theme Tracking Table

| Session | Date | Role | Themes Identified | New Themes | Cumulative Unique | Notes |
|---------|------|------|-------------------|------------|-------------------|-------|
| 1 | 1/15 | User (non-tech) | Task Management, Notification Overload | 2 | 2 | Introductory session; diverse feedback |
| 2 | 1/16 | Developer | API Performance, Offline Mode, Data Sync | 3 | 5 | Dev concerns differ from users |
| 3 | 1/18 | User (non-tech) | Task Management, Mobile-First Preference, Collaboration Gaps | 1 | 6 | Mobile-first is new; Task Management confirmed |
| 4 | 1/20 | Product Manager | Market Positioning, Competitor Parity, Enterprise Features | 3 | 9 | PM introduces business/strategy angle |
| 5 | 1/23 | Developer | API Performance, Data Sync, Documentation Gaps, Plugin Ecosystem | 1 | 10 | Documentation Gaps is new; others confirmed |
| 6 | 2/1 | User (non-tech) | Task Management, Notification Overload, Collaboration Gaps, Accessibility | 1 | 11 | Accessibility concern identified |
| 7 | 2/2 | Product Manager | Market Positioning, Competitor Parity, Enterprise Features, Integration Requests | 1 | 12 | Integration Requests is new; others repeated |
| 8 | 2/3 | Developer | API Performance, Data Sync, Offline Mode, Documentation Gaps | 0 | 12 | No new themes; confirms prior findings |

---

### Saturation Metrics

**Cumulative Data**:
- Total unique themes identified: 12
- Average new themes per session: 1.5
- Sessions since last new theme: 1 (Session 8 had no new themes)
- 3-session rolling average (Sessions 6–8): (1 + 1 + 0) / 3 = 0.67 new themes per session
- Overall emergence rate: 11 new themes / 8 sessions = **1.375 new themes per session (17.2% per session)**
- Themes by role:
  - Users: 4 unique themes (Task Management, Notification Overload, Mobile-First Preference, Collaboration Gaps, Accessibility)
  - Developers: 5 unique themes (API Performance, Offline Mode, Data Sync, Documentation Gaps, Plugin Ecosystem)
  - Product Managers: 4 unique themes (Market Positioning, Competitor Parity, Enterprise Features, Integration Requests)
- Note: Some themes appear in multiple roles; role-specific list above shows theme author role

**Saturation Percentage (Moderate Threshold)**:
- Observed themes: 12
- Estimated ceiling (heuristic: 12 + 2 estimated undiscovered): 14
- Saturation % = 12 / 14 ≈ **85.7%**

---

### Saturation Curve Narrative

The saturation curve demonstrates a **classic growth-plateau pattern**. Sessions 1–4 show steep ascent (2 → 5 → 6 → 9 new themes cumulatively), indicating diverse stakeholder perspectives and exploratory discovery. Sessions 5–7 show deceleration (slope flattens; new themes drop from 3 per session to 1 per session), reflecting theme stabilization as primary concerns are documented. **Session 8 introduces zero new themes, and the 3-session rolling average (Sessions 6–8) stands at 0.67—below the 1.5-threshold for "continue"**. The curve has entered plateau phase with confidence. The only question is whether one or two additional sessions might uncover minor edge cases or outlier concerns.

---

### Role-Specific Findings

**Users (Non-Technical)**:
- Sessions 1, 3, 6 engaged; total of 3 user sessions
- New theme emergence: Sessions 1 (2), 3 (1), 6 (1)
- Plateau evident by Session 6; Session coverage is thin
- **Status**: Saturation reached for "user perspective" but sample size is small (n=3)

**Developers**:
- Sessions 2, 5, 8 engaged; total of 3 developer sessions
- New theme emergence: Sessions 2 (3), 5 (1), 8 (0)
- New themes declining; plateau evident
- **Status**: Approaching saturation; last session confirmed prior findings

**Product Managers**:
- Sessions 4, 7 engaged; total of 2 PM sessions
- New theme emergence: Sessions 4 (3), 7 (1)
- Insufficient sessions to assess individual saturation
- **Status**: Too few sessions; if continuing, prioritize PM recruitment

**Interpretation**: Users and developers show saturation signals; PMs need 1–2 more sessions for confidence. If user/developer perspectives are priority, conclude. If PM strategy angle is critical, add 1–2 PM sessions.

---

### Confidence Assessment

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Min session threshold (moderate = 8) | ✓ Met | 8 sessions completed |
| Clear plateau in curve | ✓ Yes | Flat phase Sessions 6–8 |
| Low emergence rate (< 1.5 per session) | ✓ Yes | 3-session rolling avg = 0.67 |
| Theme extraction rigor | ~ Moderate | Codebook created; single coder |
| Role-specific saturation | ~ Partial | Users/Devs saturated; PMs underdeveloped |
| Outlier or spike patterns | ✓ None | Steady decline; no anomalies |

**Overall Confidence Level**: **MEDIUM-TO-HIGH**

---

### Recommendation

**CONCLUSION: Saturation Reached (with minor caveat)**

**Rationale**:
1. Minimum sessions met (8 ≥ 8 for moderate threshold)
2. Last session introduced zero new themes
3. 3-session rolling average (0.67) is below 1.5 threshold → minimal novelty
4. Saturation percentage at 85.7% (> 80% threshold)
5. Curve plateau is clear and stable

**Conditions**:
- This conclusion is robust for **user and developer perspectives**, which have reached saturation
- **Product manager perspective** is underdeveloped (only 2 sessions). If PM strategy is core to study, recommend 1–2 additional PM sessions

**Action Items**:
- **PRIMARY**: Data collection can pause; proceed to analysis and synthesis phase
- **OPTIONAL**: If resources allow and PM input is important, recruit 1–2 additional product managers (do not collect more user/developer data unless significant gaps emerge during coding)
- **NEXT STEP**: Begin thematic coding with the 12 themes identified; create codebook for inter-rater reliability check; prepare findings for reporting

---

---

## Example 2: Early Termination Scenario (Homogeneous Sample)

### Quick Summary
**Dataset**: Customer Support Team Process Improvement Study
**Sessions**: 6 completed
**Sample**: All participants from same company's support team (homogeneous background)
**Recommendation**: **SATURATION REACHED (aggressive threshold appropriate)**

### Key Metrics
- New themes per session: [5, 4, 2, 1, 0, 0]
- Cumulative unique themes: 12
- Emergence rate: Sessions 4–6 show 0–1 new themes (plateau evident)
- All 6 participants same role, company, experience level

### Rationale for Early Conclusion
In **homogeneous samples**, saturation typically arrives by session 6–8 because viewpoint diversity is limited. Continuing beyond clear plateau (Sessions 5–6 show zero new themes) incurs diminishing returns. **Confidence is HIGH** for understanding this team's perspective, though findings are not generalizable.

**Recommendation**: Stop data collection. Proceed to analysis.

---

## Example 3: Continue Scenario (Heterogeneous Sample)

### Quick Summary
**Dataset**: Global Workplace Flexibility Study
**Sessions**: 10 completed
**Sample**: Diverse geographic regions, industries, income levels, role types
**Recommendation**: **CONTINUE DATA COLLECTION**

### Key Metrics
- New themes per session: [4, 3, 3, 2, 2, 1, 2, 2, 1, 1]
- Cumulative unique themes: 21
- Emergence rate: 10% still evident in final sessions
- High heterogeneity in sample (age range 22–68, 6 countries, 8 industries)

### Rationale for Continuation
**Emergence rate remains > 10%** in recent sessions. The sample's diversity continues to generate novel insights. Curve shows gentle slope, not plateau. While 10 sessions is substantial, for heterogeneous international study, 12–15 sessions is standard practice.

**Recommendation**: Continue to 12–15 sessions. Budget allows; emerging findings suggest rich variation still to explore.

---

## Example 4: Late Outlier Scenario (Decision Tree)

### Quick Summary
**Dataset**: Remote Work Adoption Study
**Sessions**: 10 completed
**Pattern**: Sessions 1–8 plateau (0–1 new themes per session), then Session 9 introduces 2 new themes

### New Themes in Session 9
- "Time Zone Collaboration Challenges"
- "Caregiver Responsibility Conflicts"

### Decision Tree

**Q1: Is Session 9 participant from different role/demographic than prior 8?**
- **Yes** (new to rural region, prior sessions were urban) → These are genuine new themes; role-specific saturation not yet reached. Keep new themes; continue recruitment for rural demographic.
- **No** (same profile as prior) → Proceed to Q2

**Q2: Could these themes have been mentioned in prior sessions but missed during coding?**
- **Yes** (review reveals "scheduling conflicts" was mentioned as variant) → Recode; merge with existing theme; discard "new" label
- **No** (themes genuinely absent from prior discussions) → Proceed to Q3

**Q3: How prevalent/important is this theme in Session 9 discussion?**
- **Central to discussion** (mentioned multiple times, unprompted) → Count as new theme; continue data collection
- **Peripheral mention** (brief comment, response to direct question) → Count as new theme but note low prevalence; consider saturation likely if next 2 sessions do not confirm
- **Single mention, unclear importance** → Count as new theme but flag as low-confidence; treat Session 10–11 as confirmation round

### Example Outcome
If Session 9 introduced genuine, central themes from a new demographic, the study is **NOT saturated yet**. Recommendation: **CONTINUE** targeting this demographic to understand how their experience differs. This is not an error; it's discovery.

---

## Example 5: Mixed Results (Role-Based Recommendation)

### Quick Summary
**Dataset**: Enterprise Software Usability Study
**Sessions**: 10
**Participants**: 4 executives, 3 end-users, 3 IT administrators

| Role | Sessions | New Themes by Session | Status |
|------|----------|----------------------|--------|
| Executives | 4 | [3, 2, 0, 0] → Total 5 | **Saturated** |
| End-Users | 3 | [4, 2, 1] → Total 7 | **Near saturation** |
| IT Admins | 3 | [3, 2, 1] → Total 6 | **Near saturation** |

### Analysis
- Executives reached saturation early (likely due to narrower scope: business impact, ROI, compliance)
- End-users and IT admins still showing 1–2 new themes per session; continued growth expected
- If all three roles are equally critical to study → continue recruitment to 12–15 sessions focusing on end-users and IT admins
- If executive perspective is sufficient → can reduce executive recruitment, continue other roles

### Recommendation
**CONTINUE, BUT TARGETED**. Do not recruit more executives; recruit 2–3 additional end-users and IT admins. Estimated completion: 2–3 more weeks. Re-assess after 4 additional sessions (likely 2 end-user, 2 IT admin).

---
