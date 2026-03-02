#!/usr/bin/env python3
"""
HMW Generator Utility

Transforms pain points and workarounds into structured HMW statement templates.
Takes a CSV of research findings and outputs a structured HMW CSV ready for Claude ideation.

Usage:
    python hmw_generator.py --input pain_points.csv --output hmw_statements.csv

Input CSV format:
    Pain Point, Workaround, Quote, Persona, Theme

Output CSV format:
    HMW_ID, Pain_Point, Workaround, HMW_Statement, Personas, Priority, Evidence, Design_Implications, Confidence
"""

import argparse
import csv
from pathlib import Path
from typing import List, Dict, Tuple


def load_pain_points(input_file: str) -> List[Dict[str, str]]:
    """Load pain points from CSV file."""
    pain_points = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                pain_points.append(row)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)
    except csv.Error as e:
        print(f"Error reading CSV: {e}")
        exit(1)
    return pain_points


def generate_hmw_id(index: int) -> str:
    """Generate HMW ID (HMW-01, HMW-02, etc.)."""
    return f"HMW-{index + 1:02d}"


def cluster_by_theme(pain_points: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Cluster pain points by their Theme column."""
    clusters = {}
    for point in pain_points:
        theme = point.get('Theme', 'Uncategorized').strip()
        if theme not in clusters:
            clusters[theme] = []
        clusters[theme].append(point)
    return clusters


def create_hmw_rows(pain_points: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Transform pain points into HMW statement rows."""
    hmw_rows = []

    for index, point in enumerate(pain_points):
        pain_summary = point.get('Pain Point', '').strip()
        workaround = point.get('Workaround', '').strip()
        quote = point.get('Quote', '').strip()
        persona = point.get('Persona', '').strip()
        theme = point.get('Theme', 'Uncategorized').strip()

        hmw_id = generate_hmw_id(index)

        # HMW Statement is left as placeholder for Claude to fill in
        hmw_statement = "[Claude: Reframe as HMW statement]"

        # Design implications are also left blank for Claude
        design_implications = "[Claude: Identify 2-4 solution directions]"

        # Default priority to Medium; can be overridden later
        priority = "Medium"

        # Confidence defaults to Medium
        confidence = "Medium"

        hmw_row = {
            'HMW_ID': hmw_id,
            'Pain_Point': pain_summary,
            'Workaround': workaround,
            'HMW_Statement': hmw_statement,
            'Personas': persona,
            'Theme': theme,
            'Priority': priority,
            'Evidence': quote,
            'Design_Implications': design_implications,
            'Confidence': confidence,
        }

        hmw_rows.append(hmw_row)

    return hmw_rows


def save_hmw_output(hmw_rows: List[Dict[str, str]], output_file: str) -> None:
    """Save HMW rows to CSV output file."""
    fieldnames = [
        'HMW_ID',
        'Pain_Point',
        'Workaround',
        'HMW_Statement',
        'Personas',
        'Theme',
        'Priority',
        'Evidence',
        'Design_Implications',
        'Confidence',
    ]

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(hmw_rows)
        print(f"✓ HMW statements saved to: {output_file}")
        print(f"  Total rows: {len(hmw_rows)}")
    except IOError as e:
        print(f"Error writing output file: {e}")
        exit(1)


def print_clusters(clusters: Dict[str, List[Dict[str, str]]]) -> None:
    """Print clustering summary to console."""
    print("\nClustering Summary:")
    print("-" * 50)
    for theme, points in clusters.items():
        print(f"  {theme}: {len(points)} pain point(s)")


def main():
    parser = argparse.ArgumentParser(
        description="Transform pain points into HMW statement templates."
    )
    parser.add_argument(
        '--input',
        required=True,
        help='Input CSV file with columns: Pain Point, Workaround, Quote, Persona, Theme'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output CSV file for HMW statements'
    )
    parser.add_argument(
        '--show-clusters',
        action='store_true',
        help='Print theme clustering summary'
    )

    args = parser.parse_args()

    # Load input
    print(f"Loading pain points from: {args.input}")
    pain_points = load_pain_points(args.input)

    if not pain_points:
        print("Error: No pain points found in input file.")
        exit(1)

    print(f"✓ Loaded {len(pain_points)} pain point(s)")

    # Cluster if requested
    if args.show_clusters:
        clusters = cluster_by_theme(pain_points)
        print_clusters(clusters)

    # Generate HMW rows
    print("\nGenerating HMW statement templates...")
    hmw_rows = create_hmw_rows(pain_points)

    # Save output
    print(f"Saving to: {args.output}")
    save_hmw_output(hmw_rows, args.output)

    print("\nNext steps:")
    print("  1. Open the output CSV")
    print("  2. For each row, fill in: HMW_Statement and Design_Implications")
    print("  3. Assign Priority scores based on Impact × Urgency / Feasibility")
    print("  4. Review and validate Evidence quotes")
    print("  5. Share with team for ideation and prototyping")


if __name__ == '__main__':
    main()
