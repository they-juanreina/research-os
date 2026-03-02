#!/usr/bin/env python3
"""
Saturation Analysis Computation Tool

Analyzes theme emergence in qualitative research datasets and computes
saturation metrics to determine whether additional data collection is needed.

Usage:
    python compute_saturation.py --input theme_tracking.csv --output saturation_report.csv --threshold moderate

Input CSV format:
    Session_Number, Session_Date, Participant_Role, Theme, Is_New
    1, 2024-01-15, User, Task Management, True
    1, 2024-01-15, User, Notification Overload, True
    2, 2024-01-16, Developer, API Performance, True
    ...

Output:
    - CSV report with saturation metrics per session
    - Text summary with recommendation
"""

import argparse
import csv
import sys
from collections import defaultdict, OrderedDict
from datetime import datetime


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Compute saturation metrics for qualitative research data"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file (Session_Number, Session_Date, Participant_Role, Theme, Is_New)"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output CSV file for saturation report"
    )
    parser.add_argument(
        "--threshold",
        choices=["conservative", "moderate", "aggressive"],
        default="moderate",
        help="Saturation threshold (default: moderate)"
    )
    return parser.parse_args()


def load_theme_data(input_file):
    """
    Load theme tracking data from CSV.

    Returns:
        List of dicts with keys: Session_Number, Session_Date, Participant_Role, Theme, Is_New
    """
    data = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['Session_Number'] = int(row['Session_Number'])
                row['Is_New'] = row['Is_New'].lower() in ('true', '1', 'yes')
                data.append(row)
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to read input file: {e}")
        sys.exit(1)

    if not data:
        print("ERROR: Input CSV is empty.")
        sys.exit(1)

    return data


def compute_saturation_metrics(data):
    """
    Compute saturation metrics from theme tracking data.

    Returns:
        Dict with per-session metrics and aggregate statistics
    """
    sessions = OrderedDict()
    all_unique_themes = set()
    role_themes = defaultdict(set)

    # Organize data by session
    for row in data:
        session_num = row['Session_Number']
        if session_num not in sessions:
            sessions[session_num] = {
                'date': row['Session_Date'],
                'roles': set(),
                'themes': set(),
                'new_themes': set()
            }

        sessions[session_num]['roles'].add(row['Participant_Role'])
        sessions[session_num]['themes'].add(row['Theme'])
        role_themes[row['Participant_Role']].add(row['Theme'])

        if row['Is_New']:
            sessions[session_num]['new_themes'].add(row['Theme'])
            all_unique_themes.add(row['Theme'])

    # Compute per-session metrics
    metrics = []
    cumulative_unique = 0
    sessions_since_new = 0

    for session_num in sorted(sessions.keys()):
        session = sessions[session_num]
        new_count = len(session['new_themes'])
        cumulative_unique += new_count

        # Track sessions since last new theme
        if new_count > 0:
            sessions_since_new = 0
        else:
            sessions_since_new += 1

        metrics.append({
            'session_number': session_num,
            'date': session['date'],
            'roles': ', '.join(sorted(session['roles'])),
            'new_themes_count': new_count,
            'cumulative_unique': cumulative_unique,
            'sessions_since_new': sessions_since_new
        })

    # Compute rolling 3-session average
    for i, m in enumerate(metrics):
        if i >= 2:
            rolling_avg = sum(metrics[j]['new_themes_count'] for j in range(i - 2, i + 1)) / 3
        else:
            rolling_avg = sum(metrics[j]['new_themes_count'] for j in range(0, i + 1)) / (i + 1)
        m['rolling_avg_3session'] = rolling_avg

    # Compute aggregate statistics
    total_sessions = len(metrics)
    total_unique_themes = len(all_unique_themes)
    total_new_themes = sum(m['new_themes_count'] for m in metrics)

    # Emergence rate (% of sessions that introduced new themes)
    sessions_with_new = sum(1 for m in metrics if m['new_themes_count'] > 0)
    emergence_rate = (sessions_with_new / total_sessions * 100) if total_sessions > 0 else 0

    # Average new themes per session
    avg_new_per_session = total_new_themes / total_sessions if total_sessions > 0 else 0

    # Saturation percentage (heuristic: observed / (observed + estimated_remaining))
    # Estimated remaining: 20% of currently observed (conservative estimate)
    estimated_ceiling = total_unique_themes + max(1, int(total_unique_themes * 0.2))
    saturation_pct = (total_unique_themes / estimated_ceiling * 100) if estimated_ceiling > 0 else 0

    # Unique roles
    unique_roles = set()
    for session in sessions.values():
        unique_roles.update(session['roles'])

    aggregate = {
        'total_sessions': total_sessions,
        'total_unique_themes': total_unique_themes,
        'avg_new_per_session': avg_new_per_session,
        'emergence_rate': emergence_rate,
        'saturation_pct': saturation_pct,
        'sessions_since_last_new': metrics[-1]['sessions_since_new'] if metrics else 0,
        'rolling_avg_3session': metrics[-1]['rolling_avg_3session'] if metrics else 0,
        'unique_roles': len(unique_roles),
        'role_list': sorted(unique_roles)
    }

    return metrics, aggregate, role_themes


