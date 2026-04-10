# Research OS — Skills Library

A library of research skills for human-led, AI-assisted UX research operations.

**Human-led and AI-assisted.** Crafted by Juan Reina (they/them).

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

## For contributors and technical readers

### Shared foundation

| File | Purpose |
|------|---------|
| [`CORE.md`](CORE.md) | Shared epistemic framework — loaded with every skill invocation |
| [`PIPELINE.md`](PIPELINE.md) | Composability model — how skills chain and hand off outputs |
| [`LANGUAGE_POLICY.md`](LANGUAGE_POLICY.md) | Language and pronoun handling standards |

**Invocation pattern**: `CORE.md` + `SKILL.md` is sufficient for most tasks. Add `REFERENCE.md` for edge cases; `EXAMPLES.md` for onboarding or format clarity.

### Skill structure

Each skill directory contains:

- `SKILL.md` — Workflow, output format, quality gates *(load for every task)*
- `REFERENCE.md` — Detailed methodology, edge cases, pitfalls *(load when needed)*
- `EXAMPLES.md` — Worked examples *(load for onboarding or format clarity)*
- `TEMPLATE.md` — Blank output template *(where applicable)*
- `scripts/` — Python utilities *(where applicable)*

### Slash commands

All 16 skills are wired as project-level slash commands in `.claude/commands/`. Anyone opening this repo in Claude Code gets them automatically — no local configuration needed.

### Separation principle

**Skills consume Seeds. Seeds never reference Skills.**

Skills are experiment-agnostic reusable analytical capabilities. Experiments (Seeds) use skills but never redefine them.
