---
name: heuristic-eval
description: >
  Phase 4 — Designer Actions & Research Initiatives. Converts evaluation findings into
  designer action briefs, issue log entries, HMW statements, and research seed briefs.
  Use after the evaluation report is complete.
license: "MIT"
metadata:
  author: "Juan Reina (they/them)"
  phase: "04-handoff"
  phase_name: "Designer Actions & Research Initiatives"
  inputs: evaluation report, discovery brief
  outputs: designer action briefs, issue log entries, HMW statements, research seed briefs
  feeds_into: issue-log, hmw-extraction, planting-research-seeds, design team
---

# Phase 4 — Designer Actions & Research Initiatives

**Goal:** Ensure no finding disappears into a report. Every significant finding must produce
one of two things: a **designer action** (something specific and buildable) or a **research
initiative** (a question that requires new investigation). Many will produce both.

This phase is where heuristic evaluation connects to the Research OS pipeline and the
design team's workstream. It is not a summary — it is a translation layer.

---

## Routing logic: action vs. research vs. both

For each Severity 2–4 finding, apply this decision:

| Condition | Route |
|-----------|-------|
| The problem is diagnosed and the fix is known | → Designer action brief |
| The plural interpretations from Phase 3 have meaningfully different fix implications | → Designer action brief + Research seed brief |
| The finding reveals a gap no prior research has addressed | → Research seed brief |
| The finding involves a population not represented in prior sessions | → Research seed brief |
| The finding needs a behavioral hypothesis tested with users | → Research seed brief |
| The finding is systemic and the root cause is unknown | → Research seed brief |
| Severity 0–1 / cosmetic / root cause is clear | → Issue log entry only (no brief needed) |

A finding may route to both a designer action brief *and* a research seed brief. This is
the normal outcome for complex, high-severity findings.

---

## Step 1: Triage all findings

Read all Sev 2–4 findings from the Phase 3 report. For each, apply the routing logic
above and note the route. Build a triage table:

| Finding ID | Title | Severity | Route | Notes |
|------------|-------|----------|-------|-------|
| HE-001 | [title] | [n] | Action / Research / Both | [reason] |

---

## Step 2: Write designer action briefs

For each finding routed to "Action" or "Both," produce a designer action brief.
The brief must be buildable — specific enough that a designer can act on it without
reading the full report.

### Action brief format

```markdown
### Action Brief [HE-XXX]: [Finding title]

**Heuristic:** H[n] — [Name]  
**Severity:** [0–4]  
**Affects:** [user population] performing [journey name]  
**URL / screen:** [URL]

#### What is broken

[1–2 sentences: what the user experiences. Use plain language — no heuristic jargon.]

#### What to change

[Specific, buildable recommendation. Name the component, behavior, or content to change.
Avoid generic advice. Examples of sufficient specificity:]
- "Add an `aria-live="polite"` region to the `.upload-status` container that announces
  completed and failed states within 1 second of the event."
- "Replace placeholder-only labels on all fields in the signup form with persistent visible
  labels above the field."
- "Add a confirmation dialog before the 'Delete' action in the data table. The dialog must
  name the record being deleted and require explicit confirmation ('Delete [record name]')
  rather than a generic 'Yes / No'."

#### Effort estimate

[XS — cosmetic copy/config / S — single component change / M — pattern-level change across
multiple screens / L — architectural or system change]

#### Acceptance: how to verify the fix worked

[1–3 testable criteria. These can be re-run in Phase 2 after the fix is deployed.]
- [ ] [Specific observable condition that confirms the fix]
- [ ] [Optional: automated assertion that confirms the fix — reference heuristic-assertions.md]

#### Open questions for the designer

[If there are genuine design decisions within the fix — not research questions — list them here.
Example: "Should the error message appear inline below the field, or in a toast at the top?
Either is acceptable — choose based on the component library pattern."]
```

---

## Step 3: Write issue log entries

For every finding (Sev 0–4), produce an issue-log-compatible entry. These feed directly
into the `issue-log` skill and the seed's `04_Evaluation/issue-log.md`.

### Severity mapping

| Heuristic severity | Issue log severity |
|--------------------|--------------------|
| 4 — Catastrophic | Critical |
| 3 — Major | High |
| 2 — Moderate | Medium |
| 1 — Cosmetic | Low |
| 0 — Not a problem | (omit) |

### Issue entry format

```markdown
| [HE-XXX] | [Finding title] | [Critical/High/Medium/Low] | H[n] | [Journey name] | [URL] | [Open] |
```

Produce this as a table with all entries, ready to paste into the seed's issue log.

---

## Step 4: Generate HMW statements

For each Sev 2–4 finding, reframe the pain point as a How Might We opportunity statement.
This output feeds `hmw-extraction` or can be used directly as opportunity framing.

HMW transformation rules (from `hmw-extraction` skill):
- Lead with the user perspective, not the system's perspective
- Frame as an opportunity, not a description of failure
- Keep broad enough to invite multiple solutions, not narrow enough to prescribe one
- Do not name a specific technical fix inside the HMW

### HMW format

