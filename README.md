# PAN-OS Upgrade Automation Tool

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Issues](https://img.shields.io/github/issues/rockban31/pan_os_upgrade)](https://github.com/rockban31/pan_os_upgrade/issues)

A comprehensive automation solution for upgrading Palo Alto Networks firewalls and Panorama appliances. This tool streamlines the complex process of PAN-OS upgrades by providing automated configuration backups, readiness checks, network state snapshots, and safe upgrade procedures.

## 🚀 Features

### Core Capabilities
- **🔥 Single Firewall Upgrades**: Upgrade individual firewalls with comprehensive safety checks
- **🏢 Panorama Management**: Upgrade Panorama appliances and manage connected firewalls
- **📦 Batch Operations**: Upgrade multiple firewalls simultaneously via Panorama
- **💾 Configuration Backups**: Automatic backup before and after upgrades
- **📊 Network State Snapshots**: Before/after comparison with PDF reporting
- **✅ Readiness Checks**: Pre-upgrade validation (storage, connectivity, HA status)

### Safety & Reliability
- **🛡️ Dry-Run Mode**: Default safe mode - no changes until explicitly disabled
- **🔄 HA Support**: Handles High Availability pairs correctly
- **⚡ Retry Logic**: Configurable retry mechanisms for network operations
- **📝 Comprehensive Logging**: Detailed logs for troubleshooting and auditing

### Enterprise Features
- **⚙️ Flexible Configuration**: YAML-based inventory and settings management
- **📈 Concurrent Operations**: Parallel processing for multiple devices
- **🎯 Selective Upgrades**: Target specific devices or groups
- **📊 Detailed Reporting**: Progress tracking and completion reports

## 🏗️ Architecture

This tool is built with a modular architecture:

```
pan_os_upgrade/
├── main.py              # CLI interface and command routing
├── components/          # Core upgrade components
│   ├── firewall.py      # Single firewall operations
│   └── snapshots.py     # Network state capture
├── models/              # Data models and configuration
│   └── config.py        # Configuration management
└── __init__.py         # Package initialization
```

## 📋 Prerequisites

- **Python**: 3.11 or higher
- **Network Access**: Connectivity to target firewalls/Panorama
- **Credentials**: Administrative access to devices
- **Storage**: Sufficient disk space for backups and logs

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\Activate.ps1
# Activate virtual environment (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate Configuration Files

```bash
# Generate inventory template
python -m pan_os_upgrade inventory

# Generate settings template
python -m pan_os_upgrade settings
```

### 3. Configure Your Environment

Edit the generated `inventory.yaml` and `settings.yaml` files to match your environment.

### 4. Run Your First Upgrade (Dry-Run)

```bash
# Upgrade a single firewall (dry-run mode - safe)
python -m pan_os_upgrade firewall --host 192.168.1.1 --target-version 10.2.8

# Check what the tool will do without making changes
python -m pan_os_upgrade batch --panorama-host panorama.example.com --target-version 10.2.8
```

## 📖 Detailed Usage

### Command Overview

| Command | Purpose | Example |
|---------|---------|----------|
| `firewall` | Upgrade single firewall | `--host fw1.local --target-version 10.2.8` |
| `panorama` | Upgrade Panorama appliance | `--host panorama.local` |
| `batch` | Upgrade multiple via Panorama | `--panorama-host panorama.local --target-version 10.2.8` |
| `inventory` | Generate inventory template | Creates `inventory.yaml` |
| `settings` | Generate settings template | Creates `settings.yaml` |

### Single Firewall Upgrade

```bash
# Basic upgrade (dry-run mode)
python -m pan_os_upgrade firewall \
  --host 192.168.1.10 \
  --username admin \
  --target-version 10.2.8

# Actual upgrade (disable dry-run)
python -m pan_os_upgrade firewall \
  --host 192.168.1.10 \
  --username admin \
  --target-version 10.2.8 \
  --no-dry-run
```

### Batch Upgrade via Panorama

```bash
# Upgrade all firewalls managed by Panorama
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3 \
  --no-dry-run
```

## ⚙️ Configuration

### Inventory Management

The `inventory.yaml` file defines your firewall infrastructure:

```yaml
firewalls:
  - hostname: fw-primary.company.com
    ip: 192.168.1.10
    username: admin
    model: PA-3220
    current_version: "10.1.4"
    ha_mode: active
    
  - hostname: fw-secondary.company.com
    ip: 192.168.1.11
    username: admin
    model: PA-3220
    current_version: "10.1.4"
    ha_mode: passive
```

### Settings Configuration

The `settings.yaml` file controls tool behavior:

```yaml
# Safety settings
dry_run_default: true
retry_count: 3
retry_delay_seconds: 15

# Performance settings
concurrency: 5
max_workers: 10

# Feature toggles
pre_post_snapshots: true
generate_pdf_diff: true
backup_config: true
```

## 🛡️ Safety Features

### Dry-Run Mode (Default)
- **Always enabled by default** - protects against accidental changes
- Shows exactly what actions would be performed
- Must be explicitly disabled with `--no-dry-run`

### Pre-Flight Checks
- Storage space validation
- Network connectivity verification
- HA status confirmation
- Current version validation

### Backup & Recovery
- Automatic configuration backups
- Network state snapshots
- Rollback capabilities
- Audit trails

## 🔧 Development

### Project Structure

```
pan_os_upgrade/
├── pan_os_upgrade/          # Main package
│   ├── main.py             # CLI interface
│   ├── components/         # Core components
│   └── models/            # Data models
├── tests/                 # Test suite
├── docs/                  # Documentation
├── docker/                # Container support
├── .github/               # CI/CD workflows
└── examples/              # Usage examples
```

### Running Tests

```bash
# Install development dependencies
pip install pytest black

# Run tests
pytest tests/

# Format code
black pan_os_upgrade/
```

## 🚨 Important Notes

### ⚠️ Limitations
- Not tested in all deployment architectures
- Active-active clustering support is limited
- Log collector compatibility varies

### 🔐 Security Considerations
- Store credentials securely (environment variables, key managers)
- Use least-privilege accounts when possible
- Review all actions in dry-run mode first
- Maintain backup and rollback procedures

### 📋 Best Practices
1. **Always test in dry-run mode first**
2. **Validate inventory and settings files**
3. **Perform upgrades during maintenance windows**
4. **Monitor device status throughout the process**
5. **Keep configuration backups accessible**

## 🆘 Support & Troubleshooting

### Common Issues

- **Connection timeouts**: Check firewall/Panorama accessibility
- **Authentication failures**: Verify credentials and permissions
- **Storage issues**: Ensure sufficient disk space on devices
- **HA synchronization**: Allow extra time for HA operations

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/rockban31/pan_os_upgrade/issues)
- **Discussions**: [GitHub Discussions](https://github.com/rockban31/pan_os_upgrade/discussions)
- **Documentation**: Check the `docs/` directory

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by [cdot65/pan-os-upgrade](https://github.com/cdot65/pan-os-upgrade)
- Palo Alto Networks community
- Contributors and testers

---

**⚠️ IMPORTANT**: This tool performs critical network infrastructure changes. Always test thoroughly in a non-production environment before using in production. The default dry-run mode is your safety net - use it!
