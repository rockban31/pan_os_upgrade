# PAN-OS Upgrade Automation Tool

A Python CLI tool for automating Palo Alto Networks firewall and Panorama upgrades with safety checks and configuration backups.

## Features

- Single firewall upgrades
- Panorama appliance upgrades
- Batch operations via Panorama
- Configuration backups
- Network state snapshots
- Dry-run mode (default)

## Project Structure

```
pan_os_upgrade/
├── pan_os_upgrade/          # Main package
│   ├── main.py             # CLI interface
│   ├── components/         # Core components
│   └── models/            # Data models
├── tests/                 # Test suite
├── setup_venv.ps1         # Windows setup script
├── setup_venv.sh          # Linux/Mac setup script
└── requirements.txt       # Dependencies
```

## Prerequisites

- Python 3.11+
- Network access to firewalls/Panorama
- Administrative credentials

## Installation

**Option A: Automated Setup (Recommended)**

```bash
# Windows (PowerShell)
.\setup_venv.ps1

# Linux/Mac
chmod +x setup_venv.sh
./setup_venv.sh
```

**Option B: Manual Setup**

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1
# Activate virtual environment (Linux/Mac)
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

```bash
# View available commands
python -m pan_os_upgrade --help

# Generate configuration templates
python -m pan_os_upgrade inventory
python -m pan_os_upgrade settings

# Upgrade a firewall (dry-run mode)
python -m pan_os_upgrade firewall --host 192.168.1.1 --target-version 10.2.8

# Actual upgrade (disable dry-run)
python -m pan_os_upgrade firewall --host 192.168.1.1 --target-version 10.2.8 --no-dry-run
```

## Commands

| Command | Description |
|---------|-------------|
| `firewall` | Upgrade single firewall |
| `panorama` | Upgrade Panorama appliance |
| `batch` | Batch upgrade via Panorama |
| `inventory` | Generate inventory.yaml template |
| `settings` | Generate settings.yaml template |

## Configuration

Use `inventory.yaml` to define your firewalls and `settings.yaml` to configure tool behavior. Generate templates with:

```bash
python -m pan_os_upgrade inventory
python -m pan_os_upgrade settings
```

## Safety

- **Dry-run mode enabled by default** - no changes unless you use `--no-dry-run`
- Pre-flight readiness checks
- Automatic configuration backups
- Network state snapshots

## Testing

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest tests/
```

## License

Apache License 2.0 - see [LICENSE](LICENSE) file

## Note

⚠️ Always test in dry-run mode first. This tool modifies network infrastructure.
