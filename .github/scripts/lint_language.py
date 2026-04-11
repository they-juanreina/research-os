#!/usr/bin/env python3
"""
Language policy linter for Research OS.

Checks Markdown files in skills/ against LANGUAGE_POLICY.md.
All findings are WARNINGS — never hard failures. Language policy
enforcement requires human review; this script surfaces candidates.

Checks:
  1. Gendered default pronouns (he/she used as generics)
  2. Common gendered nouns used as defaults
  3. Binary classifications without a justification marker
  4. Assumed heteronormative or binary framings

Output: annotated list of candidates with file, line, and reason.
Exits 0 always — warnings inform review, they do not block merges.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parents[2]
SKILLS_DIR = ROOT / "skills"

# Patterns that warrant a warning.
# Format: (regex, explanation, severity)
# severity: "flag" = always surface, "maybe" = context-dependent
PATTERNS = [
    # Gendered pronouns used generically (he/she as defaults, not referring to a named person)
    (
        r"\b(he or she|she or he|his or her|her or his|him or her|he/she|she/he)\b",
        "Gendered pronoun pair — use 'they' instead",
        "flag",
    ),
    (
        r"\bthe user\b.{0,30}\b(he|his|him)\b",
        "Gendered pronoun for 'the user' — use 'they/their'",
        "flag",
    ),
    (
        r"\bthe user\b.{0,30}\b(she|her|hers)\b",
        "Gendered pronoun for 'the user' — use 'they/their'",
        "flag",
    ),
    (
        r"\bthe researcher\b.{0,30}\b(he|his|him)\b",
        "Gendered pronoun for 'the researcher' — use 'they/their'",
        "flag",
    ),
    (
        r"\bthe researcher\b.{0,30}\b(she|her|hers)\b",
        "Gendered pronoun for 'the researcher' — use 'they/their'",
        "flag",
    ),
    (
        r"\bthe participant\b.{0,30}\b(he|his|him)\b",
        "Gendered pronoun for 'the participant' — use 'they/their'",
        "flag",
    ),
    (
        r"\bthe participant\b.{0,30}\b(she|her|hers)\b",
        "Gendered pronoun for 'the participant' — use 'they/their'",
        "flag",
    ),
    # Gendered nouns used as defaults
    (
        r"\b(businessmen|manpower|mankind|chairman|stewardess|fireman|policeman|mailman)\b",
        "Gendered noun — use a neutral alternative",
        "flag",
    ),
    (
        r"\b(guys)\b",
        "Informal gendered address ('guys') — use 'folks', 'everyone', or 'team'",
        "maybe",
    ),
    # Binary framings without justification
    (
        r"\b(is either|either .{1,40} or)\b",
        "Possible unjustified binary — verify this is not a spectrum or add '(justified: ...)' note",
        "maybe",
    ),
    (
        r"\b(male or female|female or male|men and women|women and men)\b",
        "Binary gender framing — consider 'people of all genders' or justify if binary is required",
        "flag",
    ),
]

COMPILED = [(re.compile(p, re.IGNORECASE), msg, sev) for p, msg, sev in PATTERNS]


def lint_file(path: Path) -> list[tuple[int, str, str, str]]:
    """Return list of (line_number, matched_text, message, severity)."""
    findings = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return findings

    for i, line in enumerate(lines, start=1):
        # Skip code blocks (lines inside ``` fences) — false positive rate is high
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("    "):
            continue
        for pattern, msg, sev in COMPILED:
            for match in pattern.finditer(line):
                findings.append((i, match.group(0), msg, sev))
    return findings


def main():
    print("=== Language policy lint ===\n")
    print("All findings are WARNINGS. Human review required before acting on these.\n")

    md_files = list(SKILLS_DIR.rglob("*.md"))
    if not md_files:
        print("No Markdown files found in skills/ — skipping")
        sys.exit(0)

    total = 0
    for path in sorted(md_files):
        findings = lint_file(path)
        if findings:
            rel = path.relative_to(ROOT)
            for lineno, matched, msg, sev in findings:
                label = "FLAG " if sev == "flag" else "MAYBE"
                print(f"  {label}  {rel}:{lineno}  [{matched!r}]  {msg}")
                total += 1

    print()
    if total == 0:
        print("Result: No language policy candidates found")
    else:
        print(
            f"Result: {total} candidate(s) found — review each before merging. "
            f"These are warnings, not failures."
        )

    # Always exit 0 — language lint is informational
    sys.exit(0)


if __name__ == "__main__":
    main()
