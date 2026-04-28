#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Guard: require one-time setup before first run
if [ ! -d .venv ]; then
  echo "error: .venv not found — run setup first:" >&2
  echo "" >&2
  echo "  cd $(pwd) && ./setup.sh" >&2
  echo "" >&2
  echo "setup.sh creates the Python environment and a .env stub for HF_TOKEN." >&2
  exit 1
fi

# Load HF_TOKEN from .env if present
if [ -f .env ]; then
  set -a; . ./.env; set +a
fi

if [ -z "${HF_TOKEN:-}" ]; then
  echo "error: HF_TOKEN not set — diarization will not work." >&2
  echo "" >&2
  echo "  1. Accept model terms: https://hf.co/pyannote/speaker-diarization-community-1" >&2
  echo "  2. Get a token:        https://hf.co/settings/tokens" >&2
  echo "  3. Add to .env:        echo 'HF_TOKEN=hf_...' >> $(pwd)/.env" >&2
  exit 1
fi

exec .venv/bin/uvicorn service:app --host 127.0.0.1 --port 8787 --log-level info
