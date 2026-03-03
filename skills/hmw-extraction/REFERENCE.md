# HMW Extraction Reference

## The HMW Formula Breakdown

A well-formed HMW statement has four interdependent components:

### [ACTION]
The operative verb that frames what we're trying to enable. Common verbs:
- **help** — Support users in accomplishing a task
- **allow** — Remove barriers or constraints
- **enable** — Make something newly possible
- **empower** — Give users agency or confidence
- **teach** — Build user knowledge or capability
- **encourage** — Motivate behavior change
- **protect** — Safeguard against negative outcomes

**Avoid:** Prescriptive verbs like "build," "design," "create," "make" (these are solutions, not opportunities).

### [USER]
A specific user role or persona, not a generic audience. Compare:

**Too broad:** "How might we help users..."

**Specific:** "How might we help junior developers joining enterprise teams to..."

Specificity unlocks persona-appropriate solutions. Name the role, context, or constraint:
- "Remote-first managers"
- "Parents managing multiple school calendars"
- "Compliance officers auditing vendor access"

### [BENEFIT]
The outcome or goal from the user's perspective. Connect to the research finding:
- Save time on repetitive tasks
- Reduce cognitive load from context switching
- Increase confidence in decision-making
- Enable collaboration across silos
- Reduce anxiety about edge cases

Link benefits to observed pain or friction. If your research showed "users re-verify data three times," the benefit is "verify once."

### [CONTEXT] (Optional)
Constraints, scenarios, or conditions that bound the opportunity:
- "in distributed teams across time zones"
- "for organizations without IT infrastructure"
- "when collaborating with external partners"
- "on first-time use"
- "under time pressure"

Context prevents HMW statements from becoming too abstract. It grounds them in real conditions.

---

## Common Anti-Patterns

### ❌ Too Narrow (Pre-Solves the Problem)
**Bad:** "How might we add a color-coded tag system so users can organize tasks?"

**Why:** You've already decided the solution. Designers lose autonomy.

**Good:** "How might we help project managers quickly identify and organize tasks by urgency and ownership?"

### ❌ Too Broad (Unscopeable)
**Bad:** "How might we improve the user experience?"

**Why:** No clear target or metric. Impossible to ideate or validate.

**Good:** "How might we help first-time users understand what data is required before they hit a validation error?"

### ❌ Solution-Biased (Not a Reframe)
**Bad:** "How might we redesign the dashboard to show real-time alerts?"

**Why:** "Redesign the dashboard" is a solution direction, not an opportunity.

**Good:** "How might we help operations teams notice critical issues before they escalate?"

### ❌ Vague User Definition
**Bad:** "How might we help people save time?"

**Why:** Everyone wants to save time. Which users? Doing what?

**Good:** "How might we help data analysts spend less time validating data sources and more time exploring patterns?"

### ❌ Missing Evidence
**Bad:** HMW statements with no research backing.

**Why:** Teams will challenge feasibility and relevance without grounding.

**Good:** Always cite the research finding or user quote that surfaced the pain point.

---

## Clustering Methodology

Group HMW statements by theme to reveal patterns and interdependencies.

### Common Clustering Approaches

**By Problem Domain:**
- Navigation & Findability
- Trust & Security
- Data Quality & Validation
- Collaboration & Communication
- Onboarding & Learning

**By User Role:**
- Administrators
- Analysts
- Developers
- End users

**By Pain Frequency:**
- Daily friction
- Weekly/monthly tasks
- One-time setup

**By Effort Level:**
- Quick wins (small teams, fast iteration)
- Medium bets (cross-team, 1-2 sprints)
- Strategic investments (org-wide, multi-quarter)

### Benefits of Clustering
1. **Reveals systemic issues:** Multiple HMW statements in one cluster may indicate a deeper need.
2. **Enables parallel work:** Teams can own a cluster and move through ideation together.
3. **Supports sequencing:** Some clusters may be prerequisites for others (onboarding before advanced features).
4. **Highlights trade-offs:** Solving for one cluster sometimes creates constraints in another.

---

## Prioritization Matrix

Use a two-axis or three-axis matrix to guide resource allocation.

### Planning Matrix (Impact × Feasibility)

Use this *after* priority scoring to decide how to phase and sequence work. Priority (Impact × Urgency) tells you *what matters most*; this matrix tells you *how to approach it* given your team's current capacity.

```
         High Feasibility
              |
     QUICK WINS | STRATEGIC
              |
Low Impact    +------------ High Impact
              |
     FILL-INS | MOONSHOTS
              |
         Low Feasibility
```

**Quick Wins:** High impact, high feasibility. Act now.

**Strategic:** High impact, lower feasibility. These are your most important design challenges. Start scoping, de-risking, and breaking into phases rather than deferring.

**Fill-Ins:** Lower impact, high feasibility. Good for team momentum when capacity allows.

**Moonshots:** High impact, very low feasibility. Keep visible — do not discard. Constraints change. A Moonshot today may become Strategic next quarter.

### Priority Score Formula

**Priority = Impact × Urgency**

Score ≥ 15: High · 8–14: Medium · < 8: Low

**Feasibility is a separate planning column, not part of the priority score.** The previous formula `(Impact × Urgency) / Feasibility` placed feasibility in the denominator, which had two problems: (1) it deprioritized high-impact, hard-to-solve opportunities — exactly the opportunities that most need strategic attention; (2) it produced scores inconsistent with the stated tiers (a HMW with Impact=5, Urgency=5, Feasibility=4 scored 6.25 — which fell into "Low" by the threshold, not "High"). Feasibility is a planning input that determines *when* and *how* you address an opportunity, not *whether* it matters.

