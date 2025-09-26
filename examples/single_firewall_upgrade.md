# Single Firewall Upgrade Example

This example demonstrates upgrading a single Palo Alto Networks firewall from PAN-OS 10.1.4 to 10.2.8.

## Scenario
- **Device**: PA-3220 at 192.168.1.100
- **Current Version**: 10.1.4
- **Target Version**: 10.2.8
- **HA Status**: Standalone (not in HA pair)
- **Maintenance Window**: 2-hour window available

## Pre-Upgrade Preparation

### 1. Verify Current State
```bash
# Test connectivity
ping 192.168.1.100

# Test HTTPS management access
curl -k https://192.168.1.100 -I
```

### 2. Generate and Configure Templates
```bash
# Generate configuration templates
python -m pan_os_upgrade inventory --path single-fw-inventory.yaml
python -m pan_os_upgrade settings --path single-fw-settings.yaml
```

### 3. Edit Inventory File
```yaml
# single-fw-inventory.yaml
firewalls:
  - hostname: fw-branch-01.company.com
    ip: 192.168.1.100
    username: admin
    model: PA-3220
    current_version: "10.1.4"
    ha_mode: disabled
```

### 4. Edit Settings File
```yaml
# single-fw-settings.yaml
# Conservative settings for single firewall
dry_run_default: true
retry_count: 3
retry_delay_seconds: 15

# Enable all safety features
pre_post_snapshots: true
generate_pdf_diff: true
backup_config: true

# Single firewall = no concurrency needed
concurrency: 1

# Timeouts appropriate for PA-3220
connection_timeout_seconds: 60
post_reboot_wait_seconds: 300

# Backup configuration
backup_location: "./backups"
backup_retention_days: 30

# Logging
log_level: "INFO"
log_to_file: true
log_file: "single_fw_upgrade.log"
```

## Upgrade Process

### Step 1: Dry-Run (Safe Mode)
```bash
# First, run in dry-run mode to see what will happen
python -m pan_os_upgrade firewall \
  --host 192.168.1.100 \
  --username admin \
  --target-version 10.2.8
```

**Expected Output:**
```
Starting single firewall upgrade (scaffold)
Host: 192.168.1.100, Target: 10.2.8, Dry-run: True
Implement connectivity, readiness checks, download/install, reboot, snapshots...
```

### Step 2: Review Dry-Run Results
- Verify all readiness checks pass
- Confirm backup paths are correct
- Check available disk space
- Review planned actions

### Step 3: Execute Real Upgrade
```bash
# Only after dry-run looks good, disable dry-run
python -m pan_os_upgrade firewall \
  --host 192.168.1.100 \
  --username admin \
  --target-version 10.2.8 \
  --no-dry-run
```

## What Happens During Upgrade (When Implemented)

### Phase 1: Pre-Flight Checks (5-10 minutes)
1. **Connectivity Test**
   - HTTPS management access
   - API authentication
   - Device responsiveness

2. **Readiness Validation**
   - Current PAN-OS version
   - Available disk space (minimum 3GB)
   - No active critical alarms
   - License validity

3. **Backup Creation**
   - Export running configuration
   - Save to local backup directory
   - Timestamp and version the backup

### Phase 2: Pre-Upgrade Snapshot (5-10 minutes)
1. **Network State Capture**
   - Routing table dump
   - Interface status and statistics
   - Active session count
   - System resource utilization

2. **Configuration Snapshot**
   - Security policies
   - NAT rules
   - Network configuration
   - Admin users and roles

### Phase 3: PAN-OS Download (15-30 minutes)
1. **Image Download**
   - Download PAN-OS 10.2.8 image
   - Verify checksum integrity
   - Check available storage

### Phase 4: Installation & Reboot (30-45 minutes)
1. **Install Image**
   - Install PAN-OS image to alternate partition
   - Verify installation success
   - Set boot partition

2. **Device Reboot**
   - Gracefully reboot firewall
   - Wait for system to come online
   - Verify management connectivity

### Phase 5: Post-Upgrade Verification (10-15 minutes)
1. **Version Verification**
   - Confirm PAN-OS 10.2.8 is active
   - Check system status
   - Verify license activation

2. **Post-Upgrade Snapshot**
   - Capture same state as pre-upgrade
   - Compare with baseline
   - Generate difference report

### Phase 6: Reporting (2-5 minutes)
1. **Generate Reports**
   - PDF comparison report
   - Upgrade summary log
   - Success/failure status

## Expected Timeline
- **Total Duration**: 60-120 minutes
- **Actual Downtime**: 5-10 minutes (reboot only)
- **Maintenance Window**: 2 hours (with buffer)

## Post-Upgrade Validation

### Manual Checks
```bash
# Verify device is accessible
ping 192.168.1.100

# Check web management interface
curl -k https://192.168.1.100 -I

# Review generated reports
ls -la ./reports/
```

### Device Validation
1. Log into web interface
2. Verify system information shows 10.2.8
3. Check interface status
4. Verify routing table
5. Test traffic flow

## Rollback Procedure (If Needed)

If issues occur:

1. **Immediate Rollback**
   ```bash
   # Boot to previous partition (manual via console)
   # Or restore from backup configuration
   ```

2. **Configuration Restore**
   ```bash
   # Restore from backup (when implemented)
   python -m pan_os_upgrade restore \
     --host 192.168.1.100 \
     --backup-file ./backups/fw-branch-01_20231226_pre_upgrade.xml
   ```

## Troubleshooting Common Issues

### Issue: Download Fails
**Cause**: Network connectivity or disk space
**Solution**: 
- Check internet connectivity
- Verify available disk space
- Check firewall's DNS settings

### Issue: Installation Fails
**Cause**: Corrupted image or insufficient space
**Solution**:
- Re-download image
- Clear temporary files
- Check system logs

### Issue: Reboot Hangs
**Cause**: Hardware or configuration issue
**Solution**:
- Wait longer (up to 15 minutes)
- Console access for troubleshooting
- Hard reboot if necessary

### Issue: Version Not Updated
**Cause**: Boot partition not switched
**Solution**:
- Manually set boot partition
- Reboot again
- Check system status

## Files Generated

After successful upgrade:
```
./backups/
├── fw-branch-01_20231226_pre_upgrade.xml
└── fw-branch-01_20231226_post_upgrade.xml

./logs/
└── single_fw_upgrade.log

./reports/
├── fw-branch-01_upgrade_summary.pdf
└── fw-branch-01_state_comparison.pdf
```

## Lessons Learned

### Best Practices
1. Always run dry-run first
2. Schedule during maintenance windows
3. Have console access available
4. Keep backups accessible
5. Test rollback procedures

### Common Mistakes to Avoid
1. Skipping dry-run mode
2. Insufficient disk space
3. Not verifying network state
4. Rushing through validation
5. Poor rollback planning

---

**Next Example**: See [ha_pair_upgrade.md](ha_pair_upgrade.md) for upgrading HA pairs.