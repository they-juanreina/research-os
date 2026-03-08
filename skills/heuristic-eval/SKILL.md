---
name: heuristic-eval
description: >
  Conducts expert UX heuristic evaluations against Nielsen Norman Group's 10 usability
  heuristics. Produces severity-rated findings with plural interpretations, designer action
  briefs, issue log entries, HMW statements, and research seed briefs. Use when auditing a
  product's usability, running an expert UX review, performing a heuristic analysis, or
  evaluating an interface against usability principles. Also triggers on: "audit the UX of
  [site]", "evaluate [product] for usability", "run a heuristic evaluation on [URL]",
  "generate a UX report", "collect Playwright evidence for a UX audit".

  ## Prerequisites
  - Web search capability (for Phase 1 product research)
  - Node.js + npm (for Phase 2 Playwright evidence collection)
  - Ability to read and analyze web content and screenshots

  ## Common use cases
  - Full UX audit of a website or web application (Phase 1 → 4)
  - Generating Playwright evidence scripts from a discovery brief (Phase 2)
  - Synthesizing automated + visual findings into a professional report (Phase 3)
  - Converting findings into design actions and research seeds (Phase 4)
  - Re-evaluating a product after fixes to measure improvement (Phase 2 → 4)
license: "MIT"
metadata:
  version: "1.0"
  last_updated: 2026-03-01
  author: "Juan Reina (they/them)"
  phases: 01-scope, 02-evidence, 03-synthesis, 04-handoff
  depends_on: CORE.md
  feeds_into: issue-log, hmw-extraction, planting-research-seeds
  lifecycle_phase: Evaluate
---

# Heuristic Evaluation Skill

A composable, four-phase skill for conducting expert UX reviews. Every evaluation produces two
mandatory categories of output: **designer actions** (specific, buildable recommendations) and
**research initiatives** (gaps that require new investigation, surfaced as seed briefs).

> **Always load `CORE.md` before invoking any phase of this skill.**

---

## Why two outputs?

Heuristic evaluation is an *inspection method* — it identifies violations against known usability
principles. What it cannot do alone is explain *why* violations exist, *how severe* they feel
to actual users, or *which* fixes would be most valued by the people using the product.

The handoff phase (Phase 4) is mandatory precisely because findings without a research pathway are treated as engineering tickets rather than as windows into user experience.
Every meaningful finding either has a known fix **or** reveals a question that requires research.

---

## Skill Pipeline

```mermaid
flowchart LR

    subgraph Phase1["01 Scope & Discovery"]
        B1["phases/01-scope.md"]
    end

    subgraph Phase2["02 Evidence Collection"]
        B2["phases/02-evidence.md"]
    end

    subgraph Phase3["03 Heuristic Synthesis"]
        B3["phases/03-synthesis.md"]
    end

    subgraph Phase4["04 Designer Actions & Research"]
        B4["phases/04-handoff.md"]
    end

    A[Product URL] --> Phase1
    Phase1 --> C[Discovery Brief]
    C --> Phase2
    Phase2 --> E["Playwright Project + heuristic-findings.json"]
    E --> Phase3
    Phase3 --> G["Evaluation Report (plural interpretations)"]
    G --> Phase4
    Phase4 --> I["Action Briefs / HMW / Issue Log / Research Seeds"]
```

Phase 4 outputs connect back to the Research OS ecosystem:

```
Phase 4 outputs
├── Designer action briefs  →  design team handoff
├── Issue log entries       →  issue-log skill
├── HMW statements          →  hmw-extraction skill
└── Research seed briefs    →  planting-research-seeds skill
```

---

## When to run each phase

| Situation | Start at |
|-----------|----------|
| Starting cold — no prior evaluation work | Phase 1 |
| Discovery brief already exists | Phase 2 |
| Playwright evidence already collected | Phase 3 |
| Report exists, need handoff artifacts only | Phase 4 |
| Quick expert review without automation | Phase 1 → Phase 3 (skip Phase 2) |
| Recurring evaluation (re-test after fixes) | Phase 2 → Phase 3 → Phase 4 |

---

## Epistemic constraints

This skill operates under `CORE.md` at all times. Additionally:

1. **Severity is a hypothesis, not a fact.** Heuristic severity ratings reflect expert judgment under
   the assumption of a "typical" user. Actual impact varies by user context, mental model, and lived experience. All Severity 3–4 findings must carry ≥ 2 interpretations (see CORE.md Plural Interpretations).

2. **Coverage is always partial.** No heuristic evaluation covers every user population, device,
   assistive technology, or language context. Every report must include an explicit coverage
   limitations section.

3. **Findings are not verdicts.** A heuristic violation is evidence of potential friction — not
   proof of failure. Phase 3 synthesis must distinguish between *observed violations* (with evidence) and *inferred impact* (analytical judgment).

4. **Automation amplifies, it does not replace.** Playwright scripts catch rule-based patterns.
   Subjective heuristics (H2, H7, H8) require human and AI visual judgment and must be explicitly labeled as such.

---

## Invocation pattern

**Minimum viable:** `CORE.md` + `SKILL.md` + the relevant phase file  
**Full evaluation:** `CORE.md` + `SKILL.md` + `phases/01-scope.md` through `phases/04-handoff.md`  
**Methodology depth:** add `REFERENCE.md`  
**Academic foundation:** add `deep-research-report.md` (literature synthesis for defensible methodology)  
**Heuristic definitions:** add `references/nng-heuristics-guide.md`  
**Playwright assertions:** add `references/heuristic-assertions.md`

---

## Output file naming convention

| Phase | Output file |
|-------|-------------|
| 01 Scope | `heuristic-discovery-[product]-[YYYY-MM-DD].md` |
| 02 Evidence | `ux-evidence-[product]/` (folder with Playwright project) |
| 03 Synthesis | `heuristic-report-[product]-[YYYY-MM-DD].md` |
| 04 Handoff | `heuristic-handoff-[product]-[YYYY-MM-DD].md` |

Save all outputs into the relevant seed's `04_Evaluation/` folder when operating within a seed.
When running as a standalone audit outside a seed, save to a named project folder.

---

## Quality gates

Before completing each phase, verify:

| Phase | Gate |
|-------|------|
| 01 | At least 4 user journeys defined; at least 3 heuristic hypotheses grounded in evidence |
| 02 | Scripts run without error; `heuristic-findings.json` populated; screenshots captured |
| 03 | All 10 heuristics addressed (even if "no violations detected"); plural interpretations on Sev 3–4 |
| 04 | Every Sev 3–4 finding has either an action brief or a research seed brief (or both) |
