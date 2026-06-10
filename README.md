# airflowtest

Airflow DAG that runs a bash script on a remote server via SSH.

## Setup

### 1. Create a CDE Airflow job

Create a CDE Airflow job using `remote_ssh_bash_dag.py`.

### 2. Deploy the remote script

```bash
scp scripts/remote_hello.sh root@ccycloud-1.suplab.root.comops.site:/opt/scripts/remote_hello.sh
ssh root@ccycloud-1.suplab.root.comops.site "chmod +x /opt/scripts/remote_hello.sh"
```

### 3. Configure SSH connection

Create an Airflow connection with Conn Id `ssh_remote_server`:

| Field | Value |
|-------|-------|
| Conn Type | SSH |
| Host | `ccycloud-1.suplab.root.comops.site` |
| Port | `22` |
| Username | `root` |
| Password | your SSH password |

## Test

### 1. Trigger the CDE Airflow job

### 2. Check the task log

Open the `run_bash_script` task log. Success looks like:

```
Hello from remote server: <hostname>
Current time: 2026-06-10T10:30:00Z
Script finished successfully.
```
