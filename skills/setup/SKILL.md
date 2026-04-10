---
name: setup
description: "Scaffolds a complete Research OS project structure for a new research initiative. Use when starting a new project from scratch, onboarding a new team member, or replicating the Research OS structure in a new directory. Creates the full directory scaffold, CLAUDE.md, settings.json, and copies all skills. Triggers: setup research os, new project, initialize research os, scaffold project, onboard, replicate research os, set up for new project, create research os, new research project."
author: "Juan Reina (they/them)"
license: "Valtech / John Deere — Internal Use Only"
last_updated: 2026-04-10
---

# Research OS — Project Setup

> This skill creates a complete, ready-to-use Research OS instance at a new path. It is the entry point for non-technical users starting a fresh project.

**Input**: A destination path and a few project details.
**Output**: A fully scaffolded Research OS directory with all skills, configuration, and an empty Seeds structure — ready to use immediately.

---

## Step 1 — Gather Project Details

Ask for the following before creating any files. Do not invent values.

| Field | Description | Example |
|-------|-------------|---------|
| **Project Name** | Short name for this research project | "Notification Preferences" |
| **Organization / Client** | Client or team this research serves | "John Deere — Precision Ag" |
| **Research Lead** | Name of the person leading research | "Trey Secord" |
| **Destination Path** | Full path where the new project should live | `~/Projects/Notification-Research` |
| **Pronouns** (optional) | Pronouns for the research lead | defaults to they/them |

Confirm all fields before proceeding. State the destination path clearly and ask the user to confirm it is correct.

---

## Step 2 — Resolve Source Path

The source path is the directory where THIS skill lives — the Research OS template. Determine it by reading the path of the current `.claude/` directory. This is where skills, CORE.md, PIPELINE.md, and all configuration live.

```bash
# The source is the .claude/ directory of the current Research OS instance
SOURCE_CLAUDE="$(pwd)/.claude"
```

Verify the source contains:
- `CORE.md`
- `PIPELINE.md`
- `skills/` directory with at least 10 subdirectories

If the source is incomplete, warn the user and stop.

---

## Step 3 — Scaffold the Directory Structure

Create the following structure at the destination path:

```
[Project Name]/
├── CLAUDE.md                   ← Project-specific instructions (generated in Step 4)
├── README.md                   ← Project overview (generated in Step 5)
├── Seeds/                      ← Empty — seeds created via /planting-research-seeds
│   └── .gitkeep
├── Client/                     ← Client-facing artifacts
│   └── .gitkeep
├── Meetings/                   ← Working session notes
│   └── .gitkeep
├── Research Governance/        ← Governance documents
│   └── .gitkeep
└── .claude/
    ├── CORE.md                 ← Copied from source
    ├── PIPELINE.md             ← Copied from source
    ├── AUTHORSHIP.md           ← Copied from source
    ├── LANGUAGE_POLICY.md      ← Copied from source
    ├── README.md               ← Copied from source
    ├── settings.json           ← Generated in Step 6
    └── skills/                 ← All skills copied from source
```

Use these commands:

```bash
DEST="[destination path]/[project name]"

# Create top-level directories
mkdir -p "$DEST/Seeds"
mkdir -p "$DEST/Client"
mkdir -p "$DEST/Meetings"
mkdir -p "$DEST/Research Governance"
mkdir -p "$DEST/.claude/skills"

# Copy .claude shared files
cp "$SOURCE_CLAUDE/CORE.md" "$DEST/.claude/"
cp "$SOURCE_CLAUDE/PIPELINE.md" "$DEST/.claude/"
cp "$SOURCE_CLAUDE/AUTHORSHIP.md" "$DEST/.claude/" 2>/dev/null || true
cp "$SOURCE_CLAUDE/LANGUAGE_POLICY.md" "$DEST/.claude/" 2>/dev/null || true
cp "$SOURCE_CLAUDE/README.md" "$DEST/.claude/"

# Copy all skills recursively
cp -r "$SOURCE_CLAUDE/skills/" "$DEST/.claude/skills/"

# Create .gitkeep placeholders
touch "$DEST/Seeds/.gitkeep"
touch "$DEST/Client/.gitkeep"
touch "$DEST/Meetings/.gitkeep"
touch "$DEST/Research Governance/.gitkeep"
```

---

## Step 4 — Generate CLAUDE.md

Write a project-specific `CLAUDE.md` at the destination root. Use this template, filling in the gathered project details:

