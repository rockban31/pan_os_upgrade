"""Tests for component modules (scaffold)."""
import pytest
from pan_os_upgrade.components.firewall import FirewallConnection
from pan_os_upgrade.components.snapshots import NetworkSnapshot


def test_firewall_connection():
    """Test firewall connection class."""
    fw = FirewallConnection("192.0.2.10", "admin", "secret")
    assert fw.host == "192.0.2.10"
    assert fw.username == "admin"
    assert fw.password == "secret"
    assert not fw.connected
    
    # Test connection (mock)
    result = fw.connect()
    assert result is True
    assert fw.connected is True
    
    # Test version retrieval (mock)
    version = fw.get_version()
    assert version == "10.1.3"


def test_network_snapshot():
    """Test network snapshot functionality."""
    import tempfile
    import shutil
    from pathlib import Path
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change to temp directory for testing
        original_cwd = Path.cwd()
        try:
            import os
            os.chdir(tmpdir)
            
            snapshot = NetworkSnapshot("test-fw")
            
            # Test snapshot creation
            pre_snapshot = snapshot.take_snapshot("pre")
            assert pre_snapshot.exists()
            assert "pre" in str(pre_snapshot)
            
            post_snapshot = snapshot.take_snapshot("post")
            assert post_snapshot.exists()
            assert "post" in str(post_snapshot)
            
            # Test diff report generation
            report = snapshot.generate_diff_report(pre_snapshot, post_snapshot)
            assert report.exists()
            assert report.suffix == ".pdf"
            
        finally:
            os.chdir(original_cwd)