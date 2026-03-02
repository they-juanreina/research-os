#!/usr/bin/env python3
"""
Thematic Coding — Evidence Extraction Tool

Reads session note CSVs from a seed's 02_Sessions/ directory and produces
a blank coding workspace CSV ready for manual or AI-assisted thematic coding.

Usage:
    python code_themes.py --sessions path/to/02_Sessions/ --output coded-workspace.csv
    python code_themes.py --sessions path/to/02_Sessions/ --output coded-workspace.csv --codebook themes.md

Input: CSV files in the sessions directory with the following columns (any subset):
    Session_ID, Participant_ID, Role, Type, Content
    Where Type is one of: observation, quote, pain_point

    Alternatively, the tool accepts session note files with these column names
    (common variations from the session-note-taking skill output):
    - observations, quotes, pain_points (as separate columns per session row)
    - observation, quote, pain_point (singular forms)

Output:
    A CSV with blank Theme_Codes, Multi_Code, Confidence, and Notes columns —
    the coding workspace. Open in any spreadsheet tool to code manually, or
    load into an AI session with the codebook and SKILL.md.

Options:
    --sessions DIR      Path to a directory containing session CSV files (required)
    --output FILE       Path for the output coding workspace CSV (required)
    --codebook FILE     Path to an existing themes.md codebook (optional).
                        If provided, theme IDs and names are listed in the header comment
                        of the output file for reference during coding.
    --seed-id TEXT      Seed ID prefix for Unit_IDs (default: "U")
    --include-empty     Include rows where Evidence_Unit is blank (default: skip)
"""

import argparse
import csv
import os
import re
import sys
from pathlib import Path


EVIDENCE_COLUMN_VARIANTS = {
    'session_id': ['session_id', 'session', 'session id'],
    'participant_id': ['participant_id', 'participant', 'participant id', 'p_id'],
    'role': ['role', 'participant_role', 'role/type'],
    'type': ['type', 'evidence_type', 'note_type'],
    'content': ['content', 'evidence_unit', 'observation', 'quote', 'pain_point',
                'text', 'note', 'evidence', 'unit'],
}

KNOWN_TYPES = {'observation', 'quote', 'pain_point', 'pain point', 'non-verbal', 'insight'}


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Extract evidence units from session notes for thematic coding'
    )
    parser.add_argument('--sessions', required=True,
                        help='Path to directory containing session CSV files')
    parser.add_argument('--output', required=True,
                        help='Path for output coding workspace CSV')
    parser.add_argument('--codebook', default=None,
                        help='Path to existing themes.md codebook (optional)')
    parser.add_argument('--seed-id', default='U',
                        help='Prefix for Unit_IDs (default: U)')
    parser.add_argument('--include-empty', action='store_true',
                        help='Include rows where Evidence_Unit is blank')
    return parser.parse_args()


def normalize_header(header):
    """Map raw column names to canonical names."""
    h = header.strip().lower().replace(' ', '_').replace('-', '_')
    for canonical, variants in EVIDENCE_COLUMN_VARIANTS.items():
        if h in variants:
            return canonical
    return h


def find_column(headers_normalized, canonical):
    """Return the original header name for a canonical column, or None."""
    for orig, norm in headers_normalized.items():
        if norm == canonical:
            return orig
    return None


def load_session_csv(filepath):
    """
    Load a session CSV and extract evidence units.
    Returns a list of dicts: {session_id, participant_id, role, type, content}
    """
    units = []
    filename = Path(filepath).stem

    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print(f"  WARN: {filepath} — no headers found, skipping")
                return units

            # Normalize headers
            headers_normalized = {h: normalize_header(h) for h in reader.fieldnames}

            col_session = find_column(headers_normalized, 'session_id')
            col_participant = find_column(headers_normalized, 'participant_id')
            col_role = find_column(headers_normalized, 'role')
            col_type = find_column(headers_normalized, 'type')
            col_content = find_column(headers_normalized, 'content')

            for row in reader:
                session_id = row.get(col_session, filename).strip() if col_session else filename
                participant_id = row.get(col_participant, '').strip() if col_participant else ''
                role = row.get(col_role, '').strip() if col_role else ''
                evidence_type = row.get(col_type, '').strip().lower() if col_type else 'observation'
                content = row.get(col_content, '').strip() if col_content else ''

                # Normalize type
                if 'quote' in evidence_type:
                    evidence_type = 'quote'
                elif 'pain' in evidence_type:
                    evidence_type = 'pain_point'
                elif 'non' in evidence_type or 'verbal' in evidence_type:
                    evidence_type = 'non_verbal'
                elif 'insight' in evidence_type:
                    evidence_type = 'insight'
                else:
                    evidence_type = 'observation'

                units.append({
                    'session_id': session_id,
                    'participant_id': participant_id,
                    'role': role,
                    'type': evidence_type,
                    'content': content,
                    'source_file': Path(filepath).name,
                })

    except Exception as e:
        print(f"  ERROR: Could not read {filepath}: {e}")

    return units


