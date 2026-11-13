#!/usr/bin/env bash
set -e

BASE_URL="${1:-http://127.0.0.1:8000}"

echo "=================================================="
echo "Running Kane CLI Verification against ${BASE_URL}"
echo "=================================================="

# Check if kane-cli is installed
if ! command -v kane-cli &> /dev/null; then
    echo "[!] kane-cli is not installed in PATH."
    echo "[*] To install: npm install -g @testmuai/kane-cli"
    exit 2
fi

# Check authentication
if ! kane-cli whoami 2>&1 | grep -q "User:"; then
    if kane-cli whoami 2>&1 | grep -q "Not logged in"; then
        echo "[!] Kane CLI is not authenticated."
        echo "[*] Action: Run 'kane-cli login --oauth' and claim credits at https://www.testmuai.com/kane-cli/"
        exit 2
    fi
fi

echo "[*] Executing real Kane CLI run..."
KANE_CLI_USER_AGENT=hermes kane-cli run \
  "Go to ${BASE_URL}, click on Run Mock Invoice Flow (₦12,500), and verify the total shows ₦12,500" \
  --agent \
  --headless \
  --timeout 120
