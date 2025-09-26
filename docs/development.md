# Development Guide

This document provides guidance for developing and extending the PAN-OS upgrade tool.

## Project Structure

```
pan_os_upgrade/
├── pan_os_upgrade/          # Main Python package
│   ├── __init__.py         # Package init
│   ├── __main__.py         # Entry point for python -m
│   ├── main.py             # CLI application with Typer
│   ├── components/         # Core functionality modules
│   │   ├── firewall.py     # Firewall connection management
│   │   └── snapshots.py    # Network state snapshots
│   ├── models/             # Data models and configuration
│   │   └── config.py       # Configuration classes
│   └── assets/             # Static assets (images, templates)
├── tests/                  # Test suite
├── docs/                   # Documentation
├── docker/                 # Docker configuration
└── .github/workflows/      # GitHub Actions CI/CD
```

## Implementation Roadmap

### Phase 1: Core Infrastructure ✅
- [x] CLI framework with Typer
- [x] Configuration management (YAML)
- [x] Basic project structure
- [x] Testing framework

### Phase 2: PAN-OS Integration
- [ ] Integrate pan-os-python library
- [ ] Implement real firewall connections
- [ ] Add authentication methods
- [ ] Version detection and comparison

### Phase 3: Upgrade Workflow
- [ ] Pre-upgrade checks (readiness)
- [ ] Download and install images
- [ ] Reboot and recovery logic
- [ ] HA pair handling

### Phase 4: Network State Management
- [ ] Network state collection
- [ ] Snapshot comparison logic
- [ ] PDF report generation
- [ ] Diff visualization

### Phase 5: Advanced Features
- [ ] Batch operations via Panorama
- [ ] Multi-threading support
- [ ] Progress indicators
- [ ] Detailed logging

## Adding New Features

1. Create new modules in appropriate directories
2. Add tests in `tests/` directory
3. Update CLI commands in `main.py`
4. Update documentation
5. Test thoroughly with real devices (carefully!)

## Security Considerations

- Never store passwords in plain text
- Use environment variables or secure credential stores
- Implement proper input validation
- Log security events appropriately
- Default to dry-run mode for safety

## Testing Strategy

- Unit tests for individual components
- Integration tests with mock PAN-OS responses
- CLI tests for user interface
- End-to-end tests with lab devices only