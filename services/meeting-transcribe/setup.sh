#!/usr/bin/env bash
# One-time setup for the meeting-transcribe service.
# Creates a Python venv and installs dependencies. Re-runnable.
set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"

echo "==> Using $($PYTHON --version)"
if [ ! -d .venv ]; then
  echo "==> Creating .venv"
  "$PYTHON" -m venv .venv
fi

echo "==> Upgrading pip"
.venv/bin/pip install --quiet --upgrade pip

echo "==> Installing requirements (this can take 5-10 min on first run)"
.venv/bin/pip install -r requirements.txt

if [ ! -f .env ]; then
  cat > .env <<'EOF'
# Diarization needs a Hugging Face token with terms accepted for
# pyannote/speaker-diarization-community-1. Get one at https://hf.co/settings/tokens
HF_TOKEN=
EOF
  echo "==> Created .env stub. Edit it and set HF_TOKEN before running ./run.sh"
else
  echo "==> .env already exists; leaving as-is"
fi

echo
echo "Done. Next steps:"
echo "  1. (if not already) edit .env and set HF_TOKEN"
echo "  2. accept terms at https://hf.co/pyannote/speaker-diarization-community-1"
echo "  3. ./run.sh"
