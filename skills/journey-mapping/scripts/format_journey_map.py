#!/usr/bin/env python3
"""
Journey Map Format Converter

Converts between markdown journey map tables and CSV format, with validation
to ensure all required columns are present and data integrity is maintained.

Usage:
    python format_journey_map.py --input journey.md --output journey.csv --direction md2csv
    python format_journey_map.py --input journey.csv --output journey.md --direction csv2md

Required columns (in order):
    Stage, Touchpoint, User Action, Thought/Quote, Emotion, Pain Point, Opportunity, Confidence
"""

import argparse
import csv
import re
import sys
from pathlib import Path


REQUIRED_COLUMNS = [
    "Stage",
    "Touchpoint",
    "User Action",
    "Thought/Quote",
    "Emotion",
    "Pain Point",
    "Opportunity",
    "Confidence"
]


def parse_markdown_table(markdown_file):
    """
    Parse a markdown table and extract rows as dictionaries.
    Skips header and separator rows, validates column count.

    Args:
        markdown_file: Path to markdown file containing a journey map table

    Returns:
        Tuple of (column_headers, data_rows)

    Raises:
        ValueError if table format is invalid or columns don't match expected
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find markdown table blocks
    # Tables start with | and contain header and separator rows
    lines = content.split('\n')
    table_start = None
    table_end = None

    for i, line in enumerate(lines):
        if line.strip().startswith('|') and '|' in line:
            if table_start is None:
                table_start = i
            table_end = i
        elif table_start is not None and not line.strip().startswith('|'):
            break

    if table_start is None:
        raise ValueError("No markdown table found in file")

    # Extract and clean table rows
    table_lines = lines[table_start:table_end + 1]

    # Parse header row (first row with |)
    header_line = table_lines[0]
    headers = [cell.strip() for cell in header_line.split('|')[1:-1]]

    # Validate headers
    if headers != REQUIRED_COLUMNS:
        print(f"Warning: Column headers do not match expected order")
        print(f"  Expected: {REQUIRED_COLUMNS}")
        print(f"  Found: {headers}")
        if not all(col in headers for col in REQUIRED_COLUMNS):
            missing = set(REQUIRED_COLUMNS) - set(headers)
            raise ValueError(f"Missing required columns: {missing}")

    # Parse data rows (skip header and separator)
    rows = []
    for line in table_lines[2:]:  # Skip header and separator
        if not line.strip().startswith('|'):
            continue
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        if len(cells) != len(headers):
            print(f"Warning: Row has {len(cells)} cells, expected {len(headers)}. Skipping row.")
            continue
        row_dict = dict(zip(headers, cells))
        rows.append(row_dict)

    return headers, rows


def write_csv_file(csv_file, headers, rows):
    """
    Write journey map data to a CSV file.

    Args:
        csv_file: Path to output CSV file
        headers: List of column names
        rows: List of dictionaries with row data
    """
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Successfully wrote {len(rows)} rows to {csv_file}")


def parse_csv_file(csv_file):
    """
    Parse a CSV journey map file.

    Args:
        csv_file: Path to CSV file

    Returns:
        Tuple of (column_headers, data_rows)

    Raises:
        ValueError if columns don't match expected
    """
    rows = []
    headers = None

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        if not headers:
            raise ValueError("CSV file appears to be empty or malformed")

        # Validate headers
        if list(headers) != REQUIRED_COLUMNS:
            print(f"Warning: Column headers do not match expected order")
            print(f"  Expected: {REQUIRED_COLUMNS}")
            print(f"  Found: {list(headers)}")
            if not all(col in headers for col in REQUIRED_COLUMNS):
                missing = set(REQUIRED_COLUMNS) - set(headers)
                raise ValueError(f"Missing required columns: {missing}")

        for row in reader:
            rows.append(row)

    return headers, rows


def write_markdown_table(markdown_file, headers, rows):
    """
    Write journey map data to a markdown table format.

    Args:
        markdown_file: Path to output markdown file
        headers: List of column names
        rows: List of dictionaries with row data
    """
    with open(markdown_file, 'w', encoding='utf-8') as f:
        # Write header row
        f.write('| ' + ' | '.join(headers) + ' |\n')

        # Write separator row
        f.write('|' + '|'.join(['---'] * len(headers)) + '|\n')

        # Write data rows
        for row in rows:
            cells = [row.get(header, '').replace('\n', ' ') for header in headers]
            f.write('| ' + ' | '.join(cells) + ' |\n')

    print(f"Successfully wrote {len(rows)} rows to {markdown_file}")


def validate_data(rows):
    """
    Validate journey map data for common issues.

    Args:
        rows: List of dictionaries with journey map data

    Returns:
        List of validation warnings (if any)
    """
    warnings = []

    for i, row in enumerate(rows, start=1):
        # Check for empty critical fields
        if not row.get('Stage', '').strip():
            warnings.append(f"Row {i}: Stage is empty")
        if not row.get('Touchpoint', '').strip():
            warnings.append(f"Row {i}: Touchpoint is empty")
        if not row.get('User Action', '').strip():
            warnings.append(f"Row {i}: User Action is empty")

        # Check confidence value
        confidence = row.get('Confidence', '').strip()
        if confidence and confidence not in ['1', '2', '3', 'Low', 'Medium', 'High']:
            warnings.append(f"Row {i}: Confidence value '{confidence}' is not standard (expected 1/2/3 or Low/Medium/High)")

        # Check for overly long cells (may indicate formatting issues)
        for col in ['Pain Point', 'Opportunity']:
            cell = row.get(col, '').strip()
            if len(cell) > 200:
                warnings.append(f"Row {i}: {col} is very long ({len(cell)} chars). Consider breaking into multiple rows.")

    return warnings


def main():
    parser = argparse.ArgumentParser(
        description='Convert journey map tables between markdown and CSV formats'
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input file path (markdown or CSV)'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output file path'
    )
    parser.add_argument(
        '--direction',
        required=True,
        choices=['md2csv', 'csv2md'],
        help='Conversion direction'
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate the input file without converting'
    )

    args = parser.parse_args()

    try:
        input_path = Path(args.input)
        output_path = Path(args.output)

        if not input_path.exists():
            print(f"Error: Input file '{input_path}' not found", file=sys.stderr)
            sys.exit(1)

        # Parse input
        if args.direction == 'md2csv':
            print(f"Parsing markdown table from {args.input}...")
            headers, rows = parse_markdown_table(input_path)
        else:  # csv2md
            print(f"Parsing CSV file from {args.input}...")
            headers, rows = parse_csv_file(input_path)

        print(f"Found {len(rows)} rows with {len(headers)} columns")

        # Validate data
        print("\nValidating data...")
        warnings = validate_data(rows)
        if warnings:
            print(f"Validation warnings ({len(warnings)}):")
            for warning in warnings:
                print(f"  - {warning}")
        else:
            print("All validation checks passed")

        if args.validate_only:
            print("\nValidation complete. No conversion performed.")
            sys.exit(0)

        # Write output
        print(f"\nConverting to {'CSV' if args.direction == 'md2csv' else 'Markdown'}...")
        if args.direction == 'md2csv':
            write_csv_file(output_path, headers, rows)
        else:  # csv2md
            write_markdown_table(output_path, headers, rows)

        print(f"Conversion complete!")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
