#!/usr/bin/env python3
"""
Skill structure validator for Research OS.

Rules:
  HARD FAIL  — skill directory is missing SKILL.md
  HARD FAIL  — .claude/commands/ has a command with no matching skills/ directory
  WARNING    — skill is missing REFERENCE.md (recommended, not required for meta/utility skills)
  WARNING    — skill is missing EXAMPLES.md (recommended, not required for meta/utility skills)
  WARNING    — SKILL.md is missing a required section heading

Exits 1 if any hard failures are found. Warnings are printed but do not fail the build.
"""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).parents[2]
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / ".claude" / "commands"

# Skills that are intentionally minimal (meta/utility — no REFERENCE.md or EXAMPLES.md required)
META_SKILLS = {"harness", "setup", "planting-research-seeds"}

# Required content markers in SKILL.md (case-insensitive substring match).
# Skills use either "## Workflow" headings or "**Input**:" bold labels — both are valid.
REQUIRED_SECTIONS = [
    ("workflow", "a Workflow section (## Workflow or similar)"),
    ("**input**", "an Input declaration (**Input**: ...)"),
    ("**output**", "an Output declaration (**Output**: ...)"),
]

WARNINGS = []
FAILURES = []


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN  {msg}")


def fail(msg):
    FAILURES.append(msg)
    print(f"  FAIL  {msg}")


def check_skill_directory(skill_dir: Path):
    name = skill_dir.name

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"skills/{name}/ is missing SKILL.md")
        return  # Can't check sections without SKILL.md

    # Check required sections
    content = skill_md.read_text(encoding="utf-8").lower()
    for marker, label in REQUIRED_SECTIONS:
        if marker not in content:
            warn(f"skills/{name}/SKILL.md appears to be missing {label}")

    if name not in META_SKILLS:
        if not (skill_dir / "REFERENCE.md").exists():
            warn(f"skills/{name}/ has no REFERENCE.md — recommended for non-meta skills")
        if not (skill_dir / "EXAMPLES.md").exists():
            warn(f"skills/{name}/ has no EXAMPLES.md — recommended for non-meta skills")


def check_command_coverage():
    """Every command file in .claude/commands/ must have a matching skills/ directory."""
    if not COMMANDS_DIR.exists():
        warn(".claude/commands/ directory not found — skipping command coverage check")
        return

    for cmd_file in COMMANDS_DIR.glob("*.md"):
        skill_name = cmd_file.stem
        if not (SKILLS_DIR / skill_name).exists():
            fail(
                f".claude/commands/{cmd_file.name} references skill '{skill_name}' "
                f"but skills/{skill_name}/ does not exist"
            )


def main():
    if not SKILLS_DIR.exists():
        fail("skills/ directory not found")
        sys.exit(1)

    print("=== Skill structure validation ===\n")

    skill_dirs = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    if not skill_dirs:
        warn("No skill directories found in skills/")

    for skill_dir in sorted(skill_dirs):
        check_skill_directory(skill_dir)

    check_command_coverage()

    print()
    if FAILURES:
        print(f"Result: {len(FAILURES)} failure(s), {len(WARNINGS)} warning(s)")
        sys.exit(1)
    elif WARNINGS:
        print(f"Result: OK with {len(WARNINGS)} warning(s) — review before merging")
    else:
        print("Result: All checks passed")


if __name__ == "__main__":
    main()