def write_output_csv(output_file, metrics):
    """Write per-session saturation metrics to CSV."""
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = [
                'Session_Number', 'Date', 'Roles', 'New_Themes_Count',
                'Cumulative_Unique_Themes', 'Sessions_Since_Last_New',
                'Rolling_Avg_3Session'
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for m in metrics:
                writer.writerow({
                    'Session_Number': m['session_number'],
                    'Date': m['date'],
                    'Roles': m['roles'],
                    'New_Themes_Count': m['new_themes_count'],
                    'Cumulative_Unique_Themes': m['cumulative_unique'],
                    'Sessions_Since_Last_New': m['sessions_since_new'],
                    'Rolling_Avg_3Session': f"{m['rolling_avg_3session']:.2f}"
                })
        print(f"Saturation metrics CSV written to: {output_file}")
    except Exception as e:
        print(f"ERROR: Failed to write output CSV: {e}")
        sys.exit(1)


def get_threshold_criteria(threshold):
    """Return saturation criteria for a given threshold level."""
    thresholds = {
        'conservative': {
            'min_sessions': 12,
            'sessions_since_new': 5,
            'rolling_avg_max': 0.2,
            'saturation_pct_min': 90,
            'emergence_rate_max': 5
        },
        'moderate': {
            'min_sessions': 8,
            'sessions_since_new': 3,
            'rolling_avg_max': 1.5,
            'saturation_pct_min': 80,
            'emergence_rate_max': 20
        },
        'aggressive': {
            'min_sessions': 6,
            'sessions_since_new': 2,
            'rolling_avg_max': 3.0,
            'saturation_pct_min': 70,
            'emergence_rate_max': 30
        }
    }
    return thresholds[threshold]


def recommend_action(aggregate, threshold):
    """
    Determine saturation status and recommendation based on metrics and threshold.

    Returns:
        Tuple of (status, rationale)
    """
    criteria = get_threshold_criteria(threshold)

    total_sessions = aggregate['total_sessions']
    rolling_avg = aggregate['rolling_avg_3session']
    saturation_pct = aggregate['saturation_pct']
    sessions_since_new = aggregate['sessions_since_last_new']
    emergence_rate = aggregate['emergence_rate']

    # Count criteria met
    criteria_met = 0
    reasons = []

    if total_sessions >= criteria['min_sessions']:
        criteria_met += 1
        reasons.append(f"✓ Minimum {criteria['min_sessions']} sessions met ({total_sessions} completed)")
    else:
        reasons.append(f"✗ Minimum {criteria['min_sessions']} sessions NOT met ({total_sessions} completed)")

    if sessions_since_new >= criteria['sessions_since_new']:
        criteria_met += 1
        reasons.append(f"✓ {sessions_since_new} sessions without new themes (threshold: {criteria['sessions_since_new']})")
    else:
        reasons.append(f"✗ Only {sessions_since_new} sessions without new themes (threshold: {criteria['sessions_since_new']})")

    if rolling_avg <= criteria['rolling_avg_max']:
        criteria_met += 1
        reasons.append(f"✓ 3-session rolling average {rolling_avg:.2f} below threshold {criteria['rolling_avg_max']}")
    else:
        reasons.append(f"✗ 3-session rolling average {rolling_avg:.2f} above threshold {criteria['rolling_avg_max']}")

    if saturation_pct >= criteria['saturation_pct_min']:
        criteria_met += 1
        reasons.append(f"✓ Saturation {saturation_pct:.1f}% meets threshold ({criteria['saturation_pct_min']}%)")
    else:
        reasons.append(f"✗ Saturation {saturation_pct:.1f}% below threshold ({criteria['saturation_pct_min']}%)")

    if emergence_rate <= criteria['emergence_rate_max']:
        criteria_met += 1
        reasons.append(f"✓ Emergence rate {emergence_rate:.1f}% below threshold ({criteria['emergence_rate_max']}%)")
    else:
        reasons.append(f"✗ Emergence rate {emergence_rate:.1f}% above threshold ({criteria['emergence_rate_max']}%)")

    # Determine status
    if criteria_met >= 4:
        status = "SATURATED"
        recommendation = "Conclude data collection. Proceed to analysis phase."
    elif criteria_met >= 3:
        status = "LIKELY_SATURATED"
        recommendation = "Consider pausing data collection. 1–2 more sessions recommended for confirmation."
    elif criteria_met >= 2:
        status = "APPROACHING_SATURATION"
        recommendation = "Continue data collection. Monitor emergence rate closely."
    else:
        status = "CONTINUE"
        recommendation = "Continue data collection. Significant novelty still emerging."

    return status, recommendation, reasons


def print_summary(aggregate, metrics, threshold, status, recommendation, reasons):
    """Print text summary of saturation analysis."""
    print("\n" + "="*70)
    print("SATURATION ANALYSIS SUMMARY")
    print("="*70)
    print(f"\nDataset Summary:")
    print(f"  Total Sessions: {aggregate['total_sessions']}")
    print(f"  Unique Themes Identified: {aggregate['total_unique_themes']}")
    print(f"  Participant Roles: {aggregate['unique_roles']} ({', '.join(aggregate['role_list'])})")
    print(f"  Threshold Level: {threshold.upper()}")

    print(f"\nKey Metrics:")
    print(f"  Average New Themes per Session: {aggregate['avg_new_per_session']:.2f}")
    print(f"  Sessions Since Last New Theme: {aggregate['sessions_since_last_new']}")
    print(f"  3-Session Rolling Average: {aggregate['rolling_avg_3session']:.2f}")
    print(f"  Saturation Percentage: {aggregate['saturation_pct']:.1f}%")
    print(f"  Emergence Rate: {aggregate['emergence_rate']:.1f}%")

    print(f"\nCriteria Assessment:")
    for reason in reasons:
        print(f"  {reason}")

    print(f"\nRecommendation: {status}")
    print(f"  {recommendation}")

    print("\n" + "="*70)


def main():
    """Main function."""
    args = parse_arguments()

    # Load data
    data = load_theme_data(args.input)

    # Compute metrics
    metrics, aggregate, role_themes = compute_saturation_metrics(data)

    # Write output CSV
    write_output_csv(args.output, metrics)

    # Get recommendation
    status, recommendation, reasons = recommend_action(aggregate, args.threshold)

    # Print summary
    print_summary(aggregate, metrics, args.threshold, status, recommendation, reasons)

    # Return exit code based on status
    if status == "SATURATED":
        return 0
    elif status == "LIKELY_SATURATED":
        return 1
    else:
        return 2


if __name__ == '__main__':
    sys.exit(main())
