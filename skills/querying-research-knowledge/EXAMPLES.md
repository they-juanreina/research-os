---
name: querying-research-knowledge
file: EXAMPLES.md
last_updated: 2026-03-02
---

# Querying Research Knowledge — Examples

Five worked examples calibrating the full output format and the confidence spectrum. Read these before using the skill to understand what distinguishes a High confidence answer from a Medium one, and what the output looks like when evidence is absent.

| Example | Confidence | Key calibration |
|---------|-----------|-----------------|
| 1 | High | Full output format; verbatim citations; contradictions surfaced |
| 2 | Medium | Coded themes, limited quotes; minority finding present |
| 3 | Low | Single session; observer interpretation; explicit gap naming |
| 4 | None | No evidence → seed brief output |
| 5 | (Any) | Embedded assumption detected and flagged before answering |

---

## Example 1 — High Confidence Answer

**Question asked:** What do field technicians find most frustrating about the current work order system?

---

```
CONFIDENCE: High
SEEDS CONSULTED: Field-Technician-Workflows-2025-Q3, Mobile-Tools-Discovery-2025-Q4

WHAT THE RESEARCH SHOWS:
Field technicians consistently report two primary frustrations with the work order system:
status information that is out of date by the time they access it, and the number of
steps required to log parts and labor after completing a job.

In Field-Technician-Workflows-2025-Q3, 4 of 5 participants described arriving at a job
only to find the work order did not reflect decisions made since it was opened — missing
parts substitutions, updated customer instructions, or priority changes made by the
coordinator (Seed: Field-Technician-Workflows-2025-Q3, Sessions 01–04).

In Mobile-Tools-Discovery-2025-Q4, 3 of 4 participants named the post-job logging
workflow as the step most likely to be deferred or skipped entirely when the next call was
waiting (Seed: Mobile-Tools-Discovery-2025-Q4, Sessions 02, 03, 04).

EVIDENCE:
"By the time I get the work order, half of what's on it has already changed and nobody
updated it." — Participant T-02, Field-Technician-Workflows-2025-Q3, Session 02

"I'll do the notes at the end of the day. Sometimes at the end of the week. If the
system made it easier I'd probably do it right away." — Participant T-07,
Mobile-Tools-Discovery-2025-Q4, Session 03

"There are seven screens between me and logging a part number. Seven." — Participant T-05,
Mobile-Tools-Discovery-2025-Q4, Session 04

CONTRADICTIONS AND MINORITY FINDINGS:
One participant (T-01, Field-Technician-Workflows-2025-Q3, Session 01) did not describe
status freshness as a problem. They worked a single-account route with a stable coordinator
relationship and described the system as "good enough." This pattern may be specific to
stable, relationship-based workflows rather than general-purpose or high-turnover assignments.

WHAT WE DON'T KNOW:
- Whether the deferred logging pattern results in data loss (incomplete records) or merely
  timing shift (records completed later). No session captured end-of-day behavior.
- Technician experience level as a variable: all 9 participants had 3+ years of experience.
  New technicians may experience different friction points.
- Whether frustrations differ across equipment type (large ag vs. small equipment).

EMBEDDED ASSUMPTIONS FLAGGED:
None detected in this question.
```

---

## Example 2 — Medium Confidence Answer

**Question asked:** Do technicians use the mobile app or the desktop version more often when in the field?

---

