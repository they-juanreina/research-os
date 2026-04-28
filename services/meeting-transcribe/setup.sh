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

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "error: ffmpeg not found on PATH — required for audio decode." >&2
  echo "  brew install ffmpeg" >&2
  exit 1
fi
echo "==> ffmpeg $(ffmpeg -version 2>&1 | head -1 | awk '{print $3}')"

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
# Diarization needs a Hugging Face token with model terms accepted.
# See setup steps below — paste your token after HF_TOKEN=
HF_TOKEN=
EOF
  chmod 600 .env
  echo "==> Created .env stub (permissions: 600)"
else
  chmod 600 .env
  echo "==> .env already exists; permissions set to 600"
fi

echo
echo "========================================================"
echo " Setup complete. Before running ./run.sh:"
echo "========================================================"
echo
echo " Step 1 — Accept the diarization model terms (one-time):"
echo "   https://hf.co/pyannote/speaker-diarization-community-1"
echo
echo " Step 2 — Create a Hugging Face token (read access is enough):"
echo "   https://hf.co/settings/tokens"
echo
echo " Step 3 — Paste the token into .env:"
echo "   echo 'HF_TOKEN=hf_your_token_here' >> $(pwd)/.env"
echo
echo " Step 4 — Start the service:"
echo "   ./run.sh"
echo "========================================================"