def load_codebook_themes(codebook_path):
    """
    Parse a themes.md codebook and extract theme IDs and names.
    Returns a list of (ID, Name) tuples for reference in the output header.
    """
    themes = []
    try:
        with open(codebook_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Match patterns like "TC-01: Theme Name" or "### TC-01" or "**TC-01**"
        patterns = [
            r'(TC-\d+)[:\s]+([^\n]+)',
            r'###\s+(TC-\d+)[:\s]*([^\n]*)',
        ]
        found = {}
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                tc_id = match.group(1)
                name = match.group(2).strip().lstrip('—–-').strip()
                if tc_id not in found and name:
                    found[tc_id] = name
        themes = sorted(found.items())
    except Exception as e:
        print(f"  WARN: Could not read codebook at {codebook_path}: {e}")
    return themes


def write_workspace_csv(output_path, units, seed_prefix, codebook_themes, include_empty):
    """Write the coding workspace CSV."""
    fieldnames = [
        'Unit_ID', 'Session_ID', 'Participant_ID', 'Role', 'Type',
        'Evidence_Unit', 'Theme_Codes', 'Multi_Code', 'Confidence', 'Notes'
    ]

    unit_counter = 1
    written = 0
    skipped_empty = 0

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            # Write header comment block
            f.write('# THEMATIC CODING WORKSPACE\n')
            f.write('# Generated by code_themes.py\n')
            f.write('#\n')
            f.write('# HOW TO USE:\n')
            f.write('#   1. Load this file with CORE.md + thematic-coding/SKILL.md\n')
            f.write('#   2. Complete Steps 3–7 of the skill workflow\n')
            f.write('#   3. Fill Theme_Codes, Multi_Code, Confidence, Notes for each row\n')
            f.write('#   4. Use RESIDUAL or CONTRADICTS:TC-XX in Theme_Codes as needed\n')
            f.write('#\n')

            if codebook_themes:
                f.write('# CODEBOOK REFERENCE:\n')
                for tc_id, name in codebook_themes:
                    f.write(f'#   {tc_id}: {name}\n')
                f.write('#\n')
            else:
                f.write('# No codebook loaded — define themes during first-pass clustering\n')
                f.write('#\n')

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for unit in units:
                content = unit['content']

                if not content and not include_empty:
                    skipped_empty += 1
                    continue

                unit_id = f"{seed_prefix}-{unit_counter:03d}"
                writer.writerow({
                    'Unit_ID': unit_id,
                    'Session_ID': unit['session_id'],
                    'Participant_ID': unit['participant_id'],
                    'Role': unit['role'],
                    'Type': unit['type'],
                    'Evidence_Unit': content,
                    'Theme_Codes': '',
                    'Multi_Code': '',
                    'Confidence': '',
                    'Notes': '',
                })
                unit_counter += 1
                written += 1

    except Exception as e:
        print(f"ERROR: Could not write output file: {e}")
        sys.exit(1)

    return written, skipped_empty


def main():
    args = parse_arguments()

    sessions_dir = Path(args.sessions)
    if not sessions_dir.is_dir():
        print(f"ERROR: Sessions directory not found: {sessions_dir}")
        sys.exit(1)

    # Find all CSV files in sessions directory
    csv_files = sorted(sessions_dir.glob('**/*.csv'))
    if not csv_files:
        print(f"ERROR: No CSV files found in {sessions_dir}")
        sys.exit(1)

    print(f"\nThematic Coding — Evidence Extraction")
    print(f"======================================")
    print(f"Sessions directory: {sessions_dir}")
    print(f"CSV files found: {len(csv_files)}")

    # Load all evidence units
    all_units = []
    for csv_file in csv_files:
        print(f"  Reading: {csv_file.name}")
        units = load_session_csv(csv_file)
        all_units.extend(units)
        print(f"    → {len(units)} evidence units extracted")

    if not all_units:
        print("ERROR: No evidence units extracted from any session file.")
        sys.exit(1)

    print(f"\nTotal evidence units: {len(all_units)}")

    # Load codebook if provided
    codebook_themes = []
    if args.codebook:
        codebook_path = Path(args.codebook)
        if codebook_path.exists():
            codebook_themes = load_codebook_themes(codebook_path)
            print(f"Codebook loaded: {len(codebook_themes)} theme(s) found")
        else:
            print(f"WARN: Codebook not found at {args.codebook} — proceeding without reference")

    # Write workspace
    written, skipped = write_workspace_csv(
        args.output, all_units, args.seed_id, codebook_themes, args.include_empty
    )

    print(f"\nWorkspace written to: {args.output}")
    print(f"  Rows written: {written}")
    if skipped:
        print(f"  Rows skipped (empty content): {skipped} — use --include-empty to include")

    print(f"\nNext steps:")
    print(f"  1. Open {args.output} in a spreadsheet or text editor")
    print(f"  2. Load with CORE.md + thematic-coding/SKILL.md for AI-assisted coding")
    print(f"  3. Complete first-pass clustering (Step 3) before filling Theme_Codes")
    print(f"  4. Write codebook (Step 5) before second-pass coding (Step 6)")


if __name__ == '__main__':
    main()