**Impact (1–5):** How many users are affected, and how severe is the friction?
- 5: Affects all or most primary users; severe blocker
- 4: Affects most users; significant friction
- 3: Affects some users; moderate friction
- 2: Affects few users; minor inconvenience
- 1: Edge case or aspirational

**Urgency (1–5):** How often do users encounter this? How critical is timing?
- 5: Daily or constant; business-critical
- 4: Multiple times per week; high frequency
- 3: Weekly; recurring but manageable
- 2: Monthly; occasional
- 1: Rare or one-time

**Feasibility (1–5, planning column):** Can the team realistically solve this now?
- 5: Clear solution path; within team expertise; minimal dependencies
- 4: Solution is defined; requires some new learning
- 3: Solution concept exists; requires exploration; some dependencies
- 2: Solution is unclear; requires research; significant dependencies
- 1: Currently infeasible; blocking constraints; unclear how to approach

**Example Calculations:**

| HMW | Impact | Urgency | Score | Tier | Feasibility (planning) | Quadrant |
|-----|--------|---------|-------|------|------------------------|----------|
| HMW-01 | 5 | 5 | 25 | High | 4 (High) | Strategic — act now |
| HMW-02 | 4 | 4 | 16 | High | 3 (Medium) | Strategic — plan carefully |
| HMW-03 | 3 | 2 | 6 | Low | 5 (High) | Fill-in — quick win available if time permits |
| HMW-04 | 5 | 3 | 15 | High | 2 (Low) | Moonshot — high priority; start scoping and de-risking |

---

## Creating Persona-Specific Variants

One pain point may affect multiple personas differently. Create persona-specific HMW variants to unlock tailored solutions.

### Example: "Users struggle to approve vendor access"

**Variant 1 (Security Admin):**
"How might we help security administrators audit vendor access requests without losing context about which systems are affected?"

**Variant 2 (Department Manager):**
"How might we help department managers approve vendor access quickly while staying informed about compliance requirements?"

**Variant 3 (Compliance Officer):**
"How might we help compliance officers enforce access policies while enabling teams to move quickly?"

**Benefits:**
- Solutions can be persona-specific (UI, workflows, information architecture)
- Teams own different personas and move in parallel
- Ideation uncovers edge cases and interdependencies
- Validation focuses on actual user goals, not one-size-fits-all

---

## Scope Validation: The "3-5 Approaches" Test

**Every HMW statement should inspire 3-5 fundamentally different design approaches.**

### Test Process

1. **Read your HMW statement aloud.**
2. **Ask: "What are three completely different ways to address this?"**
3. **If you can name them, the HMW is well-scoped.**
4. **If you get stuck at one or two, revise.**

### Example: Well-Scoped HMW

**"How might we help analysts verify data quality without re-running full validation every time?"**

**Three distinct approaches:**
1. **Incremental validation:** Show which specific rows/fields changed since last validation.
2. **Sampling-based:** Validate a smart sample instead of 100%; show confidence levels.
3. **Assertion framework:** Let analysts define rules; system alerts when rules break.
4. **Historical comparison:** Surface deviations from historical patterns.
5. **Peer review:** Enable analysts to quickly validate each other's data.

✓ **This HMW is well-scoped.** It can go to ideation.

### Example: Over-Scoped (Too Narrow) HMW

**"How might we help analysts add checkpoints to their validation pipeline?"**

**Realistic approaches:**
1. Add a "checkpoint" button and UI?

✗ **Stuck.** You've already decided the solution. Revise to: "How might we help analysts incrementally validate their work and catch errors before finalizing?" This opens to checkpoints, assertions, sampling, or peer review.

---

## Evidence Linking

Always document the research source for each HMW statement.

### Evidence Types

**Direct Quotes:** User's own words
- "I keep a spreadsheet to track what I've already validated"
- "I never trust the first export"

**Observation:** What you saw in interviews or usability testing
- Participant manually re-checked data in three different systems
- Users navigated back and forth between tools instead of using linked workflows

**Metrics:** Quantified pain
- 60% of users reported data validation as their top friction point
- Average time spent on validation: 4 hours per week

**Behavioral Pattern:** Recurring behavior across multiple users
- All 8 interviewed analysts created custom validation checklists

### Documentation Template

| HMW_ID | HMW Statement | Evidence Type | Evidence | Source |
|--------|---------------|---------------|----------|--------|
| HMW-01 | ... | Direct Quote | "I manually check..." | Interview P5, 2026-01-15 |
| HMW-02 | ... | Observation | Saw user switch tools 12 times... | Usability Test 3, 2026-01-10 |
| HMW-03 | ... | Metrics | 70% of users reported... | Survey (n=42), 2026-01-08 |

---

## Quality Checklist

Before finalizing HMW extraction, validate:

- [ ] **Human-centered:** Focuses on user needs, not technical implementation?
- [ ] **Reframeable:** Uses "How might we...?" not a prescriptive statement?
- [ ] **Specific user:** Names a persona or role, not "users"?
- [ ] **Clear benefit:** Outcome is obvious and user-centric?
- [ ] **Well-bounded:** Not too broad ("improve UX") or too narrow ("add button")?
- [ ] **Evidence-grounded:** Linked to specific research findings?
- [ ] **Scope-testable:** Can inspire 3-5 diverse design approaches?
- [ ] **Actionable:** Teams can move to ideation and prototyping?
- [ ] **No jargon:** Written in plain language, not corporate-speak?
- [ ] **Prioritized:** Scored and ranked relative to other HMW statements?

If all checkmarks are present, the HMW statement is ready for ideation.
