---
name: synthesis-reporting
document type: reference
description: Audience calibration, confidence language, epistemic framing, minority findings, limitations section guidance, and common pitfalls.
---

# Synthesis Reporting — Methodology Reference

---

## 1. Audience Calibration

The same findings require different treatment depending on who reads the report and what they will do with it. Define the audience before writing. The table below maps audiences to format decisions:

| Audience | Key question they bring | Length | Evidence visibility | What to emphasize |
|---|---|---|---|---|
| **Design team** | What should we change, and why? | Medium (4–8 pages) | High — show quotes, session counts, theme IDs | Pain points, opportunities (HMW), journey friction, specific user behaviors |
| **Product manager** | What should we prioritize, and at what confidence? | Short (2–4 pages) | Medium — confidence labels, participant counts | Executive summary, priority opportunities, go/no-go status, limitations |
| **Leadership / stakeholders** | What does the research tell us about the user? | Short (1–2 pages) | Low — confidence labels only | Executive summary, 2–3 highest-confidence findings, recommended next steps |
| **Research team** | How was this study conducted, and what did we learn analytically? | Long (full document) | Full — all evidence, codebook links, methodology notes | All themes, minority findings, limitations, methodology, open questions |
| **External / client** | Is this research valid? Can I trust it? | Medium (4–6 pages) | Medium — evidence depth, methodology section | Methodology, confidence framework, limitations, and what the report claims vs. does not claim |

### Multi-audience reports

When a report must serve more than one audience, use a layered structure:
- Lead with the executive summary (leadership)
- Follow with Key Findings at medium evidence depth (product, design)
- Append a full Methodology and Limitations section (research team, external)

Do not try to write a single section that works equally for all audiences — it will work equally poorly for all of them.

---

## 2. Confidence Language

How you write about findings should match the evidence they rest on. Inconsistent confidence language is one of the most common ways research reports mislead readers.

### High confidence
- Evidence: ≥ 3 sessions, multiple participants, multiple roles, direct behavioral evidence or explicit statements
- Language: `"Participants consistently..."`, `"Across sessions..."`, `"All three roles reported..."`, `"The data shows..."` + `[High]`
- Avoid: Language that implies certainty beyond what the study size allows (e.g., "Users always...", "All users...")

### Medium confidence
- Evidence: 2 sessions, or single-role, or observed in behavior without explicit statement
- Language: `"In this study..."`, `"Several participants..."`, `"The pattern appeared in..."` + `[Medium]`
- Flag: `"This finding is drawn from [n] sessions and should be treated as directional rather than conclusive."`

### Low confidence
- Evidence: 1 session, 1 participant, or inferred from indirect signals
- Language: `"One participant noted..."`, `"A tentative pattern suggests..."`, `"This warrants further investigation..."` + `[Low]`
- Required footnote: Explain *why* it is included despite low confidence (strong quote, underrepresented voice, contradicts a high-confidence theme, etc.)

### Prohibited language

Never use the following in a research report without explicit qualification:

| Prohibited | Why | Replace with |
|---|---|---|
| "Users want..." | Implies universal preference | "In this study, participants expressed..." |
| "The user thinks..." | Implies access to internal states | "Participant behavior suggested..." or "[Direct quote]" |
| "Always / never" | Overgeneralizes from small samples | "In every observed session..." (if true) or "Consistently across..." |
| "Clearly / obviously" | Smuggles interpretation as fact | Remove the adverb; state what the evidence shows |
| "This proves..." | Research rarely proves; it provides evidence | "This is consistent with...", "This supports..." |
| "We recommend..." (in findings) | Conflates research with design | Move to Recommended Next Steps; state as open question or seed |

---

## 3. Epistemic Framing — Writing Interpretation as Interpretation

Every claim in a synthesis report occupies one of three epistemic levels. Mixing them without labeling is the most common source of misleading reports.

### Observed
Directly recorded in session data — behavior seen, statement made, action taken.
- Format: `"[Participant role] [verb in past tense]: [description]"`
- Example: `"Participants clicked the back button an average of three times before reaching their target screen."`

### Interpreted
An inference drawn from observed behavior, grounded in evidence but not directly stated by participants.
- Format: `"[Evidence] suggests that..."` or `"One reading of this behavior is..."`
- Example: `"Repeated backward navigation suggests that participants had not formed a mental model of the information architecture."`
- Flag: Always mark interpreted claims. Never present an inference as an observation.

### Speculative
A possible explanation or implication that goes beyond the evidence — included for its potential value, clearly labeled.
- Format: `"It is possible that..."` or `"This may reflect..."` — always with `[Speculative — not grounded in direct evidence]`
- Threshold: Include speculative claims only when they are high-stakes enough to flag for future research. Do not fill reports with speculation.

