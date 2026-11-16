#!/usr/bin/env bash
# Build print/peoples-mesh-kit-guide.pdf, print/plain-instructions.pdf and print/handouts.pdf.
# Needs python3 and Google Chrome (or Chromium); set CHROME=/path/to/chrome to override.
set -euo pipefail
cd "$(dirname "$0")/.."
VENV=.build/venv
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" -q install markdown
fi
CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for c in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "$(command -v chromium || true)" "$(command -v google-chrome || true)"; do
    if [ -n "$c" ] && [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
[ -n "$CHROME" ] || { echo "Chrome/Chromium not found; set CHROME=..." >&2; exit 1; }
mkdir -p print
"$VENV/bin/python" scripts/build_print.py .build/html
for name in peoples-mesh-kit-guide plain-instructions handouts; do
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="print/$name.pdf" "file://$PWD/.build/html/$name.html" 2>/dev/null
  echo "print/$name.pdf"
done
