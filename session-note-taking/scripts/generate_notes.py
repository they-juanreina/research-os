#!/usr/bin/env python3
"""
Session Notes Generator

Utility script to pre-fill session notes template from transcript data.
Extracts quoted speech, timestamps, and speaker attributions.

Usage:
    python generate_notes.py --input transcript.md --output session_notes.md
    python generate_notes.py -i my_transcript.txt -o notes.md
"""

import argparse
import re
from pathlib import Path
from datetime import datetime


def extract_quotes(text):
    """
    Extract direct quotes and dialogue from transcript text.

    Patterns matched:
    - "Quoted speech in double quotes"
    - 'Quoted speech in single quotes'
    - Speaker: "quoted dialogue"
    - Speaker said, "quoted dialogue"
    - [HH:MM:SS] Speaker: Quote (with timestamps)
    """
    quotes = []

    # Pattern 1: [HH:MM:SS] Speaker: "Quote"
    timestamp_pattern = r'\[(\d{1,2}:\d{2}:\d{2})\]\s+([^:]+):\s*"([^"]+)"'
    for match in re.finditer(timestamp_pattern, text):
        timestamp, speaker, quote_text = match.groups()
        quotes.append({
            'time': timestamp,
            'speaker': speaker.strip(),
            'quote': quote_text.strip(),
            'context': ''
        })

    # Pattern 2: Speaker: "Quote" (without timestamp)
    speaker_pattern = r'^([A-Za-z0-9\s\.]+):\s*"([^"]+)"'
    for match in re.finditer(speaker_pattern, text, re.MULTILINE):
        speaker, quote_text = match.groups()
        # Only match if it looks like a speaker name (not a URL or common words)
        if len(speaker.split()) <= 3 and not speaker.startswith('http'):
            quotes.append({
                'time': '',
                'speaker': speaker.strip(),
                'quote': quote_text.strip(),
                'context': ''
            })

    # Pattern 3: Free-standing quoted text in double quotes
    quote_pattern = r'"([^"]{10,})"'
    for match in re.finditer(quote_pattern, text):
        quote_text = match.group(1)
        # Skip if already captured by above patterns
        if not any(q['quote'] == quote_text for q in quotes):
            quotes.append({
                'time': '',
                'speaker': 'Unknown',
                'quote': quote_text.strip(),
                'context': ''
            })

    # Deduplicate while preserving order
    seen = set()
    unique_quotes = []
    for q in quotes:
        quote_key = (q['speaker'], q['quote'])
        if quote_key not in seen:
            seen.add(quote_key)
            unique_quotes.append(q)

    return unique_quotes[:10]  # Return top 10 quotes


def extract_timestamps(text):
    """
    Extract all timestamp markers from transcript.
    Patterns: [HH:MM:SS], HH:MM, MM:SS
    """
    timestamps = re.findall(r'\[?(\d{1,2}:?\d{2}:\d{2}|\d{1,2}:\d{2})\]?', text)
    return sorted(set(timestamps))


def load_template():
    """Load the TEMPLATE.md file content."""
    template_path = Path(__file__).parent.parent / 'TEMPLATE.md'
    if template_path.exists():
        return template_path.read_text(encoding='utf-8')
    else:
        return """# Session Notes

[Template file not found. Please ensure TEMPLATE.md exists in the same directory.]
"""


def generate_notes_from_transcript(input_file, output_file):
    """
    Parse transcript and generate pre-filled session notes.
    """
    # Read transcript
    try:
        transcript_text = Path(input_file).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

    # Extract data from transcript
    quotes = extract_quotes(transcript_text)
    timestamps = extract_timestamps(transcript_text)

    # Load template
    template = load_template()

    # Build quotes table
    quotes_table = "| Time | Participant | Quote | Context |\n|---|---|---|---|\n"
    for quote in quotes:
        time_str = quote['time'] if quote['time'] else ''
        speaker_str = quote['speaker'] if quote['speaker'] != 'Unknown' else 'P1'
        quotes_table += f"| {time_str} | {speaker_str} | \"{quote['quote']}\" | |\n"

    # Insert extracted quotes into template
    notes = template.replace(
        "| Time | Participant | Quote | Context |",
        "| Time | Participant | Quote | Context |"
    )

    # If template has a placeholder section for Key Quotes, replace it
    if "## Key Quotes" in notes:
        # Find the Key Quotes section and replace the table
        pattern = r'(## Key Quotes\n\n)(.*?)(\n---\n|## [A-Z])'
        def replace_quotes_section(match):
            return match.group(1) + quotes_table + match.group(3)
        notes = re.sub(pattern, replace_quotes_section, notes, flags=re.DOTALL)

    # Add metadata comment
    metadata = f"""---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Source Transcript: {input_file}
Extracted Quotes: {len(quotes)}
Timestamps Found: {len(timestamps)}
---

"""
    notes = metadata + notes

    # Write output
    try:
        Path(output_file).write_text(notes, encoding='utf-8')
        print(f"✓ Session notes generated: {output_file}")
        print(f"  - Extracted {len(quotes)} quotes")
        print(f"  - Found {len(timestamps)} timestamps")
    except Exception as e:
        print(f"Error writing output file: {e}")
        exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate pre-filled session notes from a research transcript.',
        epilog='Example: python generate_notes.py --input transcript.md --output notes.md'
    )

    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to input transcript file (plain text or markdown)'
    )

    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Path to output session notes file'
    )

    args = parser.parse_args()

    # Validate input file exists
    if not Path(args.input).exists():
        print(f"Error: Input file '{args.input}' does not exist.")
        exit(1)

    # Generate notes
    generate_notes_from_transcript(args.input, args.output)


if __name__ == '__main__':
    main()
