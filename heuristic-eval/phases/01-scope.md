---
name: heuristic-eval
description: >
  Phase 1 — Scope & Discovery. Researches the product, defines users, maps user journeys,
  and generates heuristic hypotheses to produce a discovery brief. Use as the entry point
  for a new heuristic evaluation.
license: "Valtech / John Deere — Internal Use Only"
metadata:
  author: "Juan Reina (they/them)"
  phase: "01-scope"
  phase_name: "Scope & Discovery"
  inputs: product URL or product description, existing research seed context (optional)
  outputs: discovery brief
  feeds_into: phases/02-evidence.md, phases/03-synthesis.md
---

# Phase 1 — Scope & Discovery

**Goal:** Become well-informed about the product before anyone touches a browser.
A rigorous discovery brief prevents wasted effort in later phases — you are answering
"who uses this, what do they need to do, and where might it already hurt?" before
capturing a single screenshot.

---

## Before starting: check existing knowledge

Search the Research OS for relevant seeds before conducting external research.
If seeds exist for this product or feature area:

1. Read the seed's `01_Plan/` and `03_Synthesis/` folders.
2. Extract: known pain points, participant observations, prior hypotheses, and any issues
   already logged in the seed's `04_Evaluation/` folder.
3. Incorporate these into the heuristic hypotheses section of the brief — do not treat
   heuristic evaluation as starting from zero when qualitative research already exists.
4. Note any sessions where participants were not represented (by role, region, assistive
   technology use, or language) — these gaps inform the coverage limitations section in Phase 3.

---

## Step 1: Gather input

Ask the user for the target URL. In the same message, also ask:

- Is there a specific user type they care about most? (e.g., new users, power users, mobile users)
- Is there a specific task or flow they're most concerned about?
- Is there a relevant research seed this evaluation should connect to?

If they say "use your judgment" or provide no preferences, proceed with defaults:
assume primary users and core flows.

---

## Step 2: Research the product

Use web search to understand the product. Run these searches in parallel:

- `[product name] what is it overview` — basic product understanding
- `[product name] target users customers who uses this`
- `[product name] user reviews complaints` — check app stores, G2, Capterra, Reddit, Trustpilot
- `[product name] UX problems usability issues accessibility`
- `[product name] competitors alternatives` — category benchmarks for H4 (Consistency/Standards)

For B2C consumer apps, also: `[product name] app store reviews`  
For SaaS tools, also: `[product name] G2 reviews ease of use`  
For enterprise tools: `[product name] customer support complaints implementation`

Extract:
- What the product does in plain language
- Who the users are — job functions, contexts, technical levels
- What users complain about most (these become heuristic hypotheses)
- What competitors do differently (sets benchmarks for standards consistency)

**Apply CORE.md Audit:** Before forming user descriptions, check — what categories are being
treated as fixed? What assumptions about "the typical user" are embedded in reviews and
documentation? Who is absent from the complaint data?

---

## Step 3: Define the users

Describe the primary and secondary user populations based on your research. Resist
collapsing to a single persona. Be explicit about:

- Range of technical levels (novice → expert is a spectrum, not two buckets)
- Range of access contexts (screen reader, keyboard-only, mobile-first, low-bandwidth)
- Language and regional context
- Frequency of use (first-time, occasional, daily-use, expert power user)

Format:

```
## Users

### Primary
**Who:** [job title / life stage / technical level — describe a range, not a single type]
**Goal:** [what they are trying to accomplish with this product]
**Context:** [when and how they use it — device, frequency, environment]
**Potential accessibility or language considerations:** [if known]

### Secondary (if relevant)
[Same structure]
```

---

## Step 4: Map four core user journeys

Identify four journeys to evaluate. These feed directly into Phase 2 Playwright scripts.

Default journey template — adapt to the product:

| # | Journey | Start | Goal | Key steps |
|---|---------|-------|------|-----------|
| 1 | Onboarding / entry | Homepage | Understand the product and start using it | Landing → value prop → CTA → sign up or first use |
| 2 | Primary task | Logged-in home | Complete the main task the product exists for | Navigate → configure → act → confirm |
| 3 | Error / edge path | Mid-task | Encounter and recover from an error | Bad input → error message → correction → retry |
| 4 | Mobile journey | Homepage on mobile | Complete journey 1 or 2 on a small screen | Same as above, different viewport |

For complex products with multiple distinct user roles, define one journey per role for the
primary task (e.g., admin journey + contributor journey).

---

## Step 5: Generate heuristic hypotheses

Based on product research and any existing seed knowledge, form 3–5 hypotheses about where
this product is likely to violate Nielsen's heuristics.

