# Batch Upgrade via Panorama Example

This example demonstrates upgrading multiple firewalls managed by Panorama from PAN-OS 10.1.x to 11.0.3.

## Scenario
- **Panorama**: panorama.company.com
- **Managed Firewalls**: 15 branch office firewalls
- **Current Versions**: Mixed (10.1.3, 10.1.4, 10.1.5)
- **Target Version**: 11.0.3
- **Strategy**: Phased rollout with 3 firewalls at a time

## Network Topology
```
Panorama (panorama.company.com)
├── Branch Office Group 1
│   ├── fw-branch-01 (10.1.3) - PA-220
│   ├── fw-branch-02 (10.1.4) - PA-220
│   └── fw-branch-03 (10.1.3) - PA-220
├── Branch Office Group 2
│   ├── fw-branch-04 (10.1.5) - PA-3220
│   ├── fw-branch-05 (10.1.4) - PA-3220
│   └── fw-branch-06 (10.1.3) - PA-3220
└── [... 9 more firewalls]
```

## Pre-Upgrade Planning

### 1. Inventory Assessment
```bash
# Generate inventory template
python -m pan_os_upgrade inventory --path batch-inventory.yaml

# Generate settings for batch operation
python -m pan_os_upgrade settings --path batch-settings.yaml
```

### 2. Configure Inventory for Batch Operation
```yaml
# batch-inventory.yaml
firewalls:
  # Group 1: Branch offices (PA-220)
  - hostname: fw-branch-01.company.com
    ip: 192.168.10.1
    username: admin
    model: PA-220
    current_version: "10.1.3"
    ha_mode: disabled
    group: branch_pa220
    
  - hostname: fw-branch-02.company.com
    ip: 192.168.20.1
    username: admin
    model: PA-220
    current_version: "10.1.4"
    ha_mode: disabled
    group: branch_pa220
    
  # Group 2: Regional offices (PA-3220)
  - hostname: fw-region-01.company.com
    ip: 192.168.100.1
    username: admin
    model: PA-3220
    current_version: "10.1.5"
    ha_mode: disabled
    group: regional_pa3220

# Group definitions for phased rollout
groups:
  pilot_group:
    - fw-branch-01.company.com
    - fw-branch-02.company.com
    - fw-branch-03.company.com
  
  branch_offices:
    - fw-branch-04.company.com
    - fw-branch-05.company.com
    # ... more branch offices
  
  regional_offices:
    - fw-region-01.company.com
    - fw-region-02.company.com
    # ... more regional offices

panorama:
  host: panorama.company.com
  username: admin
  api_key_env: PANORAMA_API_KEY  # Use API key instead of password
```

### 3. Configure Batch Settings
```yaml
# batch-settings.yaml
# Batch-specific settings
dry_run_default: true
concurrency: 3  # Maximum 3 simultaneous upgrades
max_workers: 5  # Thread pool size

# Retry configuration for network operations
retry_count: 5  # More retries for network issues
retry_delay_seconds: 30  # Longer delays for stability

# Timeout settings for slower connections
connection_timeout_seconds: 120
post_reboot_wait_seconds: 600  # 10 minutes for slower devices

# Safety and verification
pre_post_snapshots: true
generate_pdf_diff: true
backup_config: true
version_check_enabled: true

# Batch-specific behavior
fail_fast: false  # Continue with other devices if one fails
rollback_on_failure: true  # Auto-rollback failed devices

# Progress reporting
progress_reporting: true
progress_interval_seconds: 60
email_notifications: true  # Send status emails

# Resource management
pause_between_groups: true
group_pause_minutes: 15  # Wait between device groups

# Logging and audit
log_level: "INFO"
log_to_file: true
log_file: "batch_upgrade.log"
audit_trail: true

# Backup management
backup_location: "./backups"
backup_retention_days: 60  # Keep longer for batch operations
compress_backups: true

# Report generation
reports_directory: "./reports"
generate_summary_report: true
include_device_details: true
```