### Applying plural interpretations

For any significant interpreted finding, provide ≥ 2 plausible interpretations as required by CORE.md:

```
**Finding**: Participants frequently abandoned the export workflow mid-completion. [Medium]

**Interpretation 1 (primary)**: The export configuration options exceeded participants' mental models for the task, creating decision paralysis at the final step.

**Interpretation 2 (alternative)**: Participants may have completed the export through a different path (e.g., sharing vs. downloading) and the observed abandonment reflects a successful alternative route rather than failure.

**What would distinguish these**: Reviewing completion paths in analytics; asking participants in a follow-up session whether they found an alternative.
```

---

## 4. Writing Minority Findings

A minority finding is a finding drawn from 1–2 participants that cannot be generalized but cannot be ethically suppressed. See also `thematic-coding/REFERENCE.md` → Section 6.

### When a minority finding belongs in the report

- The evidence is strong (verbatim quote, clear behavioral observation) even if rare
- The participant is from an underrepresented population in the study
- The finding contradicts a high-confidence majority finding
- If confirmed in future research, it would change a significant design decision

### How to present minority findings without distorting weight

**Do not**: present in the executive summary or at the same level as high-confidence findings.

**Do**: include in the relevant theme narrative under a subsection:

```
**Minority finding** [Low confidence — 1 participant]:
One participant (admin role, S04) described a fundamentally different workflow for the same task: rather than using the primary interface, they had built a workaround using a secondary tool. This was the only instance of this pattern in the study. If this approach is more common among admin users, it would substantially change the design implications for this theme. **Recommended: probe in follow-up sessions with admin participants.**
```

### What minority findings are not

They are not noise to be discarded. They are not anecdotes to be downweighted reflexively. They are the places where the dominant pattern breaks — which is often where the most important design information lives.

---

## 5. The Limitations Section — Why It Matters and How to Write It

The limitations section is the most intellectually honest part of a research report. It is often the shortest, most generic, and least useful part. Here is how to write it so it earns the trust it promises.

### What a limitations section is not

- Not a legal disclaimer: `"This is qualitative research and results may vary."`
- Not a list of apologies: `"We wish we had more participants."`
- Not a hedge that makes claims unfalsifiable

### What it is

A precise, specific account of what this study cannot establish, and what a reader should not conclude from it.

### Structure

**Sample scope** — Name the participants who were *not* in the study:
- `"All participants were current users who had opted into the study. Non-users, former users, and users who declined to participate are not represented. Findings should not be generalized to users who have churned."`

**Evidence gaps** — Name the open questions:
- `"TC-03 (System trust) is Low confidence — drawn from 1 session. The finding warrants inclusion but should not drive design decisions without follow-up."`

**Methodological limits** — What the method cannot establish:
- `"This study documents what participants said and did during moderated sessions. It cannot establish what participants do in unsupervised contexts, how representative this behavior is of the broader user population, or the causal relationship between any observed behavior and product design choices."`

**Interpretation limits** — Where inference replaces observation:
- `"The emotional states described in the journey map are inferred from vocal tone, word choice, and behavioral signals. Direct statements of emotion were collected where available and are labeled [High] confidence. All other emotional attributions are labeled [Inferred]."`

---

## 6. Common Pitfalls

| Pitfall | What it looks like | How to avoid it |
|---|---|---|
| **Findings as recommendations** | Findings section says "we should add X" | Findings describe what was observed. Recommendations go in Next Steps, framed as seeds or open questions. |
| **Confidence laundering** | Low-confidence finding in the executive summary without flagging | Every executive summary finding is confidence-rated. Low-confidence findings go in theme body or limitations. |
| **Symmetry theater** | Limitations section is the same length as the executive summary and equally vague | Limitations must be specific. If you can't name a specific gap, you haven't written the section yet. |
| **Ventriloquism** | Report says "users think X" or "users want Y" without evidence | Replace with: what participants said, what they did, what behavior suggests. Never infer internal states without labeling. |
| **Audience mismatch** | 12-page technical report sent to leadership; 2-page summary sent to design team | Define audience in Step 0. Report length and depth follow from that. |
| **Missing minority findings** | All findings represent the modal participant | Every theme narrative requires an edge-and-variance check. If variance existed, document it. |
| **Orphaned opportunities** | HMW statements that don't link to research evidence | Every HMW must trace to a theme ID and evidence count. If it can't, it doesn't belong in the report. |
| **Report as endpoint** | Report delivered, filing closed | Reports drive seeds, open questions, and handoff decisions — not filing. Recommended Next Steps section must be actionable. |
| **Participant erasure** | Report uses abstract language: "users experience friction" | Name the specific participants (by role, not by name) who experienced specific things. "Two admin participants (S02, S05) described..." keeps the people in the finding. |