```
HMW-[HE-XXX]: How might we [opportunity], so that [user] can [outcome]?

Origin finding: [HE-XXX title]
Heuristic: H[n]
Evidence: [brief quote or description from evidence]
Priority: [High/Medium/Low — based on severity and frequency]
```

Examples of well-formed HMWs from heuristic findings:

- *Finding: form submits silently, user doesn't know if action succeeded*  
  → `How might we keep users informed at every step, so that they can trust their actions
     have been completed without checking a second time?`

- *Finding: delete action has no confirmation dialog*  
  → `How might we protect users from irreversible mistakes, so that the cost of errors
     is always recoverable?`

- *Finding: icon-only navigation lacks labels*  
  → `How might we make every navigation option legible to any user, regardless of prior
     product familiarity or assistive technology context?`

---

## Step 5: Write research seed briefs

For each finding routed to "Research" or "Both," produce a seed brief in the format
compatible with `planting-research-seeds`.

A seed brief is appropriate when:
- The root cause requires behavioral data from actual users
- The plural interpretations point to different recommended fixes
- A user population not yet represented in research is affected
- The evaluator has low-to-medium confidence and more data would change the recommendation

### Seed brief format

```markdown
### Seed Brief [HE-XXX-S]: [Research question title]

**Origin finding:** [HE-XXX — Finding title]  
**Heuristic:** H[n]  
**Severity if hypothesis confirmed:** [0–4]

#### Why this needs research (not just a fix)

[1–2 sentences: what the evaluation cannot determine. Why does a designer action alone
risk being wrong? What would change about the recommendation if interpretation 1 is
true vs. interpretation 2?]

#### Research question

[One specific, answerable question. Not "how do users feel about X" but "what do users
expect to happen after they click X — and how do they recover when their expectation is not met?"]

#### Suggested method

[Moderated usability testing / Unmoderated task-based test / Contextual inquiry /
Interview / Survey / Analytics analysis — with a one-sentence rationale]

#### Participants needed

[Who needs to be in the session. Include any population currently underrepresented in
prior seeds that this finding specifically concerns.]

#### Connects to

[List any prior seeds, session notes, or HMW statements this research would inform
or extend]

#### Recommended seed phase placement

[01_Plan → what should be in the discussion guide /
02_Sessions → evidence to collect /
03_Synthesis → how findings would be synthesized /
04_Evaluation → what success looks like]
```

---

## Step 6: Compile the handoff document

Output file: `heuristic-handoff-[product]-[YYYY-MM-DD].md`

Structure:

```markdown
---
document type: heuristic evaluation handoff
product: [product name]
date: [Month YYYY]
origin_report: heuristic-report-[product]-[YYYY-MM-DD].md
author: [name]
seed_connection: [seed name or "standalone"]
verified: false
---

# Heuristic Evaluation Handoff: [Product Name]

**Findings routed:** [n total]  
**→ Designer action briefs:** [n]  
**→ Research seed briefs:** [n]  
**→ Both:** [n]  
**→ Issue log only:** [n]

---

## Triage Summary

[Triage table from Step 1]

---

## Designer Action Briefs

[All action briefs from Step 2, ordered by severity descending]

---

## Issue Log Entries

[Issue log table from Step 3]

---

## HMW Statements

[All HMW statements from Step 4, ordered by priority]

---

## Research Seed Briefs

[All seed briefs from Step 5]

---

## Next steps

### For the design team
[Numbered list: which action briefs to start with, any sequencing dependencies,
and how to use the acceptance criteria to verify fixes]

### For the research team
[Which seed briefs to plant first, any sequencing dependencies between research questions,
and how findings from new seeds would update the handoff recommendations]

### For stakeholders
[3–5 bullet points: patterns observed, confidence level in the findings, what investment
in research or design would most improve the product's usability]
```

---

## Export suggestions

The handoff document is authored in Markdown. For stakeholder distribution:
- **PDF / DOCX:** Use `pandoc heuristic-handoff-*.md -o handoff.pdf` (or `.docx`) for polished output.
- **Issue tracker:** Copy the issue-log table rows directly into Jira, GitHub Issues, or Azure DevOps work items.
- **Design tool:** Paste action briefs into Figma/FigJam annotations linked to the affected screen.

---

## Regression testing

After the design team ships fixes for action briefs:
1. Re-run the Phase 2 Playwright scripts against the updated build.
2. Compare the new `heuristic-findings.json` to the original.
3. Mark resolved findings in the issue log.
4. Flag any new findings introduced by the fix (regressions).
5. Update the handoff document with a "Fix Verification" appendix summarizing pass/fail per action brief.

---

## Quality gate

Before completing Phase 4, verify:

- [ ] Every Sev 3–4 finding has at least one action brief, one seed brief, or both
- [ ] Every finding (Sev 1+) has an issue log entry
- [ ] Every Sev 2+ finding has a HMW statement
- [ ] Seed briefs include participant requirements that reflect populations underrepresented
      in prior research
- [ ] Action briefs include specific, testable acceptance criteria
- [ ] The handoff document is self-contained — a reader who has not seen the full report
      knows what to do next
- [ ] Export format is confirmed with the stakeholder (Markdown, PDF, or DOCX)