## Phased Upgrade Execution

### Phase 1: Pilot Group (Dry-Run)
```bash
# First, test with pilot group in dry-run mode
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3 \
  --group pilot_group \
  --dry-run
```

**Expected Output:**
```
Starting batch upgrade workflow (scaffold)
Panorama: panorama.company.com, Target: 11.0.3, Dry-run: True
Connecting to Panorama...
Discovered 3 managed firewalls in pilot_group
Planning upgrade sequence...

Device: fw-branch-01 (10.1.3 → 11.0.3) - READY
Device: fw-branch-02 (10.1.4 → 11.0.3) - READY  
Device: fw-branch-03 (10.1.3 → 11.0.3) - READY

Dry-run completed successfully. No changes made.
```

### Phase 2: Execute Pilot Group
```bash
# Execute pilot group upgrade (real upgrade)
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3 \
  --group pilot_group \
  --no-dry-run
```

### Phase 3: Monitor Progress
During execution, the tool would display:
```
[14:30:15] Starting batch upgrade for 3 devices
[14:30:16] ✓ Connected to Panorama (panorama.company.com)
[14:30:17] ✓ Validated 3 target devices
[14:30:18] Starting concurrent upgrades (max: 3)

[14:30:20] fw-branch-01: Starting readiness checks...
[14:30:20] fw-branch-02: Starting readiness checks...
[14:30:20] fw-branch-03: Starting readiness checks...

[14:32:45] fw-branch-01: ✓ Readiness checks passed
[14:32:46] fw-branch-02: ✓ Readiness checks passed  
[14:32:47] fw-branch-03: ✓ Readiness checks passed

[14:33:00] fw-branch-01: Creating configuration backup...
[14:33:15] fw-branch-02: Creating configuration backup...
[14:33:30] fw-branch-03: Creating configuration backup...

[14:35:00] fw-branch-01: Downloading PAN-OS 11.0.3 (1.2GB)...
[14:45:30] fw-branch-01: ✓ Download complete, starting installation
[14:46:00] fw-branch-02: ✓ Download complete, starting installation
[14:47:15] fw-branch-03: ✓ Download complete, starting installation

[15:15:00] fw-branch-01: Rebooting device...
[15:15:30] fw-branch-02: Rebooting device...
[15:16:45] fw-branch-03: Rebooting device...

[15:25:00] fw-branch-01: ✓ Device online, verifying upgrade
[15:25:30] fw-branch-02: ✓ Device online, verifying upgrade
[15:27:00] fw-branch-03: ✓ Device online, verifying upgrade

[15:30:00] ✓ All 3 devices upgraded successfully!
           Duration: 1h 00m
           Success Rate: 100%
```

### Phase 4: Validation Before Next Phase
```bash
# Validate pilot group before proceeding
python -m pan_os_upgrade validate \
  --group pilot_group \
  --expected-version 11.0.3
```

### Phase 5: Continue with Remaining Groups
```bash
# Upgrade branch offices (after pilot success)
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3 \
  --group branch_offices \
  --no-dry-run

# Wait for completion, then regional offices
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --username admin \
  --target-version 11.0.3 \
  --group regional_offices \
  --no-dry-run
```

## Advanced Batch Operations

### Selective Device Targeting
```bash
# Upgrade only devices with specific current version
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --target-version 11.0.3 \
  --filter-current-version "10.1.3" \
  --no-dry-run

# Upgrade only specific device models
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --target-version 11.0.3 \
  --filter-model "PA-220" \
  --no-dry-run
```

### Scheduling and Automation
```bash
# Schedule upgrade for off-hours (planned feature)
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --target-version 11.0.3 \
  --schedule "2024-01-15 02:00:00" \
  --timezone "America/New_York"

# Use maintenance windows defined in Panorama
python -m pan_os_upgrade batch \
  --panorama-host panorama.company.com \
  --target-version 11.0.3 \
  --respect-maintenance-windows \
  --no-dry-run
```