```markdown
# CLAUDE.md — [Project Name]

This file provides guidance to Claude Code when working in this Research OS project.

## Project

| Field | Value |
|-------|-------|
| **Project** | [Project Name] |
| **Organization** | [Organization / Client] |
| **Research Lead** | [Research Lead] ([pronouns]) |
| **Created** | [current date, Month YYYY format] |
| **Status** | Active |

## Architecture

​```
[Project Name]/
├── Seeds/           ← Research experiments (created via /planting-research-seeds)
├── Client/          ← Client-facing artifacts
├── Meetings/        ← Working session notes
└── Research Governance/
​```

## Getting Started

If this is your first time here, run `/harness` to get oriented and find out what to do next.

To start a new research initiative: `/planting-research-seeds`
To navigate by phase: `/harness`

## Core Rule

**Skills consume Seeds. Seeds never redefine Skills.**

See `.claude/PIPELINE.md` for how skills chain through the research lifecycle.

## Document Frontmatter Standard

All markdown files should use YAML frontmatter:

​```yaml
---
author: [Research Lead]
document type:
  - [type]
description: Brief description
date: Month YYYY
methodology:
  - [method]
tags:
  - [lowercase-tag]
verified: true/false
---
​```
```

---

## Step 5 — Generate README.md

Write a human-readable `README.md` at the destination root:

```markdown
# [Project Name] — Research OS

Research operations workspace for **[Organization / Client]**.

**Research Lead**: [Research Lead]
**Created**: [current date]

---

## Quick Start

Open this folder in [Claude Code](https://claude.ai/code) and type:

​```
/harness
​```

Claude will orient you, show what research is in progress, and guide you to the right skill for your current task.

---

## Skills Available

| When you want to… | Type… |
|-------------------|-------|
| Start a new research initiative | `/planting-research-seeds` |
| Write a discussion guide | `/discussion-guide` |
| Take session notes | `/session-note-taking` |
| Log usability issues | `/issue-log` |
| Code session data | `/thematic-coding` |
| Create a journey map | `/journey-mapping` |
| Extract HMW statements | `/hmw-extraction` |
| Check if research is saturated | `/saturation-analysis` |
| Track success criteria | `/success-criteria-tracking` |
| Run a heuristic evaluation | `/heuristic-eval` |
| Write a synthesis report | `/synthesis-reporting` |
| Ask a question about existing research | `/querying-research-knowledge` |
| Get oriented / not sure what to do | `/harness` |

---

## Structure

​```
[Project Name]/
├── Seeds/           ← One folder per research initiative
│   └── [Seed Name]/
│       ├── 01_Plan/
│       ├── 02_Sessions/
│       ├── 03_Synthesis/
│       └── 04_Evaluation/
├── Client/          ← Deliverables for stakeholders
├── Meetings/        ← Working session notes
└── Research Governance/
​```

---

*Built on Research OS Skills Library v3.0. Human-led and AI-assisted.*
```

---

## Step 6 — Generate settings.json

Write `.claude/settings.json` at the destination:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "discussion.guide|session.note|journey.map|thematic.cod|hmw|issue.log|saturation|success.criteria|synthesis.report|heuristic.eval|planting|querying|harness|/discussion|/session|/journey|/thematic|/hmw|/issue|/saturation|/success|/synthesis|/heuristic|/planting|/querying|/harness",
        "hooks": [
          {
            "type": "command",
            "command": "echo '<!-- Research OS: CORE.md auto-loaded -->' && cat .claude/CORE.md 2>/dev/null"
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "Bash(mkdir:*)",
      "Bash(cp:*)",
      "Bash(touch:*)",
      "Bash(ls:*)",
      "Bash(find:*)",
      "Bash(wc:*)",
      "Bash(source:*)",
      "Bash(python3:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git status:*)"
    ]
  }
}
```

---

## Step 7 — Confirm and Orient

After all files are created:

1. List the created structure using `find "$DEST" -maxdepth 3 | sort`
2. Show a summary table:

| Created | Path |
|---------|------|
| Root directory | `[dest]/[project name]/` |
| Seeds folder | `[dest]/[project name]/Seeds/` |
| Skills (count) | `[dest]/[project name]/.claude/skills/` (N skills) |
| CLAUDE.md | ✓ |
| README.md | ✓ |
| settings.json | ✓ |

3. Tell the user:

> **Your Research OS is ready.**
>
> Open `[destination path]` in Claude Code (VS Code extension or CLI: `claude` in that folder).
> Type `/harness` to get oriented and start your first research initiative.

---

## Quality Gates

- [ ] Destination path confirmed by user before any files are created
- [ ] Source `.claude/` verified to be complete before copying
- [ ] All 14+ skills copied (count with `ls .claude/skills/ | wc -l`)
- [ ] CLAUDE.md contains real project values (no placeholder text)
- [ ] README quick-start table uses correct skill names
- [ ] settings.json is valid JSON
