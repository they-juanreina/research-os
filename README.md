# Research OS — Skills Library

A library of research skills for human-led, AI-assisted UX research operations.

**Human-led and AI-assisted.** Crafted by Juan Reina (they/them) — open to contributions
from researchers, practitioners, and methodologists at any technical level.

---

## Getting Started

### What you need
- [Claude Code](https://claude.ai/code) — the desktop or VS Code extension
- This repository open as your project folder

### First time here?

Open this folder in Claude Code and type:

```
/harness
```

That's it. The harness will read the current state of your project, show you what's in progress, and guide you to the right next step. You don't need to know which skill to use — just describe what you're trying to do and it will route you.

### Setting up a new project

If you want to use Research OS for a new project (new team, new initiative), type:

```
/setup
```

It will ask you a few questions (project name, team, research lead) and scaffold a complete ready-to-use Research OS folder for you.

---

## How to use a skill

Every skill is a slash command. Type it in Claude Code and follow the prompts.

**Example — you just finished 5 interviews and want to find patterns:**
```
/thematic-coding
```
Then paste or describe your session notes. Claude will walk you through the rest.

**Not sure which skill to use?** Always start with `/harness`.

---

## All Skills

| When you want to… | Type… | Phase |
|---|---|---|
| Get oriented or not sure what to do | `/harness` | Start here |
| Start a new research initiative | `/planting-research-seeds` | Plan |
| Write a discussion guide or session script | `/discussion-guide` | Plan |
| Take notes during a live session | `/session-note-taking` | Collect |
| Transcribe a raw audio/video recording | `/meeting-transcription` | Collect |
| Process a Teams transcript or recording | `/session-ingestion` | Collect |
| Log a usability issue you just observed | `/issue-log` | Collect |
| Code session data into themes | `/thematic-coding` | Synthesize |
| Build a journey map | `/journey-mapping` | Synthesize |
| Extract How Might We statements | `/hmw-extraction` | Synthesize |
| Check if you have enough data | `/saturation-analysis` | Evaluate |
| Track research success criteria | `/success-criteria-tracking` | Evaluate |
| Run a heuristic / expert UX review | `/heuristic-eval` | Evaluate |
| Write a synthesis report for stakeholders | `/synthesis-reporting` | Report |
| Ask a question about existing research | `/querying-research-knowledge` | Query |
| Set up Research OS for a new project | `/setup` | Setup |
| Document a UI component in Storybook | `/storybook-documentation` | Design |

---

## How research is organized

Each research initiative is called a **seed**. Seeds live in the `Seeds/` folder and follow a four-phase structure:

```
Seeds/
└── [Seed Name]/
    ├── 01_Plan/        ← Discussion guides, research plans
    ├── 02_Sessions/    ← Transcripts, session notes
    ├── 03_Synthesis/   ← Themes, journey maps, HMW statements
    └── 04_Evaluation/  ← Issue logs, success criteria, saturation
```

Skills know about this structure — you don't need to manage it manually.

---

## Core principles

Every skill applies the same epistemic framework ([`CORE.md`](CORE.md)):

- Categories are constructed, not natural — binary labels require justification
- Context must be preserved before compressing data into outputs
- Edge cases and minority perspectives are never discarded
- All outputs are provisional — one analytical lens at one point in time
- Automation amplifies human judgment; it does not replace it

---

## Contributing

Research OS is an open project. Contributions from researchers, practitioners, and
methodologists are welcome — and the most valuable contributions right now require
no code at all.

### Your first contribution: run an eval

The skills in this library have never been systematically tested against their own
quality gates. The best way to improve them — and the best way to start contributing
— is to run an evaluation on a skill you use or care about.

**What you need:** Claude Code and 30–60 minutes. No Python. No git setup beyond
cloning this repo.

**What you do:**
1. Pick a skill from the table above
2. Open this folder in Claude Code
3. Run the skill with a fabricated research scenario (not real participant data)
4. Score the output against the six-check rubric in [`skills/evals/rubric/core_rubric.md`](skills/evals/rubric/core_rubric.md)
5. [Submit your findings as a GitHub issue](https://github.com/they-juanreina/research-os/issues/new?template=eval_findings.md) — no PR required

That's it. Every finding improves the skill directly.

Running an eval is not a support task — it's research. You're studying how well
the tool applies its own principles. The same epistemic standards apply to the
evaluation that apply to the research the tool supports.

The full guide is in [`skills/evals/README.md`](skills/evals/README.md).

### Other ways to contribute

**Write eval cases** — Each skill needs three test cases (normal, edge, adversarial).
Pick one skill, write its cases in Markdown using the template, open a PR.
See [issue #24](https://github.com/they-juanreina/research-os/issues/24).

**Propose a methodology improvement** — If a skill applies its principles weakly,
or misses an edge case you've encountered in practice, [open a methodology proposal](https://github.com/they-juanreina/research-os/issues/new?template=methodology_proposal.md).
These don't require code — just a careful argument grounded in [`CORE.md`](CORE.md).

**Correct the language** — If a skill uses language that violates [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md)
— assumed pronouns, unjustified binary classifications, gendered defaults — open an issue or a PR.

**Contribute a new skill** — If you work in a research method not covered here
(diary studies, participatory design, longitudinal tracking, etc.), read the
[skill contribution guide](CONTRIBUTING.md) and open a [skill submission issue](https://github.com/they-juanreina/research-os/issues/new?template=skill_submission.md).

Before contributing anything, read [`CONTRIBUTING.md`](CONTRIBUTING.md). It's the
epistemic contract for this project — what it means to contribute here goes beyond
code style.

---

## Project foundation

| File | Purpose |
|------|---------|
| [`CORE.md`](CORE.md) | Shared epistemic framework — loaded with every skill invocation |
| [`PIPELINE.md`](PIPELINE.md) | Composability model — how skills chain and hand off outputs |
| [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md) | Language and pronoun handling standards |
| [`AUTHORSHIP.md`](AUTHORSHIP.md) | Creator positioning and epistemic stance |
| [`ROADMAP.md`](ROADMAP.md) | Where the project is going and why |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to contribute — the full epistemic contract |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | How contributors treat each other |

### Skill structure

Each skill directory contains:

- `SKILL.md` — Workflow, output format, quality gates *(load for every task)*
- `REFERENCE.md` — Detailed methodology, edge cases, pitfalls *(load when needed)*
- `EXAMPLES.md` — Worked examples *(load for onboarding or format clarity)*
- `TEMPLATE.md` — Blank output template *(where applicable)*
- `scripts/` — Python utilities *(where applicable)*

**Invocation pattern**: `CORE.md` + `SKILL.md` is sufficient for most tasks.
Add `REFERENCE.md` for edge cases; `EXAMPLES.md` for onboarding or format clarity.

All 16 skills are wired as project-level slash commands in `.claude/commands/`.
Anyone opening this repo in Claude Code gets them automatically — no local
configuration needed.

### Separation principle

**Skills consume Seeds. Seeds never reference Skills.**

Skills are experiment-agnostic reusable analytical capabilities. Seeds use skills
but never redefine them.
