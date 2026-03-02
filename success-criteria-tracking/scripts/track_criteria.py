#!/usr/bin/env python3
"""
Success Criteria Tracking Utility

Computes pass/fail metrics per criterion, aggregates across sessions,
and generates a go/no-go recommendation.

Usage:
    python track_criteria.py --criteria criteria.csv --sessions ./session_results/ --output tracking_matrix.csv

Input Files:
    - criteria.csv: Columns: Criterion_ID,Criterion_Name,Type,Threshold,Must_Have
    - session_results/*.csv: Columns: Criterion_ID,Session_Number,Result,Status

Output:
    - tracking_matrix.csv: Aggregated results with pass rates and confidence
    - summary.txt: Go/no-go recommendation and key findings
"""

import csv
import os
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from statistics import mean, stdev


class CriteriaTracker:
    def __init__(self, criteria_file):
        """Load criteria definitions from CSV."""
        self.criteria = {}
        self.must_haves = set()

        with open(criteria_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                crit_id = row['Criterion_ID'].strip()
                self.criteria[crit_id] = {
                    'name': row['Criterion_Name'].strip(),
                    'type': row['Type'].strip(),  # Q, B, C
                    'threshold': float(row['Threshold']),
                    'must_have': row['Must_Have'].strip().lower() == 'yes'
                }
                if self.criteria[crit_id]['must_have']:
                    self.must_haves.add(crit_id)

    def load_session_results(self, sessions_dir):
        """Load session results from CSV files in directory."""
        self.results = defaultdict(list)  # crit_id -> [results]
        self.sessions = set()

        session_files = sorted(Path(sessions_dir).glob('*.csv'))
        for session_file in session_files:
            with open(session_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    crit_id = row['Criterion_ID'].strip()
                    session_num = int(row['Session_Number'])
                    result = row['Result'].strip()
                    status = row['Status'].strip()  # Pass, Fail, Partial

                    self.results[crit_id].append({
                        'session': session_num,
                        'result': float(result) if result.replace('.', '', 1).isdigit() else result,
                        'status': status
                    })
                    self.sessions.add(session_num)

        self.sessions = sorted(self.sessions)

    def compute_pass_rate(self, crit_id):
        """Compute pass rate for a criterion across sessions."""
        if crit_id not in self.results or len(self.results[crit_id]) == 0:
            return None, 0

        results = self.results[crit_id]
        crit_type = self.criteria[crit_id]['type']

        if crit_type == 'B':  # Behavioral: Y/N or 1/0
            passes = sum(1 for r in results if r['status'].lower() == 'pass')
            return passes / len(results), len(results)
        else:  # Quantitative or Qualitative: numeric or status-based
            passes = sum(1 for r in results if r['status'].lower() == 'pass')
            return passes / len(results), len(results)

    def compute_confidence(self, crit_id):
        """Assess confidence based on sample size and consistency."""
        if crit_id not in self.results:
            return 'Low'

        results = self.results[crit_id]
        n = len(results)

        # Extract numeric results for variance calculation
        numeric_results = []
        for r in results:
            if isinstance(r['result'], (int, float)):
                numeric_results.append(r['result'])

        # Sample size check
        if n < 3:
            return 'Low'
        if n < 5:
            base_confidence = 'Medium'
        else:
            base_confidence = 'High'

        # Consistency check (only if numeric data exists)
        if len(numeric_results) >= 2:
            avg = mean(numeric_results)
            if avg == 0:
                variance_pct = 0
            else:
                variance_pct = (stdev(numeric_results) / avg) * 100 if len(numeric_results) > 1 else 0

            if variance_pct > 30:
                return 'Low'
            if variance_pct > 15 and base_confidence == 'Medium':
                return 'Low'

        return base_confidence

    def compute_trend(self, crit_id):
        """Assess trend: improving, stable, or declining."""
        if crit_id not in self.results or len(self.results[crit_id]) < 3:
            return 'Insufficient data'

        results = sorted(self.results[crit_id], key=lambda r: r['session'])

        # Extract numeric results
        numeric_results = []
        for r in results:
            if isinstance(r['result'], (int, float)):
                numeric_results.append(r['result'])

        if len(numeric_results) < 3:
            return 'Stable'

        # Compare first third vs last third
        split = len(numeric_results) // 3
        early = mean(numeric_results[:split]) if split > 0 else numeric_results[0]
        late = mean(numeric_results[-split:]) if split > 0 else numeric_results[-1]

        change_pct = ((late - early) / early * 100) if early != 0 else 0

        if change_pct > 10:
            return 'Improving'
        elif change_pct < -10:
            return 'Declining'
        else:
            return 'Stable'

    def generate_tracking_matrix(self, output_file):
        """Write tracking matrix to CSV."""
        with open(output_file, 'w', newline='') as f:
            fieldnames = ['Criterion_ID', 'Criterion_Name', 'Type', 'Must_Have', 'Sample_Size']

            # Add per-session columns
            for session in self.sessions:
                fieldnames.append(f'S{session}')

            fieldnames.extend(['Pass_Rate', 'Status', 'Confidence', 'Trend', 'Notes'])

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for crit_id in sorted(self.criteria.keys()):
                row = {
                    'Criterion_ID': crit_id,
                    'Criterion_Name': self.criteria[crit_id]['name'],
                    'Type': self.criteria[crit_id]['type'],
                    'Must_Have': 'Yes' if crit_id in self.must_haves else 'No',
                }

                # Add per-session results
                if crit_id in self.results:
                    result_map = {r['session']: r['status'] for r in self.results[crit_id]}
                    row['Sample_Size'] = len(self.results[crit_id])
                    for session in self.sessions:
                        if session in result_map:
                            row[f'S{session}'] = result_map[session][0]
                else:
                    row['Sample_Size'] = 0

                # Compute aggregates
                pass_rate, sample_size = self.compute_pass_rate(crit_id)
                threshold = self.criteria[crit_id]['threshold']

                if pass_rate is None:
                    row['Pass_Rate'] = 'N/A'
                    row['Status'] = 'Insufficient data'
                else:
                    row['Pass_Rate'] = f'{pass_rate*100:.0f}%'
                    if pass_rate >= threshold:
                        row['Status'] = 'Pass'
                    elif pass_rate >= threshold * 0.75:
                        row['Status'] = 'Partial'
                    else:
                        row['Status'] = 'Fail'

                row['Confidence'] = self.compute_confidence(crit_id)
                row['Trend'] = self.compute_trend(crit_id)
                row['Notes'] = ''

                writer.writerow(row)

    def generate_summary(self, output_file):
        """Generate go/no-go summary and key findings."""
        must_have_results = {}
        nice_to_have_results = {}

        for crit_id in self.criteria.keys():
            pass_rate, sample_size = self.compute_pass_rate(crit_id)
            confidence = self.compute_confidence(crit_id)
            trend = self.compute_trend(crit_id)
            threshold = self.criteria[crit_id]['threshold']

            result = {
                'pass_rate': pass_rate,
                'sample_size': sample_size,
                'confidence': confidence,
                'trend': trend,
                'passes': pass_rate >= threshold if pass_rate is not None else False
            }

            if crit_id in self.must_haves:
                must_have_results[crit_id] = result
            else:
                nice_to_have_results[crit_id] = result

        # Compute recommendation
        recommendation = self._compute_recommendation(must_have_results, nice_to_have_results)

        with open(output_file, 'w') as f:
            f.write('SUCCESS CRITERIA TRACKING SUMMARY\n')
            f.write('=' * 60 + '\n\n')

            f.write('MUST-HAVE CRITERIA\n')
            f.write('-' * 60 + '\n')
            for crit_id in sorted(must_have_results.keys()):
                result = must_have_results[crit_id]
                name = self.criteria[crit_id]['name']
                status = 'PASS' if result['passes'] else 'FAIL'
                f.write(f'{crit_id}: {name}\n')
                f.write(f'  Status: {status} | Confidence: {result["confidence"]} | Trend: {result["trend"]}\n')
                if result['pass_rate'] is not None:
                    f.write(f'  Pass Rate: {result["pass_rate"]*100:.0f}% | Sample Size: {result["sample_size"]}\n')
                f.write('\n')

            f.write('NICE-TO-HAVE CRITERIA\n')
            f.write('-' * 60 + '\n')
            for crit_id in sorted(nice_to_have_results.keys()):
                result = nice_to_have_results[crit_id]
                name = self.criteria[crit_id]['name']
                status = 'PASS' if result['passes'] else 'FAIL'
                f.write(f'{crit_id}: {name}\n')
                f.write(f'  Status: {status} | Confidence: {result["confidence"]} | Trend: {result["trend"]}\n')
                if result['pass_rate'] is not None:
                    f.write(f'  Pass Rate: {result["pass_rate"]*100:.0f}% | Sample Size: {result["sample_size"]}\n')
                f.write('\n')

            f.write('GO/NO-GO RECOMMENDATION\n')
            f.write('=' * 60 + '\n')
            f.write(f'RECOMMENDATION: {recommendation["status"]}\n\n')
            f.write(f'RATIONALE:\n{recommendation["rationale"]}\n\n')
            f.write(f'NEXT STEPS:\n{recommendation["next_steps"]}\n')

    def _compute_recommendation(self, must_haves, nice_to_haves):
        """Compute go/no-go recommendation based on criteria results."""
        must_have_passes = sum(1 for r in must_haves.values() if r['passes'])
        must_have_high_conf = sum(1 for r in must_haves.values() if r['passes'] and r['confidence'] == 'High')
        nice_to_have_passes = sum(1 for r in nice_to_haves.values() if r['passes'])
        must_have_count = len(must_haves)
        nice_to_have_count = len(nice_to_haves)

        declining_must_haves = sum(1 for r in must_haves.values() if r['trend'] == 'Declining')

        if (must_have_passes == must_have_count and
            must_have_high_conf >= must_have_count * 0.8 and
            declining_must_haves == 0 and
            nice_to_have_passes >= nice_to_have_count * 0.5):
            return {
                'status': 'GO',
                'rationale': 'All must-have criteria pass at high confidence. Core objectives met. At least 50% of nice-to-haves pass. Trends are positive or stable.',
                'next_steps': 'Proceed to next phase. Plan to address nice-to-have gaps in iteration.'
            }
        elif (must_have_passes >= must_have_count * 0.8 or
              (must_have_passes == must_have_count and must_have_high_conf < must_have_count * 0.8)):
            return {
                'status': 'CAUTION',
                'rationale': 'Most must-haves pass but confidence or consistency is medium. Some declining trends detected. Investigate and plan mitigation.',
                'next_steps': 'Proceed with caution. Collect 2+ more sessions on high-risk criteria. Plan remediation for gaps in next iteration.'
            }
        else:
            return {
                'status': 'NO-GO',
                'rationale': 'Core must-have criteria fail or are unverified. Fundamental objectives at risk. Design or approach requires revision.',
                'next_steps': 'Do not proceed. Diagnose root causes. Redesign and retest, or redefine criteria and reset expectations.'
            }


def main():
    parser = argparse.ArgumentParser(
        description='Track research success criteria against session outcomes'
    )
    parser.add_argument('--criteria', required=True, help='Path to criteria CSV file')
    parser.add_argument('--sessions', required=True, help='Path to directory of session result CSVs')
    parser.add_argument('--output', default='tracking_matrix.csv', help='Output CSV file for tracking matrix')
    parser.add_argument('--summary', default='summary.txt', help='Output text file for go/no-go summary')

    args = parser.parse_args()

    # Validate inputs
    if not os.path.exists(args.criteria):
        print(f'Error: Criteria file not found: {args.criteria}', file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(args.sessions):
        print(f'Error: Sessions directory not found: {args.sessions}', file=sys.stderr)
        sys.exit(1)

    # Load and process
    tracker = CriteriaTracker(args.criteria)
    tracker.load_session_results(args.sessions)
    tracker.generate_tracking_matrix(args.output)
    tracker.generate_summary(args.summary)

    print(f'Tracking matrix written to: {args.output}')
    print(f'Summary written to: {args.summary}')


if __name__ == '__main__':
    main()
