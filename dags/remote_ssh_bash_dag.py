"""
DAG: run a bash script on a remote server via the Airflow SSH provider.

Remote target (Cloudera cluster host):
  Host:     ccycloud-1.suplab.root.comops.site
  SSH port: 22  (7183 is Cloudera Manager web UI, not SSH)
  Username: root

Prerequisites:
  1. Install dependencies: pip install -r requirements.txt
  2. Copy scripts/remote_hello.sh to the remote host (e.g. /opt/scripts/remote_hello.sh)
  3. Configure the Airflow SSH connection (do not commit passwords to git):
       Option A — UI (Admin -> Connections):
         Conn Id:   ssh_remote_server
         Conn Type: SSH
         Host:      ccycloud-1.suplab.root.comops.site
         Port:      22
         Username:  root
         Password:  <set in UI>
       Option B — local script (export SSH_HOST, SSH_PORT, SSH_USER, SSH_PASSWORD first):
         ./scripts/setup_airflow_ssh_connection.sh
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

REMOTE_SCRIPT_PATH = "/opt/scripts/remote_hello.sh"
SSH_CONN_ID = "ssh_remote_server"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="remote_ssh_bash_script",
    default_args=default_args,
    description="Run a bash script on a remote server using SSHOperator",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["ssh", "remote"],
) as dag:
    run_remote_bash_script = SSHOperator(
        task_id="run_bash_script",
        ssh_conn_id=SSH_CONN_ID,
        command=f"bash {REMOTE_SCRIPT_PATH}",
        cmd_timeout=300,
        get_pty=True,
    )