These are **informed guesses to be tested**, not findings. Grounding them in evidence makes
the evaluation more targeted and harder to dismiss as "just opinion."

Format each hypothesis:

```
[Heuristic name] — [What might be broken and for whom] — [Evidence source] — [Confidence: High/Medium/Low]
```

Examples:
- `H1 Visibility — Long-running file uploads may show no progress indicator — Reddit thread mentioning "thought it froze", 4 mentions — Confidence: Medium`
- `H4 Consistency — Primary action button label differs between the dashboard and the detail view — Prior session note P3-S2 — Confidence: High`
- `H6 Recognition — Icon-only navigation on mobile may lack accessible labels — Category norm in B2B SaaS — Confidence: Low`

---

## Step 6: Identify pages and selectors

List the key pages and UI elements to capture in Phase 2. Be specific — this directly
informs what Playwright scripts will target.

| Page | Path | What to capture |
|------|------|-----------------|
| [name] | [/path] | [screenshots, interactions, states to exercise] |

Include key states: empty state, loaded state, error state, completed/success state.

---

## Step 7: Note outcome hypotheses

This section connects the evaluation to business and research outcomes. For each heuristic
hypothesis, note what *improving* it would enable — not just what violating it prevents.

Format: `If [heuristic violation is fixed] → [outcome for users] → [outcome for the product]`

Examples:
- `If upload progress feedback is added → users can self-correct or wait confidently → reduced support tickets about "stuck uploads"`
- `If icon-only navigation is labeled → keyboard and screen reader users can navigate independently → expanded accessible user base`

This section directly feeds the opportunity framing in Phase 3 and the research priorities
in Phase 4.

---

## Output: Discovery Brief

Save as: `heuristic-discovery-[product]-[YYYY-MM-DD].md`

Use the template below. All sections are required. If a section cannot be completed,
write the reason (e.g., "No public user reviews available — proceed with category defaults").

```markdown
---
document type: heuristic discovery brief
product: [product name]
url: [URL]
date: [Month YYYY]
author: [evaluator]
seed_connection: [seed name or "standalone"]
verified: false
---

# Heuristic Discovery Brief: [Product Name]

**URL:** [URL]  
**Date:** [date]  
**Evaluator:** [name]

---

## Product Overview

[2–3 sentences: what it is, who makes it, core value proposition]

## Product Category

[e.g., B2B SaaS / Consumer mobile / Enterprise platform / Government portal]

---

## Users

### Primary
**Who:** [range of users — not a single persona]  
**Goal:** [their primary task]  
**Context:** [device, frequency, environment]  
**Access considerations:** [assistive tech, language, bandwidth constraints — known or assumed]

### Secondary (if relevant)

---

## Core User Journeys

### Journey 1: [Name]
**Start:** [URL/state]  
**Goal:** [what success looks like]  
**Steps:**
1. [step]
2. [step]

[Repeat for journeys 2–4]

---

## Key Pages to Evaluate

| Page | Path | What to capture |
|------|------|-----------------|

---

## Heuristic Hypotheses

| Heuristic | Hypothesis | Confidence | Source |
|-----------|------------|------------|--------|

---

## Outcome Hypotheses

| Fix | User outcome | Product outcome |
|-----|-------------|-----------------|

---

## Existing Research Context

[List any relevant seeds, session notes, or prior findings that informed this brief.
If none: "No prior Research OS context — evaluation proceeds from external research only."]

---

## Coverage Limitations (known at this stage)

[Note user populations, flows, or contexts that will NOT be covered in this evaluation]

---

## Notes for Phase 2 (Evidence Collection)

- [Auth/login requirements]
- [Dynamic content or loading patterns to account for]
- [Suggested viewports: desktop default + mobile]
- [Any A/B tests or regional variations]
```

---

## Pre-save quality check

Before writing the discovery brief, verify:

- [ ] At least 4 journeys are defined (adaptable — not fewer)
- [ ] Each journey has a clear start URL and success condition
- [ ] Heuristic hypotheses cite a specific evidence source (not "general intuition")
- [ ] Users section describes a range, not a single persona
- [ ] Coverage limitations are explicit — not generic ("some users may not be represented")
- [ ] If prior seeds exist, the brief explains how their findings were incorporated

---

## Handoff to Phase 2

After saving the brief:
1. Share the file location with the user.
2. Summarize in 2–3 sentences what was most notable in the research — be specific, not generic.
3. Say: "Phase 2 will use this brief to generate Playwright scripts that capture evidence across
   each journey. Load `phases/02-evidence.md` with this brief to continue."
