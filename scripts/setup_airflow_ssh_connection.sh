#!/usr/bin/env bash
# Create or update the Airflow SSH connection from environment variables.
#
# Usage:
#   export SSH_HOST=ccycloud-1.suplab.root.comops.site
#   export SSH_PORT=22
#   export SSH_USER=root
#   export SSH_PASSWORD='your-password'
#   ./scripts/setup_airflow_ssh_connection.sh

set -euo pipefail

: "${SSH_HOST:?SSH_HOST is required}"
: "${SSH_PORT:?SSH_PORT is required}"
: "${SSH_USER:?SSH_USER is required}"
: "${SSH_PASSWORD:?SSH_PASSWORD is required}"

CONN_ID="ssh_remote_server"

airflow connections delete "${CONN_ID}" 2>/dev/null || true
airflow connections add "${CONN_ID}" \
  --conn-type ssh \
  --conn-host "${SSH_HOST}" \
  --conn-port "${SSH_PORT}" \
  --conn-login "${SSH_USER}" \
  --conn-password "${SSH_PASSWORD}"

echo "Airflow connection '${CONN_ID}' configured for ${SSH_USER}@${SSH_HOST}:${SSH_PORT}"
