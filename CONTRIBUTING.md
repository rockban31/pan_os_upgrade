# Contributing to PAN-OS Upgrade Automation

Thank you for your interest in contributing! This project is a scaffold inspired by the original [pan-os-upgrade](https://github.com/cdot65/pan-os-upgrade) tool.

## Development Setup

1. Clone the repository
2. Create a virtual environment: `py -3.11 -m venv .venv`
3. Activate the environment: `.venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`
5. Install development dependencies (if using Poetry): `poetry install --with dev`

## Code Style

- Use [Black](https://black.readthedocs.io/) for code formatting
- Follow PEP 8 conventions
- Add type hints where appropriate
- Write docstrings for functions and classes

## Testing

Run tests with pytest:
```bash
pytest
```

## Submitting Changes

1. Create a feature branch from `main`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request with a clear description

## Areas for Contribution

- Implement real PAN-OS API integration using pan-os-python
- Add comprehensive error handling
- Implement network state snapshot comparison
- Add PDF report generation for diffs
- Enhance HA support and workflows
- Add comprehensive logging
- Improve CLI user experience

## Questions?

Open an issue for questions or discussion about potential contributions.