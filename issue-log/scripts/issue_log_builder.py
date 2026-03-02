#!/usr/bin/env python3
"""
Issue Log Builder

Utility for creating and maintaining issue logs from research session notes.

Usage:
    python issue_log_builder.py --sessions ./sessions/ --output issue_log.csv
    python issue_log_builder.py --append issue_log.csv --participant "Sarah Malone"
    python issue_log_builder.py --append issue_log.csv --participant "Sarah Malone" --session-date 2025-02-12

Features:
    - Extracts participant names from markdown headers
    - Generates issue ID prefixes from participant initials
    - Creates blank issue log CSV templates
    - Appends new entries with auto-incremented IDs
    - Preserves existing data when appending
"""

import argparse
import os
import csv
import re
from pathlib import Path
from datetime import datetime


def extract_initials(name):
    """Generate initials from full name (e.g., 'Sarah Malone' -> 'SM')."""
    parts = name.strip().split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1:
        return parts[0][:2].upper()
    return "XX"


def extract_names_from_sessions(session_dir):
    """
    Scan markdown files in sessions directory and extract participant names.
    Looks for headers like: "# Session: Sarah Malone" or "## Participant: Sarah Malone"
    """
    participants = {}
    session_path = Path(session_dir)

    if not session_path.exists():
        print(f"Warning: Session directory {session_dir} does not exist.")
        return participants

    for md_file in session_path.glob("**/*.md"):
        with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

            # Match patterns like "# Session: Sarah Malone" or "## Participant: Sarah Malone"
            matches = re.findall(r'#+ (?:Session|Participant):\s*(.+?)(?:\n|$)', content)
            for match in matches:
                name = match.strip()
                initials = extract_initials(name)
                if name and initials not in participants:
                    participants[initials] = name

    return participants


def get_highest_id_number(csv_file, participant_initials):
    """Read existing CSV and find highest ID number for participant."""
    if not os.path.exists(csv_file):
        return 0

    highest = 0
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='|', skipinitialspace=True)
            if reader.fieldnames:
                for row in reader:
                    if row and 'ID' in row:
                        id_val = row['ID'].strip()
                        if id_val.startswith(participant_initials + '-'):
                            try:
                                num = int(id_val.split('-')[1])
                                highest = max(highest, num)
                            except (ValueError, IndexError):
                                pass
    except Exception as e:
        print(f"Warning: Could not read {csv_file}: {e}")

    return highest


def create_blank_log(output_file, participants=None):
    """Create a blank issue log CSV with headers and optional participant rows."""
    headers = [
        'ID', 'Severity', 'Title', 'Description', 'Role Affected',
        'Frequency', 'Effort', 'Status', 'Notes'
    ]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter='|')

        # Write header row
        f.write(' | '.join(headers) + '\n')

        # Write example rows if participants provided
        if participants:
            for initials, name in participants.items():
                example_row = {
                    'ID': f'{initials}-01',
                    'Severity': '[Blocker|Major|Minor|Polish]',
                    'Title': '[Issue title]',
                    'Description': '[Observable behavior description]',
                    'Role Affected': '[User role]',
                    'Frequency': '[1x|2x|3x+]',
                    'Effort': '[Low|Medium|High]',
                    'Status': '[Open|In Design|In Build|Resolved]',
                    'Notes': f'Session: [YYYY-MM-DD-{initials}]; Timestamp: [HH:MM]'
                }
                f.write(' | '.join([example_row.get(h, '') for h in headers]) + '\n')

    print(f"Created blank issue log: {output_file}")


def append_new_entry(csv_file, participant_name, session_date=None, num_entries=1):
    """Append new blank entry/entries for participant with auto-incremented ID."""
    initials = extract_initials(participant_name)
    highest_num = get_highest_id_number(csv_file, initials)

    headers = [
        'ID', 'Severity', 'Title', 'Description', 'Role Affected',
        'Frequency', 'Effort', 'Status', 'Notes'
    ]

    # Read existing data
    existing_rows = []
    if os.path.exists(csv_file):
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter='|', skipinitialspace=True)
                if reader.fieldnames:
                    for row in reader:
                        existing_rows.append(row)
        except Exception as e:
            print(f"Warning: Could not read existing {csv_file}: {e}")

    # Create new entries
    new_rows = []
    if session_date is None:
        session_date = datetime.now().strftime('%Y-%m-%d')

    for i in range(num_entries):
        new_num = highest_num + i + 1
        new_id = f'{initials}-{new_num:02d}'
        new_row = {
            'ID': new_id,
            'Severity': '',
            'Title': '',
            'Description': '',
            'Role Affected': '',
            'Frequency': '',
            'Effort': '',
            'Status': 'Open',
            'Notes': f'Session: {session_date}-{initials}; Timestamp: '
        }
        new_rows.append(new_row)

    # Write all rows
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers, delimiter='|', extrasaction='ignore')

        # Write header
        f.write(' | '.join(headers) + '\n')

        # Write existing rows
        for row in existing_rows:
            if row.get('ID'):  # Skip empty rows
                f.write(' | '.join([str(row.get(h, '')).strip() for h in headers]) + '\n')

        # Write new rows
        for row in new_rows:
            f.write(' | '.join([str(row.get(h, '')).strip() for h in headers]) + '\n')

    print(f"Added {num_entries} new entry/entries for {participant_name} ({initials})")
    print(f"New IDs: {initials}-{highest_num + 1:02d} to {initials}-{highest_num + num_entries:02d}")


def main():
    parser = argparse.ArgumentParser(
        description='Create and manage issue logs from research session notes.'
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # Create command
    create_parser = subparsers.add_parser('create', help='Create blank issue log from sessions')
    create_parser.add_argument('--sessions', required=True, help='Path to sessions directory')
    create_parser.add_argument('--output', required=True, help='Output CSV file path')

    # Append command
    append_parser = subparsers.add_parser('append', help='Append new entries to existing log')
    append_parser.add_argument('--csv', required=True, help='Existing CSV file to append to')
    append_parser.add_argument('--participant', required=True, help='Participant full name')
    append_parser.add_argument('--session-date', help='Session date (YYYY-MM-DD), defaults to today')
    append_parser.add_argument('--count', type=int, default=1, help='Number of entries to add (default: 1)')

    args = parser.parse_args()

    if args.command == 'create':
        participants = extract_names_from_sessions(args.sessions)
        if participants:
            print(f"Found {len(participants)} participant(s): {', '.join(participants.values())}")
        create_blank_log(args.output, participants)

    elif args.command == 'append':
        append_new_entry(args.csv, args.participant, args.session_date, args.count)

    else:
        # Default behavior: if only positional args provided, infer command
        if len(parser._actions) == 1:  # Only help action
            parser.print_help()


if __name__ == '__main__':
    main()
