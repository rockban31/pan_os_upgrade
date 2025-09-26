# PAN-OS Upgrade Examples

This directory contains practical examples demonstrating how to use the PAN-OS Upgrade Automation tool in various scenarios.

## 📚 Available Examples

### [Single Firewall Upgrade](single_firewall_upgrade.md)
Complete walkthrough of upgrading a standalone firewall:
- **Scenario**: PA-3220 standalone firewall
- **Version**: 10.1.4 → 10.2.8
- **Duration**: ~1-2 hours
- **Complexity**: Beginner
- **Use Case**: Branch office, single device upgrades

**Key Learning Points:**
- Basic CLI usage and options
- Dry-run mode for safety
- Configuration backup and restore
- Pre/post upgrade validation
- Troubleshooting common issues

### [Batch Upgrade via Panorama](batch_panorama_upgrade.md)
Large-scale upgrade of multiple firewalls through Panorama:
- **Scenario**: 15 branch office firewalls
- **Version**: Mixed 10.1.x → 11.0.3
- **Duration**: 4-6 hours (phased approach)
- **Complexity**: Advanced
- **Use Case**: Enterprise deployment, multiple locations

**Key Learning Points:**
- Phased rollout strategies
- Concurrent upgrade management
- Progress monitoring and reporting
- Error handling and recovery
- Batch operation best practices

## 🎯 Choosing the Right Example

| Scenario | Recommended Example | Why |
|----------|-------------------|-----|
| First-time user | Single Firewall Upgrade | Learn basics safely |
| Single device upgrade | Single Firewall Upgrade | Direct applicable steps |
| Multiple devices (2-5) | Single Firewall Upgrade | Apply sequentially |
| Large deployment (6+) | Batch Panorama Upgrade | Efficient bulk operations |
| HA pairs | *(Coming Soon)* | Specialized HA handling |
| Mixed versions | Batch Panorama Upgrade | Handles version diversity |
| Time-sensitive | Batch Panorama Upgrade | Parallel processing |

## 🚀 Quick Start Guide

### For Beginners
1. Start with [Single Firewall Upgrade](single_firewall_upgrade.md)
2. Use a test firewall in a lab environment
3. Always run in dry-run mode first
4. Follow the step-by-step instructions exactly
5. Understand each phase before proceeding

### For Experienced Users
1. Review [Batch Panorama Upgrade](batch_panorama_upgrade.md)
2. Adapt configuration files to your environment
3. Plan phased rollout strategy
4. Set up monitoring and alerting
5. Prepare rollback procedures

## 📋 Prerequisites for All Examples

### Environment Setup
```bash
# Clone repository
git clone https://github.com/rockban31/pan_os_upgrade.git
cd pan_os_upgrade

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Network Requirements
- Management network connectivity to target devices
- HTTPS (443) access to firewalls and Panorama
- Sufficient bandwidth for PAN-OS image downloads
- DNS resolution for device hostnames

### Credentials and Permissions
- Administrative credentials for target devices
- API access enabled on firewalls/Panorama
- Sufficient privileges for configuration changes
- Backup storage location access

## 📊 Example Comparison

| Feature | Single Firewall | Batch Panorama |
|---------|-----------------|----------------|
| **Devices** | 1 | Multiple (typically 5-50) |
| **Complexity** | Low | High |
| **Duration** | 1-2 hours | 4-8 hours |
| **Downtime** | 5-10 minutes | 5-10 min per device |
| **Monitoring** | Manual | Automated |
| **Rollback** | Manual | Automated options |
| **Reporting** | Basic | Comprehensive |
| **Concurrency** | N/A | 3-10 simultaneous |

## 🛡️ Safety Guidelines

### Always Follow These Steps
1. **Test in Lab First**: Never run directly in production
2. **Use Dry-Run Mode**: Verify actions before execution
3. **Backup Everything**: Configuration, settings, documentation
4. **Plan Rollback**: Have reversion procedures ready
5. **Monitor Closely**: Watch for issues during upgrade
6. **Validate Results**: Confirm successful completion

### Risk Mitigation
- **Maintenance Windows**: Schedule during low-usage periods
- **Communication Plan**: Notify stakeholders of activities
- **Emergency Contacts**: Have support resources available
- **Console Access**: Ensure out-of-band management available
- **Documentation**: Keep detailed records of all changes

## 🔧 Customization Tips

### Adapting Examples to Your Environment

#### Network Addresses
```yaml
# Update inventory.yaml with your networks
firewalls:
  - hostname: your-firewall.company.com
    ip: 10.1.1.100  # Your management IP
    username: admin  # Your admin username
```

#### Timing and Concurrency
```yaml
# Update settings.yaml for your requirements
concurrency: 2  # Start conservative
retry_count: 5  # Increase for unstable networks
post_reboot_wait_seconds: 600  # Adjust for device speed
```

#### Backup Locations
```yaml
# Ensure backup paths exist and have space
backup_location: "/path/to/your/backups"  # Unix/Linux
backup_location: "C:\\backups"            # Windows
```

## 📈 Performance Expectations

### Single Firewall Upgrade Timeline
```
Pre-flight checks:     5-10 minutes
Configuration backup:  2-5 minutes
PAN-OS download:      10-30 minutes (depends on connection)
Installation:         15-30 minutes
Reboot and startup:   5-15 minutes
Post-verification:    5-10 minutes
Total:               42-100 minutes
```

### Batch Upgrade Scaling
| Devices | Concurrent | Total Time | Efficiency |
|---------|------------|------------|------------|
| 5 | 3 | 2-3 hours | High |
| 10 | 5 | 3-4 hours | High |
| 20 | 5 | 5-7 hours | Medium |
| 50 | 10 | 8-12 hours | Medium |

## 🆘 Getting Help

### If Examples Don't Work
1. **Check Prerequisites**: Ensure all requirements are met
2. **Review Logs**: Look for error messages and clues
3. **Try Dry-Run**: Verify configuration without changes
4. **Start Simple**: Begin with single device before batch
5. **Seek Support**: Use GitHub Issues for assistance

### Common Issues and Solutions

#### "Connection Failed"
- Verify network connectivity (`ping`, `telnet`)
- Check firewall management settings
- Confirm credentials and permissions

#### "Insufficient Disk Space"
- Clear temporary files on device
- Check available storage requirements
- Consider smaller concurrent operations

#### "Download Failed"
- Verify internet connectivity from firewall
- Check DNS resolution
- Try manual download to test

## 🔄 Contributing Examples

Have a unique use case or improvement? We welcome contributions!

### Example Contributions Should Include:
- Clear scenario description
- Step-by-step instructions
- Expected outputs and timelines
- Troubleshooting section
- Configuration file samples
- Lessons learned and best practices

### Submission Process:
1. Fork the repository
2. Create your example in `examples/`
3. Test thoroughly in lab environment
4. Submit pull request with clear description
5. Include any supporting files or screenshots

---

**⚠️ Important Reminder**: All examples are for educational purposes. Always test thoroughly in a lab environment before using in production. The default dry-run mode is your safety net!