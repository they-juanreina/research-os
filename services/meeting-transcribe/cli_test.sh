#!/usr/bin/env bash
# Usage: ./cli_test.sh path/to/audio.{wav,mp3,m4a,mp4} [language]
set -euo pipefail
AUDIO="${1:?usage: $0 path/to/audio [language]}"
LANG="${2:-}"

ARGS=(-F "audio=@${AUDIO}")
[ -n "$LANG" ] && ARGS+=(-F "language=${LANG}")

curl -sS --fail-with-body http://127.0.0.1:8787/transcribe "${ARGS[@]}" | \
  tee /tmp/transcribe-last.json | \
  python3 -c "
import json, sys
data = json.load(sys.stdin)
print()
print(f\"language: {data['language']}  speakers: {', '.join(data['speakers'])}\")
print('─' * 60)
for seg in data['segments']:
    mm, ss = divmod(int(seg['start']), 60)
    print(f'[{mm:02d}:{ss:02d}] {seg[\"speaker\"]}: {seg[\"text\"]}')
"
echo
echo "Full JSON: /tmp/transcribe-last.json"