## Monitoring and Status

### Real-Time Monitoring
```bash
# Monitor active batch upgrade
python -m pan_os_upgrade status \
  --batch-id upgrade-20241226-143000

# Get detailed progress report
python -m pan_os_upgrade progress \
  --batch-id upgrade-20241226-143000 \
  --detailed
```

### Status Dashboard (Future Feature)
```
Batch Upgrade Status: upgrade-20241226-143000
Target Version: 11.0.3
Started: 2024-12-26 14:30:00

Progress: 12/15 devices (80%)
Success: 11 devices
Failed: 1 device (fw-branch-07 - disk space)
In Progress: 1 device (fw-region-03)
Pending: 2 devices

Estimated Completion: 16:45:00 (2h 15m remaining)
```

## Error Handling and Recovery

### Automatic Recovery Actions
```yaml
# In batch-settings.yaml
error_handling:
  auto_retry_failed: true
  max_retry_attempts: 2
  retry_delay_minutes: 10
  
  # Automatic rollback on critical failures
  auto_rollback_conditions:
    - "boot_failure"
    - "management_unreachable > 20min"
    - "license_activation_failed"
  
  # Notification settings
  notify_on_failure: true
  notify_on_success: true
  notification_channels:
    - email: admin@company.com
    - slack: "#network-ops"
```

### Manual Recovery
```bash
# Retry failed devices only
python -m pan_os_upgrade retry \
  --batch-id upgrade-20241226-143000 \
  --failed-only

# Rollback specific device
python -m pan_os_upgrade rollback \
  --host fw-branch-07.company.com \
  --to-version 10.1.4

# Resume interrupted batch
python -m pan_os_upgrade resume \
  --batch-id upgrade-20241226-143000
```

## Reporting and Audit

### Generated Reports
```
./reports/batch-upgrade-20241226-143000/
├── summary.pdf                    # Executive summary
├── detailed_report.pdf           # Technical details
├── device_reports/               # Per-device reports
│   ├── fw-branch-01_upgrade.pdf
│   ├── fw-branch-02_upgrade.pdf
│   └── ...
├── failure_analysis.pdf         # Failed devices analysis
├── timeline.html                # Interactive timeline
└── audit_log.json              # Machine-readable audit trail
```

### Summary Statistics
```json
{
  "batch_id": "upgrade-20241226-143000",
  "target_version": "11.0.3",
  "start_time": "2024-12-26T14:30:00Z",
  "end_time": "2024-12-26T17:45:00Z",
  "total_duration": "3h 15m",
  "devices": {
    "total": 15,
    "successful": 14,
    "failed": 1,
    "skipped": 0
  },
  "success_rate": "93.3%",
  "total_downtime": "45 minutes",
  "data_transferred": "18.2 GB",
  "backup_size": "2.1 GB"
}
```

## Best Practices for Batch Upgrades

### Planning Phase
1. **Start Small**: Begin with pilot group
2. **Group Strategically**: Similar devices and locations
3. **Plan Rollback**: Have rollback procedures ready
4. **Schedule Wisely**: Use maintenance windows
5. **Communicate**: Notify stakeholders

### Execution Phase
1. **Monitor Closely**: Watch for issues early
2. **Validate Frequently**: Check each phase completion
3. **Be Patient**: Don't rush the process
4. **Document Issues**: Track problems for learning
5. **Stay Available**: Be ready for manual intervention

### Post-Upgrade Phase
1. **Validate All Devices**: Comprehensive testing
2. **Update Documentation**: Record changes
3. **Review Metrics**: Analyze performance
4. **Plan Next Phase**: Apply lessons learned
5. **Archive Reports**: Keep for compliance

---

**Related Examples**: 
- [single_firewall_upgrade.md](single_firewall_upgrade.md) for individual device upgrades
- [ha_pair_upgrade.md](ha_pair_upgrade.md) for HA pair scenarios