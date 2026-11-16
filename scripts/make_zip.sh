#!/usr/bin/env bash
# Zip the committed repo (what you'd hand to someone) into dist/.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
name="peoples-mesh-kit-$(git rev-parse --short HEAD)"
git archive --format=zip --prefix="$name/" -o "dist/$name.zip" HEAD
echo "dist/$name.zip"
