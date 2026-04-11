# Contributing to Research OS

Research OS is a library of research skills for human-led, AI-assisted UX research. If you're reading this, you're considering participating in that work — and the first thing to know is that contributing here means accepting an epistemic contract, not just a code style guide.

This document explains what that contract is.

---

## The contract

Every skill in this library applies the same five-principle framework from [`CORE.md`](CORE.md). That framework is not optional, and it is not decorative. It was built to resist the ways that synthesis tools typically distort human experience: by collapsing minority perspectives, by optimizing speed over dignity, by treating categories as natural rather than constructed.

If your contribution doesn't apply these principles, it doesn't belong here — regardless of how technically correct it is.

Read [`CORE.md`](CORE.md) before you do anything else. Then read [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md). Then read [`AUTHORSHIP.md`](AUTHORSHIP.md) to understand the epistemic stance from which this project was built.

Those three documents are your onboarding.

---

## Who should contribute

Anyone doing qualitative research, UX research operations, or research methodology work who wants to encode rigorous, care-first practice into reusable tools.

You don't need to be a software engineer. Most skills are Markdown files with structured workflows, not code. If you can write a careful research procedure and apply the CORE.md principles to it, you can contribute a skill.

You don't need to be based in any particular country or cultural context — in fact, contributions from researchers in different institutional, cultural, and linguistic contexts make this library more robust. That's not a diversity statement for optics; it's methodological necessity. See the edge & variance scan principle.

---

## Your positionality

Before contributing, spend a moment with this question: **what is your relationship to the research practice you're encoding?**

Are you a practitioner who has run hundreds of sessions? A researcher studying research methodology? Someone who has been on the participant side of extractive research and wants to build something different? Someone working in a context where the dominant UX research canon doesn't fit well?

You don't need to include a biography in your PR. But being aware of your position — and naming it in your PR description — helps reviewers understand what assumptions you're carrying and what blind spots to watch for. This is what situated knowledge requires: not neutrality, but accountable positioning.

---

## What to contribute

### New skills

A skill encodes a research methodology step as a reusable, AI-assisted procedure. Good candidates for new skills:

- Research activities that aren't covered by the 16 core skills (diary studies, participatory design, longitudinal tracking, survey analysis, etc.)
- Alternative approaches to existing phases (e.g., a different synthesis method that serves a different research context)
- Skills adapted for specific institutional or cultural contexts where the default assumptions don't hold

A new skill must include:
- `SKILL.md` — workflow, input contract, output schema, quality gates, CORE.md application
- `REFERENCE.md` — edge cases, methodology notes, pitfall avoidance
- `EXAMPLES.md` — at least one worked example showing input → output

See [Skill structure](#skill-structure) below.

### Methodology improvements

Existing skills are not finished. If you have a rigorous reason to change how a skill reasons, structures its output, or applies the CORE.md principles — that's a contribution worth making. Use the methodology proposal issue template when opening that conversation.

### Language and policy corrections

If a skill uses language that violates [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md), that's a bug. Binary classifications that aren't justified, gendered defaults, assumed pronouns — flag them.

### Documentation

Clearer examples, better edge case documentation, corrections to `REFERENCE.md` files.

---

## What doesn't belong here

- Features that optimize speed over dignity (faster output generation at the cost of epistemic rigor)
- Abstractions that compress context without justification
- Skills that automate synthesis decisions that require human judgment
- Skills that require cloud API calls without an offline fallback (participant data must be able to stay local)
- Anything that treats binary classifications as natural rather than constructed

If you're unsure whether something belongs, open a discussion issue before writing code or content.

---

## Skill structure

Every skill directory must follow this structure:

```
skills/<skill-name>/
├── SKILL.md          # Workflow, input contract, output schema, quality gates (required)
├── REFERENCE.md      # Edge cases, methodology notes (required)
├── EXAMPLES.md       # At least one worked example (required)
├── TEMPLATE.md       # Blank output template (where applicable)
└── scripts/          # Python utilities (where applicable)
    └── requirements.txt
```

### `SKILL.md` required sections

1. **YAML frontmatter** with `name`, `description`, `author`, `license`, `last_updated`
2. **Input** — what the skill receives and in what format
3. **Output** — what the skill produces, with file naming conventions
4. **Workflow** — numbered steps, each referencing CORE.md principles where relevant
5. **Quality gates** — what must be true before the output is considered complete
6. **What this skill does NOT do** — explicit scope limits
7. **Pipeline position** — what feeds this skill, what this skill feeds (see [`PIPELINE.md`](PIPELINE.md))

The CORE.md application must be visible in the workflow steps — not as a preamble but as an active constraint at the specific steps where it applies.

### The slash command

Every skill also needs a corresponding command file in `.claude/commands/<skill-name>.md`. Copy the format from an existing command file — it's a short description and the skill invocation pattern.

---

## How to propose a methodology change

Methodology changes are different from bug fixes. Changing *how* a skill reasons — the order of steps, what counts as evidence, when to flag uncertainty — changes what research outputs look like downstream. That's consequential.

When proposing a methodology change:

1. **Open an issue first** using the methodology proposal template
2. Name which CORE.md principle motivates the change
3. **Name what is lost** by the change — this is a required field, not optional. Every abstraction has a cost. What context is compressed? What minority cases are affected?
4. Provide at least two alternative interpretations of the problem you're solving — the change you're proposing is one reading; name the others
5. If the change affects downstream skills, describe how

PRs for methodology changes without an associated issue will be asked to open one before review begins.

---

## The care check

Before submitting anything, run this check:

- [ ] Does this contribution apply all five CORE.md principles?
- [ ] Does the language follow LANGUAGE_POLICY.md throughout? (gender-neutral defaults, no assumed pronouns, justified binaries)
- [ ] Does this preserve context rather than compress it for convenience?
- [ ] Does this surface minority cases rather than absorb them into majority readings?
- [ ] Am I aware of my positionality relative to the research practice I'm encoding?
- [ ] Does this amplify human judgment, or does it try to replace it?

If any of these is a no, address it before submitting. If you're genuinely unsure about one of them, name the uncertainty in your PR description.

---

## Review criteria

PRs are reviewed for **epistemic integrity** as well as technical correctness. A skill that works but produces outputs that misrepresent human experience will not be merged. A skill that is imperfect but handles minority cases carefully and names its limitations honestly is worth working with.

Reviewers will:

- Check that CORE.md principles are applied in the workflow steps, not just declared in a preamble
- Check that the language policy is followed
- Check that the output schema preserves enough context for downstream skills
- Check that the skill names what it does not do
- Ask about positionality if the skill encodes assumptions that may not travel across contexts

---

## Getting help

If you're unsure where to start, open a discussion. If you find something wrong and aren't sure how to fix it, open an issue. If you want to contribute but don't know what's needed, look at the open issues labeled `good first issue`.

This project is maintained by Juan Reina (they/them). Response times vary — this is not a full-time open source project, and that's fine. Good work doesn't have a deadline.
