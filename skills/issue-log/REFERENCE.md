# Issue Log Reference

## Severity Level Definitions

### Blocker (Severity 4)
**Definition:** User cannot complete their primary task. Work is completely halted or task is abandoned.

**Characteristics:**
- No workaround exists
- Core workflow is broken
- User must exit the experience or seek alternative solution

**Examples:**
- Form submission button is disabled and shows no error message
- Critical navigation element is missing or unreachable
- Authentication system fails; user locked out
- Data loss occurs (save fails silently, submit doesn't register)
- User's primary role function is unavailable

**Design Fix Direction:** Restore core functionality; ensure clear error messaging and recovery paths.

### Major (Severity 3)
**Definition:** User experiences significant friction. Task completion is possible but delayed, requires workaround, or involves inefficient steps.

**Characteristics:**
- Task completes but with friction
- User must deviate from expected flow
- Significant time/effort overhead added
- User confusion or multiple attempts required

**Examples:**
- Search filters are hidden below the fold; user must scroll to access basic filtering
- Error message appears but is cryptic; user must trial-and-error to fix
- Required information is formatted in confusing way (e.g., price currency not shown)
- User must navigate through unnecessary steps to reach desired feature
- Loading time is excessive but page eventually loads

**Design Fix Direction:** Streamline workflow; improve discoverability; clarify messaging.

### Minor (Severity 2)
**Definition:** User encounters confusion or inefficiency but completes task successfully. Impact is localized.

**Characteristics:**
- Task eventually completes as intended
- User notices friction but can resolve it independently
- No workaround needed
- Confusion resolves quickly

**Examples:**
- Label text is truncated on mobile; user taps to reveal full text
- Button color doesn't clearly indicate state but function is obvious
- Help text is present but buried in tooltip
- Icon is mildly ambiguous but context makes meaning clear
- Spacing makes related items seem disconnected

**Design Fix Direction:** Improve clarity; adjust information hierarchy; refine visual feedback.

### Polish (Severity 1)
**Definition:** UX refinement with no functional impact. Experience works correctly but feels unpolished.

**Characteristics:**
- No user blockers or confusion
- Functional goal is met
- Improvement is cosmetic or delightful
- No measurable impact on task completion

**Examples:**
- Loading spinner lacks animation; feels static but data loads correctly
- Transition timing is abrupt but not disorienting
- Color contrast is acceptable but not optimal
- Whitespace feels cramped but layout is scannable
- Success message could be more celebratory

**Design Fix Direction:** Refine visual design; improve micro-interactions; enhance delight.

---

## ID Scheme

### Format
`[Initial][Number]`

Examples:
- `SM-01` (participant: Sarah Malone)
- `JR-14` (participant: James Rodriguez)
- `AB-03` (participant: Amy Bjorn)

### Generation Rules

1. **Extract Participant Initials** — Use first letter of first name + first letter of last name
2. **Numbering** — Start at 01 for each participant; increment sequentially
3. **Reset Per Cycle** — Reset to 01 if running a new research cycle with same participant
4. **Multi-Session Prefix** — If aggregating issues from multiple sessions with same participant, continue numbering (SM-01 through SM-15)
5. **Cross-Study Prefix** — If combining studies, optionally add study code: `[Study]-[Initial][Number]` (e.g., `H1-SM-01`)

### Auto-Increment Rules
- When appending to an existing log, use the highest existing number + 1
- Maintain separate numbering per participant
- Do not reuse IDs across sessions

---

## Priority Formula

### Calculation

```
Priority = (Frequency × Severity Weight) + Role Impact
```

Score tiers: **High ≥ 8 · Medium 4–7 · Low ≤ 3**

### Why effort is not in the formula

Effort is a **planning input**, not a priority modifier. The previous formula `(Frequency × Severity + RoleImpact) / Effort` placed effort in the denominator, which caused critical high-effort issues (Blockers requiring complex fixes) to score lower than low-effort Minor issues. A Blocker that is hard to fix is not less urgent — it is still blocking a user from completing their task. Effort determines *when* and *how* to address an issue; it does not determine whether the issue matters. Keep Effort as a log column for sprint planning; do not embed it in the priority score.

### Component Definitions

**Frequency** — How many times the issue appeared across sessions
- 1x = 1
- 2x = 2
- 3x+ = 3

**Severity Weight**
- Blocker = 4
- Major = 3
- Minor = 2
- Polish = 1

**Role Impact** — Does this affect the core work of the user's role?
- High (core to primary task) = +2 points
- Medium (supporting task) = +1 point
- Low (secondary/optional task) = +0 points

**Effort** (planning column, not in formula)
- Low (< 0.5 day)
- Medium (0.5–2 days)
- High (> 2 days)

### Blocker Override

Any issue with Severity: Blocker requires immediate team review, regardless of priority score. A user who cannot complete their primary task cannot wait for frequency analysis. Use the priority score to rank Blockers relative to each other and to sequence all other issues — but never use a low priority score to defer a Blocker.

### Example Calculation

Issue: Login fails silently (Blocker)
- Frequency: 2x = 2
- Severity: Blocker = 4
- Role Impact: High (core to using system) = +2

Score = (2 × 4) + 2 = **10 → High** + Blocker Override → immediate review

*Previous formula for comparison*: The old formula with Effort=Medium=2 produced: (2 × 4 + 2) / 2 = **5.0** (Medium). A Blocker seen twice by a core-task user scored Medium. The new formula correctly scores this as High.

### Score Range Reference

| Severity | Frequency | Role Impact | Score | Tier |
|---|---|---|---|---|
| Blocker (4) | 3x | High (+2) | 14 | High + Override |
| Blocker (4) | 2x | High (+2) | 10 | High + Override |
| Blocker (4) | 1x | Low (+0) | 4 | Medium + Override |
| Major (3) | 3x | High (+2) | 11 | High |
| Major (3) | 2x | Medium (+1) | 7 | Medium |
| Major (3) | 1x | Low (+0) | 3 | Low |
| Minor (2) | 3x | High (+2) | 8 | High |
| Minor (2) | 2x | Low (+0) | 4 | Medium |
| Polish (1) | 3x | High (+2) | 5 | Medium |
| Polish (1) | 1x | Low (+0) | 1 | Low |

---

## Issue Description Guidelines

### What to Include
- **Observable behavior** — What did the user actually do and experience?
- **Context** — What task were they attempting?
- **Outcome** — What happened as a result?
- **Time reference** — When in the session did this occur?

### What to Avoid
- **Prescriptive language** — Do not suggest solutions ("button should be larger")
- **Opinions** — Avoid "user was confused" unless accompanied by observable evidence
- **Assumptions** — Do not infer intent; record only what you observed

### Example Format

**Poor:** "The button is too small and user can't find it."
**Better:** "User looked for 'Submit' button in form footer. Button exists at top-right corner but is styled gray on gray background. User scrolled entire page before asking where to proceed."

**Poor:** "Error messaging is bad."
**Better:** "User entered phone number in E.164 format (+1-555-0123). Form rejected with message 'Invalid phone number.' User tried 4 different formats (with/without dashes, parentheses) before succeeding with 10-digit numeric only."

---

## Status Tracking Lifecycle

### Status Values

**Open** — Issue identified; not yet in design pipeline

**In Design** — Issue is actively being addressed; design work or specifications in progress

**In Build** — Issue fix is in development/engineering; code in progress or testing

**Resolved** — Fix is complete, tested, and released; or issue is deemed wont-fix with documented reason

### Transitions

```
Open → In Design → In Build → Resolved
            ↓
         Backlog (optional: deferred, pending resource allocation)
```

### Tracking Notes

- Update status after design review or sprint planning
- Include status change date in "Notes" column: "Status changed to In Design on 2025-02-12"
- Document why an issue is deferred: "Wont-fix: edge case affecting <1% of users; requires data pipeline refactor"
- Link to design ticket/pull request when moving to "In Design" or "In Build"

---

## Issue Aggregation Across Sessions

### Multi-Session Scenario

When running multiple sessions with different participants or repeating sessions:

1. **Maintain Separate Files Per Session** — Create `issue_log_SESSION-A.csv` and `issue_log_SESSION-B.csv`
2. **Merge Into Master Log** — Combine all logs into `issue_log_MASTER.csv` with cumulative numbering per participant
3. **Deduplicate** — If same issue appears with multiple participants, create single row with frequency count and add multiple participant initials in "Notes"
4. **Cross-Reference** — In "Notes" column, link to all session IDs where issue was observed: "Observed in Session-A, Session-C"

### Deduplication Example

| ID | Severity | Title | Frequency | Notes |
|----|----------|-------|-----------|-------|
| SM-04 | Major | Cart doesn't update on mobile | 2x | SM (Sarah Malone), JR (James Rodriguez); Session-A, Session-B |

---

## Cross-Referencing Issues to Session IDs

### Linking Strategy

- **Session ID Format** — Use `YYYY-MM-DD-[Participant-Initials]` (e.g., `2025-02-12-SM`)
- **Issue Notes Field** — Always include session reference: `Session: 2025-02-12-SM; Timestamp: 14:23`
- **Session Artifacts** — Store original notes at `Sessions/2025-02-12-SM/notes.md`

### Example Issue with Full Context

| ID | Severity | Title | Description | Role Affected | Frequency | Effort | Status | Notes |
|----|----------|-------|-------------|---------------|-----------|--------|--------|-------|
| SM-07 | Major | Search query not persisting | User typed "red widgets" in search. Clicked filter. Filter applied but search term was cleared. User had to re-enter search term after using filter. | Designer | 1x | Low | Open | Session: 2025-02-12-SM; Timestamp: 15:47; Observed during product search task |

### Master Reference Log

Maintain a simple index file `Sessions/INDEX.md`:

```
# Research Session Index

## 2025-02-12
- Session-A: Sarah Malone (SM) — Product search flow
- Session-B: James Rodriguez (JR) — Checkout flow
- Session-C: Amy Bjorn (AB) — Admin dashboard

Issues merged into: Logs/issue_log_MASTER.csv
```

---

## Frequency Notation

When the same issue appears multiple times:

- **Single Occurrence** — `Frequency: 1x; Notes: Session-A`
- **Multiple Participants** — `Frequency: 2x; Notes: Session-A (SM), Session-B (JR)`
- **Multiple Sessions, Same Participant** — `Frequency: 2x; Notes: Session-A (2025-02-12), Session-B (2025-02-14)`

---

## Templates & Tools

### CSV Headers (Canonical)
```
ID | Severity | Title | Description | Role Affected | Frequency | Effort | Status | Notes
```

### Alternative Extended Headers
```
ID | Severity | Title | Description | Role Affected | Frequency | Effort | Priority Score | Status | Design Ticket | Dev Ticket | Notes
```

Use the extended format when coordinating with design and engineering systems.
