# Installation Guide

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.11 or higher
- **Operating System**: Windows 10+, macOS 10.14+, Ubuntu 18.04+, RHEL 8+
- **Memory**: 2GB RAM minimum, 4GB recommended
- **Disk Space**: 1GB for installation, additional space for backups and logs
- **Network**: Connectivity to target firewalls and Panorama appliances

### Recommended Requirements
- **Python**: 3.12 (latest stable)
- **Memory**: 8GB RAM for concurrent operations
- **Disk Space**: 10GB+ for enterprise deployments
- **Network**: Dedicated management network access

## 🖥️ Operating System Specific Installation

### Windows Installation

#### Option 1: Using Git (Recommended)
```powershell
# Install Git if not already installed
winget install --id Git.Git -e --source winget

# Clone the repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m pan_os_upgrade --help
```

#### Option 2: Download ZIP
```powershell
# Download and extract ZIP from GitHub
# Navigate to extracted folder

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### Windows Troubleshooting
- **PowerShell Execution Policy**: Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **Python not found**: Install Python from [python.org](https://python.org) and add to PATH
- **Git not found**: Install Git from [git-scm.com](https://git-scm.com)

### Linux Installation (Ubuntu/Debian)

```bash
# Update package manager
sudo apt update

# Install Python 3.11+ and pip
sudo apt install python3.11 python3.11-venv python3-pip git -y

# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python3.11 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m pan_os_upgrade --help
```

### Linux Installation (RHEL/CentOS/Fedora)

```bash
# For RHEL/CentOS 8+
sudo dnf install python3.11 python3-pip git -y

# For older versions or if python3.11 not available
sudo dnf install python3 python3-pip git -y

# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### macOS Installation

#### Option 1: Using Homebrew (Recommended)
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11+
brew install python@3.11 git

# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python3.11 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using System Python
```bash
# Ensure you have Python 3.11+ installed
python3 --version

# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🐳 Docker Installation

### Using Pre-built Image (Coming Soon)
```bash
# Pull the image
docker pull rockban31/pan_os_upgrade:latest

# Run with volume mounts for configuration
docker run -it --rm \
  -v $(pwd)/config:/app/config \
  -v $(pwd)/backups:/app/backups \
  rockban31/pan_os_upgrade:latest --help
```

### Building from Source
```bash
# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Build Docker image
docker build -t pan_os_upgrade:local .

# Run container
docker run -it --rm \
  -v $(pwd)/inventory.yaml:/app/inventory.yaml \
  -v $(pwd)/settings.yaml:/app/settings.yaml \
  pan_os_upgrade:local --help
```

## 📦 Package Manager Installation (Future)

### PyPI Installation (Planned)
```bash
# Install from PyPI (when available)
pip install pan-os-upgrade

# Verify installation
pan-os-upgrade --help
```

### Conda Installation (Planned)
```bash
# Install from conda-forge (when available)
conda install -c conda-forge pan-os-upgrade
```

## ⚙️ Post-Installation Configuration

### 1. Generate Configuration Files
```bash
# Activate virtual environment first
# Windows: .venv\Scripts\Activate.ps1
# Linux/Mac: source .venv/bin/activate

# Generate inventory template
python -m pan_os_upgrade inventory

# Generate settings template
python -m pan_os_upgrade settings
```

### 2. Edit Configuration Files

#### Edit `inventory.yaml`:
```yaml
firewalls:
  - hostname: your-firewall.company.com
    ip: 192.168.1.100
    username: admin
    model: PA-3220
    current_version: "10.1.4"
    ha_mode: disabled
```

#### Edit `settings.yaml`:
```yaml
# Customize for your environment
dry_run_default: true  # Keep true for safety
retry_count: 3
concurrency: 2  # Start with lower concurrency
```

### 3. Test Installation
```bash
# Test CLI access
python -m pan_os_upgrade --help

# Test configuration generation
python -m pan_os_upgrade inventory --path test-inventory.yaml
python -m pan_os_upgrade settings --path test-settings.yaml

# Clean up test files
rm test-inventory.yaml test-settings.yaml
```

## 🔍 Verification & Troubleshooting

### Verify Python Version
```bash
python --version  # Should be 3.11+
```

### Check Dependencies
```bash
pip list | grep -E "(click|colorama|pyyaml)"
```

### Test Network Connectivity
```bash
# Test connectivity to your firewalls
ping your-firewall-ip
telnet your-firewall-ip 443
```

### Common Issues and Solutions

#### Issue: "Python not found"
**Solution**: 
- Windows: Install Python from python.org and add to PATH
- Linux: `sudo apt install python3` or `sudo dnf install python3`
- macOS: `brew install python@3.11`

#### Issue: "Permission denied" on virtual environment activation
**Solution**:
- Windows: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Linux/Mac: `chmod +x .venv/bin/activate`

#### Issue: "pip install fails with SSL errors"
**Solution**:
```bash
# Upgrade pip and certificates
python -m pip install --upgrade pip
pip install --upgrade certifi
```

#### Issue: "Module not found" when running tool
**Solution**:
```bash
# Ensure virtual environment is activated
# Windows: .venv\Scripts\Activate.ps1
# Linux/Mac: source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: "Git clone fails"
**Solution**:
```bash
# Use HTTPS instead of SSH
git clone https://github.com/rockban31/pan_os_upgrade.git

# Or download ZIP from GitHub
```

## 🌐 Enterprise Deployment

### Centralized Installation
```bash
# Install to shared location
sudo mkdir /opt/pan_os_upgrade
sudo chown $USER:$USER /opt/pan_os_upgrade
cd /opt/pan_os_upgrade

# Clone and install
git clone https://github.com/rockban31/pan_os_upgrade.git .
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Create wrapper script
sudo tee /usr/local/bin/pan-os-upgrade << 'EOF'
#!/bin/bash
cd /opt/pan_os_upgrade
source .venv/bin/activate
python -m pan_os_upgrade "$@"
EOF

sudo chmod +x /usr/local/bin/pan-os-upgrade
```

### Configuration Management
```bash
# Centralized config directory
sudo mkdir -p /etc/pan_os_upgrade
sudo cp inventory.yaml.example /etc/pan_os_upgrade/inventory.yaml
sudo cp settings.yaml.example /etc/pan_os_upgrade/settings.yaml

# Edit configs as needed
sudo nano /etc/pan_os_upgrade/inventory.yaml
sudo nano /etc/pan_os_upgrade/settings.yaml
```

## 🔄 Updating the Tool

### Update from Git
```bash
# Navigate to installation directory
cd pan_os_upgrade

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\Activate.ps1  # Windows

# Pull latest changes
git pull origin master

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Clean Reinstall
```bash
# Remove old installation
rm -rf pan_os_upgrade

# Fresh clone and install
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🔐 Security Considerations

### File Permissions
```bash
# Secure configuration files (Linux/Mac)
chmod 600 inventory.yaml settings.yaml
chmod 700 .venv/

# Windows: Use file properties to restrict access
```

### Environment Variables
```bash
# Set sensitive variables
export PAN_USERNAME="admin"
export PAN_PASSWORD="secure_password"

# Use in commands
python -m pan_os_upgrade firewall --host 192.168.1.1 --username $PAN_USERNAME
```

### Firewall Access
- Create dedicated service account with minimal privileges
- Use certificate-based authentication when possible
- Restrict management network access
- Enable audit logging

---

**Next Steps**: After successful installation, proceed to [USAGE.md](USAGE.md) for detailed usage instructions.