#!/usr/bin/env bash
# One-time setup for the meeting-transcribe service.
# Creates a Python venv and installs dependencies. Re-runnable.
set -euo pipefail
cd "$(dirname "$0")"

# Find a Python 3.11+ interpreter. WhisperX and many of the ML deps require >=3.10.
find_python() {
  if [ -n "${PYTHON:-}" ]; then echo "$PYTHON"; return; fi
  for cand in python3.13 python3.12 python3.11 python3; do
    if command -v "$cand" >/dev/null 2>&1; then
      ver=$("$cand" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
      major=${ver%.*}; minor=${ver#*.}
      if [ "$major" -ge 3 ] && [ "$minor" -ge 11 ]; then
        echo "$cand"; return
      fi
    fi
  done
  return 1
}

PYTHON="$(find_python || true)"
if [ -z "$PYTHON" ]; then
  echo "error: need Python 3.11+ on PATH (try: brew install python@3.11)" >&2
  exit 1
fi

echo "==> Using $($PYTHON --version) at $(command -v "$PYTHON")"
if [ -d .venv ]; then
  existing=$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || echo "?")
  if [ "$existing" != "?" ]; then
    existing_major=${existing%.*}; existing_minor=${existing#*.}
    if [ "$existing_major" -lt 3 ] || [ "$existing_minor" -lt 11 ]; then
      echo "==> Existing .venv uses Python $existing — recreating with $PYTHON"
      rm -rf .venv
    fi
  fi
fi
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
