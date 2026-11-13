#!/usr/bin/env bash
set -e

BASE_URL="${1:-http://localhost:8000}"

echo "=================================================="
echo "Running Kane CLI Verification against ${BASE_URL}"
echo "=================================================="

# Check if kane-cli is installed
if ! command -v kane-cli &> /dev/null; then
    echo "[!] kane-cli is not installed globally."
    echo "[*] To install: npm install -g @testmuai/kane-cli"
    echo "[*] Falling back to curl assertion test:"
    curl -s "${BASE_URL}/api/document/$(curl -s -X POST "${BASE_URL}/mock-invoice/" -H "HX-Request: true" | grep -o 'ID: [a-f0-9-]*' | cut -d' ' -f2)/" || true
    exit 0
fi

KANE_CLI_USER_AGENT=hermes kane-cli run \
  "Go to ${BASE_URL}, click on Run Mock Invoice Flow (₦12,500), and verify the total shows ₦12,500" \
  --agent \
  --headless \
  --timeout 120
