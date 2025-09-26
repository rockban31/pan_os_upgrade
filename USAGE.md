# Usage Guide

This guide explains what the tool does, why it's needed, and how to execute it safely in your environment.

## Why this tool exists

Upgrading PAN-OS on Palo Alto Networks firewalls and Panorama can be complex and risky, especially at scale. This tool aims to:
- Standardize and automate the upgrade workflow
- Reduce risk via dry-run simulation and pre-flight checks
- Capture pre/post snapshots and backups for auditability
- Support batch operations across many devices
- Provide consistent reporting and logging

## Key Concepts

- Dry-run: Default mode that shows what would happen without making changes
- Inventory: A YAML file listing devices to target
- Settings: A YAML file controlling concurrency, retries, snapshots, etc.
- Snapshots: Before/after state captures for verification and reporting
- Backups: Pre/post configuration backups for rollback and auditing

## CLI Overview

Invoke the CLI either as a module or via the console script:

```bash
# Module form (always available)
python -m pan_os_upgrade --help

# If installed as a package in the future
pan-os-upgrade --help
```

## Prepare Your Environment

1) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# Linux/Mac
source .venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Generate templates and edit them
```bash
python -m pan_os_upgrade inventory
python -m pan_os_upgrade settings

# Edit inventory.yaml and settings.yaml with your values
```

## Commands and Examples

### Single Firewall Upgrade (safe by default)

```bash
python -m pan_os_upgrade firewall \
  --host 192.168.1.10 \
  --username admin \
  --target-version 10.2.8
```

- Prompts for password securely
- Runs in dry-run mode by default
- Prints planned actions (download, install, reboot) without changing the device

Run a real upgrade by disabling dry-run explicitly:
```bash
python -m pan_os_upgrade firewall \
  --host 192.168.1.10 \
  --username admin \
  --target-version 10.2.8 \
  --no-dry-run
```

### Panorama Operations (scaffold)

```bash
python -m pan_os_upgrade panorama \
  --host panorama.company.com \
  --username admin
```

- Placeholder implementation prints intended Panorama workflow

### Batch Upgrades via Panorama

```bash
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3
```

- Dry-run by default
- Targets devices defined/managed by Panorama (implementation TBD)

### Generate Templates

```bash
# Inventory template (will not overwrite existing file)
python -m pan_os_upgrade inventory --path inventory.yaml

# Settings template (will not overwrite existing file)
python -m pan_os_upgrade settings --path settings.yaml
```

## Environment Variables for Secrets (Recommended)

Avoid passing credentials inline. Use environment variables instead.

```powershell
# PowerShell (Windows)
$env:PAN_USERNAME = "admin"
$env:PAN_PASSWORD = "your-secure-password"
```

```bash
# Bash (Linux/Mac)
export PAN_USERNAME="admin"
export PAN_PASSWORD="your-secure-password"
```

Then reference them at runtime (the tool currently prompts, but this is a pattern to adopt when implemented):
```bash
python -m pan_os_upgrade firewall --host 192.168.1.10 --username $PAN_USERNAME
```

## Logging and Outputs

- Logs: Written to console; future enhancements may include file logging
- Backups: Stored in configurable directories (settings.yaml)
- Reports: PDF diffs or snapshot reports when implemented

## Best Practices

1. Always run a dry-run first
2. Start with a single test firewall
3. Back up configurations and verify snapshots
4. Plan maintenance windows and communicate with stakeholders
5. Monitor devices during and after upgrade

## Troubleshooting

- Authentication failures: verify username/password and role permissions
- Connectivity issues: test ping/HTTPS to the device
- Insufficient disk space: adjust readiness checks and free space on device
- HA pairs: ensure passive member readiness and sync behavior

For additional details, see:
- README.md for overview
- INSTALLATION.md for setup
- ARCHITECTURE.md for component breakdown (coming soon)