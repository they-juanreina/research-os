---
name: issue-log
description: "Creates structured issue logs from research session data. Use when cataloging usability issues, design friction, or behavioral blockers observed during research sessions. Assigns unique IDs, severity levels, affected roles, and design fix directions. Triggers: issue log, usability issues, bug log, friction log, issue tracking, severity classification, issue inventory."
author: "Juan Reina (they/them)"
license: "MIT"
last_updated: 2026-03-02
---

# Issue Log

> Apply `CORE.md` epistemic framework before logging. See `PIPELINE.md` for upstream/downstream handoffs.

**Input**: Session notes, transcripts, or observation data from a research session.
**Output**: Structured CSV issue log with IDs, severity, role, effort, and status.

---

## Severity Definitions

| Level | Definition | Example |
|-------|-----------|---------|
| **Blocker** | User cannot proceed; work stops entirely | Form submit disabled; user cannot complete registration |
| **Major** | Significant friction; task requires workaround | Filters hidden below fold; user must scroll to apply |
| **Minor** | Confusion or inefficiency; task still completes | Label truncated; user taps icon to understand field |
| **Polish** | Aesthetic refinement; no functional impact | Spinner lacks animation; feels unresponsive but loads |

---

## Workflow

1. **Extract session context** — Participant name, role, session date, observed task.
2. **Read chronologically** — Work through notes in order; mark friction moments with timestamps or context.
3. **Classify each issue** — Assign severity based on impact to task completion.
4. **Generate IDs** — Format: `[Initials]-[Number]` (e.g., `SM-01`). Reset per participant or aggregate across sessions as needed.
5. **Write observable descriptions** — Record *what happened*, not *what should happen*. Neutral, factual language. No prescriptive phrasing.
6. **Estimate effort** — Design or development work required to resolve: Low / Medium / High.
7. **Track frequency** — Note if issue appeared once or across multiple sessions.
8. **Create or append log** — Structured CSV; link to session notes in the "Notes" column.

---

## Output Format

CSV (pipe-delimited):

```
ID | Severity | Title | Description | Role Affected | Frequency | Effort | Status | Notes
SM-01 | Blocker | Login fails silently | User entered credentials; form submitted but no error appeared. Waited 30s before refreshing. | Developer | 1x | Medium | Open | Session-A; 14:23
SM-02 | Major | Cart total off-screen | Subtotal/tax/shipping correct but total hidden below fold on mobile. | Designer | 2x | Low | Open | Session-A, Session-B
```

---

## Priority Formula

```
Priority = (Frequency × Severity Weight) + Role Impact

Severity:    Blocker=4, Major=3, Minor=2, Polish=1
Role Impact: High (core task)=+2, Medium=+1, Low=+0
Frequency:   1x=1, 2x=2, 3x+=3
```

Score tiers: **High ≥ 8 · Medium 4–7 · Low ≤ 3**

**Effort** stays in the log as a planning column — it determines *when* and *how* an issue is fixed, not *whether* it matters. A high-effort Blocker is still a Blocker.

**Blocker override**: Any issue with Severity: Blocker requires immediate team review regardless of priority score. A user who cannot complete their primary task cannot wait for frequency analysis. Use the priority score to rank Blockers relative to each other; never use it to defer a Blocker. See `REFERENCE.md` → Priority Formula for worked examples.

---

## Quality Gates

✓ Descriptions neutral and factual — observed behavior only, no opinions or solutions
✓ Each issue references session ID and timestamp when available
✓ No duplicate IDs; sequential numbering per participant
✓ Every issue assigned exactly one severity level
✓ Effort estimates realistic for team capacity

---

## Status Lifecycle

`Open` → `In Design` → `In Build` → `Resolved`

---

## References

- `REFERENCE.md` — severity detail, ID scheme, priority formula worked examples, status lifecycle, multi-session aggregation
- `EXAMPLES.md` — complete 6-issue sample log with severity distribution and priority calculations
- `scripts/issue_log_builder.py` — Python builder utility