```
CONFIDENCE: Medium
SEEDS CONSULTED: Mobile-Tools-Discovery-2025-Q4, Field-Technician-Workflows-2025-Q3,
                 Dealer-Operations-Audit-2025-Q2

WHAT THE RESEARCH SHOWS:
Available evidence suggests mobile is the primary access point in the field, but this
finding comes from 2 sessions and coded theme analysis — not from a systematic behavioral
count. It should not be treated as a frequency statistic.

In Mobile-Tools-Discovery-2025-Q4, 3 of 4 participants described using their phone or
tablet as their first point of access during a job. Desktop access was described as a
"back at the shop" behavior (Seed: Mobile-Tools-Discovery-2025-Q4, Sessions 02–04).

The coded theme "Device Context" in Field-Technician-Workflows-2025-Q3 (TC-04, 3
sessions, 3 participants) captured participants naturally shifting to desktop for tasks
requiring document upload or form-heavy data entry, and to mobile for quick status checks.
This suggests device preference is task-dependent rather than a consistent global pattern
(Seed: Field-Technician-Workflows-2025-Q3, coded dataset).

Dealer-Operations-Audit-2025-Q2 did not include technician participants — no relevant
evidence found.

EVIDENCE:
"In the field I've always got my phone. I'm not going to carry a laptop into a barn."
— Participant T-03, Mobile-Tools-Discovery-2025-Q4, Session 02

"If I'm uploading a picture of the damage, I do that on the phone. If I need to fill out
the whole service report I wait until I'm back at the computer." — Participant T-07,
Mobile-Tools-Discovery-2025-Q4, Session 03

CONTRADICTIONS AND MINORITY FINDINGS:
One participant (T-06, Field-Technician-Workflows-2025-Q3, Session 05) described preferring
desktop "almost always" due to vision difficulties with small screens. They kept a tablet
charged in their truck but rarely used it for the system. This is a single data point and
may reflect an accessibility need not represented elsewhere in the sample.

WHAT WE DON'T KNOW:
- Actual usage frequency (sessions, page views, time on device type). Research did not
  include analytics or instrumentation data.
- Whether mobile preference varies by geography (connectivity issues were mentioned once
  but not explored systematically).
- Behavior for technicians who serve primarily residential vs. commercial vs. fleet accounts.

EMBEDDED ASSUMPTIONS FLAGGED:
The question frames this as an either/or pattern ("mobile or desktop more often"). The
research suggests context-dependent switching rather than a single dominant preference.
The question may be better answered as: "For which tasks does each device type appear?"
```

---

## Example 3 — Low Confidence Answer

**Question asked:** How do service coordinators prioritize competing urgent work orders when multiple technicians are unavailable?

---

```
CONFIDENCE: Low
SEEDS CONSULTED: Field-Technician-Workflows-2025-Q3, Dealer-Operations-Audit-2025-Q2,
                 Mobile-Tools-Discovery-2025-Q4

WHAT THE RESEARCH SHOWS:
One session addressed coordinator prioritization behavior directly. The evidence captures
one coordinator's described practice but cannot be treated as representative of the role.

In Dealer-Operations-Audit-2025-Q2 (Session 03), one service coordinator participant
described using a combination of customer tier (contract vs. non-contract), crop calendar
timing ("if it's harvest time and they're down, everything else waits"), and personal
judgment about relationship priority when deciding which jobs to escalate.

No other session in the corpus included a coordinator participant who described their
prioritization logic in response to a direct question on this topic.

Note: Two technician participants in Field-Technician-Workflows-2025-Q3 mentioned
coordinator decisions as part of their experience (Sessions 01, 04), but these are
secondhand descriptions of coordinator behavior, not coordinator accounts. They are
researcher-interpreted and carry lower evidential weight.
[Inferred from secondhand technician accounts — not directly observed or stated by
coordinator participants]

EVIDENCE:
"Harvest is harvest. A down combine in August beats everything else on my list, no
matter who the customer is." — Coordinator C-01, Dealer-Operations-Audit-2025-Q2,
Session 03

CONTRADICTIONS AND MINORITY FINDINGS:
No contradicting evidence exists — this topic has only one data point. The absence of
contradiction reflects sample size, not consensus.

WHAT WE DON'T KNOW:
- Whether the crop calendar heuristic applies to coordinators at non-agricultural
  dealerships or in regions with different seasonal patterns.
- How coordinators handle situations where all urgent jobs involve harvest-season customers
  (which is not an edge case — it is the normal state during peak season).
- Whether the system supports the prioritization logic described, or whether coordinators
  work around it using external tools.
- How this decision-making process changes under different staffing conditions
  (solo coordinator vs. team of coordinators).

EMBEDDED ASSUMPTIONS FLAGGED:
The question assumes coordinators have a defined prioritization method. The one coordinator
in the corpus described a heuristic and personal judgment rather than a system or
documented procedure. It is not known whether this reflects the absence of a formal
method or simply a preference for informal approaches.
```

---

## Example 4 — No Evidence → Seed Brief

**Question asked:** What do customers expect to receive after a service call is completed?

---

