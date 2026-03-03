# Skills 3.0

A library of research skills integrating plural epistemology and radical tenderness as methodological requirements.

**Human-led and AI-assisted.** Crafted by Juan Reina (they/them).

---

## Shared Foundation

Every skill in this library depends on two shared files:

| File | Purpose |
|------|---------|
| [`CORE.md`](CORE.md) | Shared epistemic framework — load with every skill invocation |
| [`PIPELINE.md`](PIPELINE.md) | Composability model — how skills chain and hand off outputs |

**Invocation pattern**: `CORE.md` + `SKILL.md` is sufficient for most tasks. Add `REFERENCE.md` for edge cases; add `EXAMPLES.md` for onboarding or format uncertainty.

---

## Available Skills

| Skill | Purpose | Phase |
|-------|---------|-------|
| [discussion-guide](skills/discussion-guide/SKILL.md) | Generate teleprompter-ready facilitator scripts | Plan |
| [session-note-taking](skills/session-note-taking/SKILL.md) | Structured observation during moderated sessions | Collect |
| [issue-log](skills/issue-log/SKILL.md) | Track and categorize usability/research issues | Collect |
| [thematic-coding](skills/thematic-coding/SKILL.md) | Transform raw session data into a validated codebook and coded evidence dataset | Synthesize |
| [journey-mapping](skills/journey-mapping/SKILL.md) | Synthesize qualitative data into experience maps | Synthesize |
| [hmw-extraction](skills/hmw-extraction/SKILL.md) | Transform pain points into opportunity statements | Synthesize |
| [saturation-analysis](skills/saturation-analysis/SKILL.md) | Determine when research reaches thematic saturation | Evaluate |
| [success-criteria-tracking](skills/success-criteria-tracking/SKILL.md) | Map objectives to indicators and track go/no-go | Evaluate |
| [querying-research-knowledge](skills/querying-research-knowledge/SKILL.md) | Answer questions from the research corpus with evidence and confidence ratings | Query |
| [planting-research-seeds](skills/planting-research-seeds/SKILL.md) | Create a new research seed with metadata, starter plan, and phase folders | Plant |
| [heuristic-eval](skills/heuristic-eval/SKILL.md) | Run expert UX reviews; every evaluation produces designer action briefs and research seed briefs | Evaluate |
| [synthesis-reporting](skills/synthesis-reporting/SKILL.md) | Package synthesis findings into a confidence-rated, evidence-grounded stakeholder report | Report |

---

## Skill Structure

Each skill directory contains:

- `SKILL.md` — Core instructions: workflow, output format, quality gates *(load for every task)*
- `REFERENCE.md` — Detailed methodology, edge cases, pitfalls *(load when needed)*
- `EXAMPLES.md` — Worked examples *(load for onboarding or format clarity)*
- `TEMPLATE.md` — Blank output template *(where applicable)*
- `scripts/` — Python utilities *(where applicable)*

---

## Core Epistemic Principles

See [`CORE.md`](CORE.md) for the full framework. In brief:

1. Intelligence is orchestrated, not generated.
2. Categories are constructed, not natural.
3. Binary assumptions must be explicitly justified.
4. Compression requires context.
5. Automation amplifies intention; it does not replace judgment.
6. Care precedes optimization.
7. Outputs are provisional and perspective-dependent.

---

## Separation Principle

**Experiments consume Skills. Skills never reference Experiments.**

Skills are completely experiment-agnostic reusable analytical capabilities.

See [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md) for language and pronoun handling standards.
