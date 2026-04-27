#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# Load HF_TOKEN from .env if present
if [ -f .env ]; then
  set -a; . ./.env; set +a
fi

if [ -z "${HF_TOKEN:-}" ]; then
  echo "warning: HF_TOKEN not set — diarization will fail on first call." >&2
  echo "Put HF_TOKEN=hf_... in $(pwd)/.env" >&2
fi

exec .venv/bin/uvicorn service:app --host 127.0.0.1 --port 8787 --log-level info