```
NO RESEARCH EVIDENCE FOUND
════════════════════════════════════════════
The current research corpus does not address: what customers expect to receive as
confirmation, documentation, or follow-up after a service call is completed.

All available seeds focused on internal participants (technicians, coordinators, service
managers). No study recruited or observed end-customer participants.

PROPOSED SEED BRIEF
────────────────────────────────────────────
Title: Customer Expectations After Service Completion
Research Question: What do customers expect to receive as confirmation or documentation
after a service call is marked complete — and what happens when those expectations
are not met?
Why This Matters: Post-service communication is a key satisfaction and trust driver.
If the workflow does not support customer expectations, it risks repeat contacts,
disputes, and relationship erosion — but we currently have no evidence to act on
or design around.
Suggested Method: Semi-structured interviews with 5–8 customers who have used
dealer service in the past 12 months; supplement with 2–3 coordinator interviews
focused on customer-facing post-service communication.
Suggested Participant Criteria: Customers with at least 2 service calls in the last
year; mix of contract and non-contract accounts; mix of service call types
(warranty vs. out-of-warranty; planned vs. emergency).
Related Seeds: Dealer-Operations-Audit-2025-Q2 (coordinator perspective on
customer communication); Field-Technician-Workflows-2025-Q3 (technician
perspective on what they log at close).
────────────────────────────────────────────

Next step: Use the planting-research-seeds skill to open this as a formal research seed.
```

---

## Example 5 — Embedded Assumption Detected

**Question asked:** Why do technicians prefer not to use the app's diagnostic upload feature?

---

> ⚠️ **Embedded assumption detected**: This question assumes technicians prefer *not* to use the diagnostic upload feature. The research corpus will be searched for evidence that supports *or* contradicts this assumption — it will not be searched to confirm it.

```
CONFIDENCE: Low
SEEDS CONSULTED: Mobile-Tools-Discovery-2025-Q4, Field-Technician-Workflows-2025-Q3

WHAT THE RESEARCH SHOWS:
The research does not establish that technicians prefer to avoid the diagnostic upload
feature. Available evidence is mixed and the feature was not a focus of any session.

In Mobile-Tools-Discovery-2025-Q4 (Session 04), one participant described abandoning a
diagnostic upload midway because of poor field connectivity, not because of preference
or aversion to the feature. They did not indicate they would avoid it in conditions with
better connectivity.

In Field-Technician-Workflows-2025-Q3 (Session 02), one participant mentioned not
knowing the feature existed. This suggests a discoverability gap, not an avoidance
preference.

No participant in any seed expressed explicit dislike or avoidance preference regarding
diagnostic upload.

EVIDENCE:
"I tried to send the scan report but it kept failing. Just gave up and described it
in the notes field." — Participant T-05, Mobile-Tools-Discovery-2025-Q4, Session 04

"There's a place to upload that? I just take a photo and text it to the coordinator."
— Participant T-02, Field-Technician-Workflows-2025-Q3, Session 02

CONTRADICTIONS AND MINORITY FINDINGS:
No evidence of explicit aversion to the feature. Observed non-use appears attributable
to connectivity failure (1 case) and feature non-discovery (1 case), not preference.

WHAT WE DON'T KNOW:
- Whether participants who are aware of the feature and have reliable connectivity
  use it routinely (no session captured this scenario).
- The range of diagnostic upload contexts: size of files, required connection quality,
  how results are used downstream.

EMBEDDED ASSUMPTIONS FLAGGED:
The question presupposes avoidance preference as a known state. Current evidence does
not support this. The more productive question — and one the data does begin to address —
is: "What barriers prevent technicians from using the diagnostic upload feature when
they attempt or intend to?"
```

---

## Confidence Calibration Summary

| Level | Evidence floor | Quote availability | Pattern breadth | Contradictions |
|-------|---------------|-------------------|----------------|----------------|
| **High** | ≥ 3 sessions, consistent | Verbatim quotes from multiple participants | Pattern spans sessions and personas | Minority finding explicitly surfaced |
| **Medium** | 2 sessions or coded themes only | At least 1 verbatim quote | Pattern present but not exhaustively tested | Contradictions noted if present |
| **Low** | 1 session or secondhand account | May have 1 quote; may be observer interpretation | Single data point; not generalizable | Contradiction absence = data gap, not consensus |
| **None** | No evidence | No quotes | No pattern | N/A — seed brief issued instead |

**The threshold to move from Medium to High is not the strength of your belief in the finding — it is the number of independent sessions that produced consistent evidence.**
