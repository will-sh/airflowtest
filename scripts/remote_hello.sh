#!/usr/bin/env bash
set -euo pipefail

echo "Hello from remote server: $(hostname)"
echo "Current time: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "Script finished successfully."
