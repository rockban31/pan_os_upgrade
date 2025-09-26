# PAN-OS Upgrade Automation (Project Scaffold)

This repository is a scaffold inspired by cdot65/pan-os-upgrade. It provides a ready-to-extend structure for building an automation tool that performs:

- Configuration backups
- Network state snapshots
- Readiness checks
- PAN-OS upgrades for Palo Alto Networks firewalls and Panorama

Key CLI subcommands to implement (placeholders provided):
- firewall: Upgrade a single firewall
- panorama: Upgrade a Panorama appliance
- batch: Upgrade multiple firewalls via Panorama
- inventory: Generate/update inventory.yaml
- settings: Generate/update settings.yaml

Getting started (Python venv):
- py -3.11 -m venv .venv
- .venv\Scripts\Activate.ps1
- pip install -r requirements.txt
- python -m pan_os_upgrade --help

Notes:
- This scaffold pins minimal dependencies. Add/adjust as needed.
- Default behavior should be dry-run when you implement actions.
