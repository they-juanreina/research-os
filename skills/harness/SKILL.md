---
name: harness
description: "Research OS guided entry point. Use when the user doesn't know what to do, wants an overview of available research capabilities, wants to know what phase they're in, or needs help choosing a skill. Routes to the right skill based on research phase and context. Also orients new users and shows the current state of Seeds. Triggers: harness, what should I do, where do I start, help, orient me, what's next, I'm new here, guide me, I don't know what skill to use, what can you do, research os help, show me what's available, I need to, overview, navigate, get started."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-04-10
---

# Research OS Harness

> The Harness is the guided entry point for Research OS. It reads the current state of the project, orients the user, and routes them to the right skill. Non-technical users should start here every session.

**Input**: Nothing required. Optionally: a description of what the user is trying to do.
**Output**: Orientation summary + recommended next action + skill invocation or handoff.

---

## Step 1 — Read the Current Project State

Before responding, scan the project to understand what exists:

```bash
# List all seeds and their status
find Seeds/ -name "seed.md" -exec grep -l "" {} \; 2>/dev/null | sort

# For each seed found, extract status and phase
find Seeds/ -name "seed.md" | while read f; do
  seed_dir=$(dirname "$f")
  seed_name=$(basename "$seed_dir")
  status=$(grep "^status:" "$f" | head -1 | sed 's/status: *//' | tr -d '"')
  echo "$seed_name | $status"
done 2>/dev/null

# Check what phases have content
find Seeds/ -type d -name "0[1-4]*" | sort
find Seeds/ -type f -name "*.md" | wc -l
```

Parse the results to build a mental model of:
- How many seeds exist
- Which seeds are In Progress vs Complete
- Which research phases have populated content
- Whether this looks like a brand-new project (no seeds) or an active one

---

## Step 2 — Greet and Orient

Present a brief orientation. Adapt the tone to the context:

**If the project has no seeds yet** (brand new):
> Welcome to Research OS. This project has no research initiatives yet.
>
> To start your first research initiative, I'll need a research question or topic — something you want to learn about users. Type `/planting-research-seeds` or just describe what you're curious about.

**If the project has seeds**:
> Here's a snapshot of your research:
>
> | Seed | Status | Active Phase |
> |------|--------|--------------|
> | [seed name] | [status] | [most recent phase with content] |
> | ... | ... | ... |
>
> What would you like to do?

**If the user already described what they want to do**, skip the greeting and go directly to routing (Step 3).

---

## Step 3 — Route to the Right Skill

If the user has not stated what they want, present the phase menu:

```
What are you working on?

PLAN
  [1] Create a discussion guide or session script → /discussion-guide

COLLECT
  [2] Take notes during a session → /session-note-taking
  [3] Process a Teams transcript or recording → /session-ingestion
  [4] Log a usability issue I just observed → /issue-log

SYNTHESIZE
  [5] Code session data into themes → /thematic-coding
  [6] Build a journey map → /journey-mapping
  [7] Extract How Might We statements → /hmw-extraction

EVALUATE
  [8] Check if we have enough data → /saturation-analysis
  [9] Track success criteria → /success-criteria-tracking
  [10] Run a heuristic evaluation → /heuristic-eval

REPORT
  [11] Write a synthesis report → /synthesis-reporting

KNOWLEDGE
  [12] Ask a question about existing research → /querying-research-knowledge

MANAGE
  [13] Start a new research initiative → /planting-research-seeds
  [14] Set up Research OS for a new project → /setup

  [?] I'm not sure — describe what you need
```

When the user picks a number or describes their need, do one of the following:

### A — Direct match
If the user's intent maps cleanly to a single skill, invoke that skill immediately. Do not ask for confirmation — just load it.

Example: User says "I want to build a journey map" → invoke `/journey-mapping` directly.

### B — Ambiguous intent
If the intent is unclear or spans multiple skills, ask one clarifying question before routing. Do not ask more than one question.

Example: User says "I need to analyze my sessions" — ask: "Do you want to code the data into themes first (thematic-coding), or jump straight to journey mapping / HMW extraction?"

### C — No-skill request
If the user is asking a factual question about existing research (not running a skill), route to `/querying-research-knowledge` with their question as input.

### D — Setup or onboarding
If the user is a new team member or wants to replicate Research OS for a different project, route to `/setup`.

---

## Step 4 — Provide Context for the Skill

Before handing off to a skill, give the user a one-sentence expectation:

> "I'll run **[skill name]** now. You'll end up with [brief output description]. If you have [key input] ready, bring it — otherwise I'll ask."

**Skill output summaries** (use these):

| Skill | What you'll get |
|-------|----------------|
| discussion-guide | A teleprompter-ready moderator script with timed sections and probes |
| session-note-taking | A structured note document with observations, quotes, and pain points |
| session-ingestion | Normalized JSON + filled discussion note from a Teams transcript |
| issue-log | A table of usability issues with IDs, severity, roles, and fix directions |
| thematic-coding | A codebook (theme definitions) + coded evidence dataset |
| journey-mapping | A stage-by-stage experience map with touchpoints, emotions, and opportunities |
| hmw-extraction | A prioritized list of How Might We opportunity statements with evidence |
| saturation-analysis | A recommendation (Continue / Pause / Conclude) with theme-emergence data |
| success-criteria-tracking | A go/no-go recommendation per criterion with confidence ratings |
| heuristic-eval | Heuristic findings report + designer action briefs + seed briefs |
| synthesis-reporting | A stakeholder-ready narrative report with themes, journey arc, and next steps |
| querying-research-knowledge | An evidence-grounded answer with confidence rating and citations |
| planting-research-seeds | A new seed directory with metadata, starter plan, and phase folders |
| setup | A complete Research OS project at a new path, ready to open in Claude Code |

---

## Step 5 — After Routing

Once a skill is invoked and completes, offer to:
- Return to the phase menu (`/harness` again)
- Suggest the logical next skill based on the pipeline (see `.claude/PIPELINE.md`)
- Note any quality gates that should be checked before moving on

**Pipeline suggestions to offer after each skill**:

| Just completed | Suggest next |
|----------------|-------------|
| discussion-guide | session-note-taking (run sessions, then bring back notes) |
| session-note-taking | issue-log (concurrent), thematic-coding (after all sessions) |
| session-ingestion | session-note-taking (review + fill notes) |
| issue-log | success-criteria-tracking (behavioral evidence input) |
| thematic-coding | journey-mapping OR hmw-extraction (can run concurrently) |
| journey-mapping | hmw-extraction (pain points → opportunities) |
| hmw-extraction | synthesis-reporting (if evaluation is complete) |
| saturation-analysis | Recruit more participants (Continue) OR move to reporting (Conclude) |
| success-criteria-tracking | synthesis-reporting (if go/no-go is reached) |
| heuristic-eval | issue-log, hmw-extraction, planting-research-seeds (Phase 4 outputs) |

---

## Harness Guardrails

- Never ask more than one question at a time.
- Do not explain skills the user didn't ask about.
- Do not summarize what you just did — the output speaks for itself.
- If the user seems frustrated or lost, offer the phase menu without judgment.
- Always apply `CORE.md` epistemic framework to any skill you invoke.
- If this is the user's first session ever and no `.claude/` exists, refer them to the README and suggest running `/setup` from the Research OS template.
