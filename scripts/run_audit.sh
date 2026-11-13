#!/usr/bin/env bash
set -e

echo "Running security vulnerability audit via pip-audit..."
if [ -f ".venv/bin/pip-audit" ]; then
    .venv/bin/pip-audit
else
    pip-audit
fi
echo "Audit complete: No known vulnerabilities."
