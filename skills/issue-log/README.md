# Issue Log Skill — Canonical Structure

This directory contains a complete, canonical implementation of the Issue Log skill for Claude Code.

## Files

### 1. SKILL.md (103 lines)
**Agent-directive skill definition** with YAML frontmatter.

Contains:
- Quick Start section with agent instructions
- Severity Definitions (Blocker, Major, Minor, Polish)
- Core Workflow (8 steps)
- Output Format (CSV structure)
- Priority Formula
- Quality Gates
- References

**Tone:** Direct instructions to Claude; action-oriented; no experiment-specific references.

### 2. REFERENCE.md (270 lines)
**Comprehensive reference documentation** for implementers and users.

Contains:
- Severity level definitions with characteristics and examples for each level
- ID scheme: Format, generation rules, auto-increment rules
- Priority formula with component definitions and worked examples
- Issue description guidelines (what to include/avoid)
- Status tracking lifecycle (Open → In Design → In Build → Resolved)
- Multi-session aggregation strategy
- Cross-referencing issues to session IDs
- Frequency notation rules
- Templates & tools section

### 3. EXAMPLES.md (220 lines)
**Practical examples** demonstrating skill usage.

Contains:
- Complete sample issue log with 6 entries across all severity levels (1 Blocker, 2 Major, 2 Minor, 1 Polish)
- Severity distribution breakdown
- Priority calculation worked examples
- Issue Summary Snapshot (by severity, status, effort, role)
- Session metadata table
- Description quality examples (poor → better patterns)
- Aggregation and deduplication example
- Exporting and sharing guide (CSV, Markdown, JSON)

### 4. issue_log_builder.py (222 lines)
**Python utility** for creating and maintaining issue logs.

Features:
- Extracts participant names from markdown session headers
- Generates issue ID prefixes from participant initials
- Creates blank issue log CSV templates
- Appends new entries with auto-incremented IDs
- Preserves existing data when appending

Usage:
```bash
python issue_log_builder.py create --sessions ./sessions/ --output issue_log.csv
python issue_log_builder.py append --csv issue_log.csv --participant "Sarah Malone"
python issue_log_builder.py append --csv issue_log.csv --participant "Sarah Malone" --session-date 2025-02-12 --count 3
```

## Design Principles

### Canonical Structure
Follows Anthropic's skill template:
- SKILL.md: Agent instructions + quick reference
- REFERENCE.md: Detailed technical documentation
- EXAMPLES.md: Practical examples and worked calculations
- scripts/: Utility tools supporting the skill

### Agent-Focused
SKILL.md uses direct, actionable language to guide Claude through the issue logging workflow without prescriptive solutions.

### No Experiment-Specific References
All examples use generic fictional participants and scenarios; easily adaptable to any research context.

### Precision Over Brevity
Severity definitions include characteristics, examples, and design fix directions.
Priority formula is mathematical and reproducible.

## Quick Start

1. **Define Issues** — Read session notes and identify friction points
2. **Assign Severity** — Use the 4-level scale (Blocker → Polish)
3. **Generate IDs** — Use participant initials + sequential number
4. **Complete CSV** — Fill in Title, Description, Role, Frequency, Effort, Status
5. **Calculate Priority** — Use formula: (Frequency × Severity + Role Impact) / Effort

## CSV Format

```
ID | Severity | Title | Description | Role Affected | Frequency | Effort | Status | Notes
```

## ID Format

`[Initials]-[Number]` (e.g., `SM-01`, `JR-14`, `AB-03`)

## Severity Levels

| Level | Impact | Example |
|-------|--------|---------|
| **Blocker** | Task cannot complete | Form submission disabled |
| **Major** | Significant friction | Search hidden below fold |
| **Minor** | Confusion/inefficiency | Label truncated on mobile |
| **Polish** | No functional impact | Missing loading animation |

---

**Version:** 1.0  
**Last Updated:** 2025-02-12  
**Status:** Production-ready
**Author:** Juan Reina (they/them)
