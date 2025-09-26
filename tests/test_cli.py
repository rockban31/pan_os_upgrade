"""Basic CLI tests for the PAN-OS upgrade tool scaffold."""
import pytest
from click.testing import CliRunner
from pan_os_upgrade.main import cli

runner = CliRunner()


def test_app_help():
    """Test that the CLI app shows help."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "PAN-OS Upgrade Automation CLI" in result.output


def test_firewall_command_help():
    """Test that firewall command shows help."""
    result = runner.invoke(cli, ["firewall", "--help"])
    assert result.exit_code == 0
    assert "Upgrade a single firewall" in result.output


def test_inventory_command():
    """Test inventory command creates skeleton file."""
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as tmpdir:
        inventory_path = os.path.join(tmpdir, "test_inventory.yaml")
        result = runner.invoke(cli, ["inventory", "--path", inventory_path])
        assert result.exit_code == 0
        assert "Created" in result.output
        assert os.path.exists(inventory_path)


def test_settings_command():
    """Test settings command creates skeleton file."""
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as tmpdir:
        settings_path = os.path.join(tmpdir, "test_settings.yaml")
        result = runner.invoke(cli, ["settings", "--path", settings_path])
        assert result.exit_code == 0
        assert "Created" in result.output
        assert os.path.exists(settings_path)
