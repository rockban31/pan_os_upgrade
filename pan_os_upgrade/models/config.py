"""Configuration models for the PAN-OS upgrade tool (scaffold)."""
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import yaml
from pathlib import Path


@dataclass
class FirewallInfo:
    """Firewall device information."""
    hostname: str
    ip: str
    username: str
    password: Optional[str] = None  # Should be provided via environment or secret manager
    model: Optional[str] = None
    current_version: Optional[str] = None
    ha_mode: Optional[str] = None


@dataclass
class Settings:
    """Global settings for the upgrade tool."""
    concurrency: int = 5
    retry_count: int = 3
    retry_delay_seconds: int = 15
    pre_post_snapshots: bool = True
    generate_pdf_diff: bool = True
    
    @classmethod
    def load_from_file(cls, path: str = "settings.yaml") -> "Settings":
        """Load settings from YAML file."""
        settings_path = Path(path)
        if not settings_path.exists():
            return cls()  # Return defaults
        
        with open(settings_path) as f:
            data = yaml.safe_load(f)
        
        return cls(**data)


@dataclass
class Inventory:
    """Inventory of firewalls to manage."""
    firewalls: List[FirewallInfo]
    
    @classmethod
    def load_from_file(cls, path: str = "inventory.yaml") -> "Inventory":
        """Load inventory from YAML file."""
        inventory_path = Path(path)
        if not inventory_path.exists():
            return cls(firewalls=[])
        
        with open(inventory_path) as f:
            data = yaml.safe_load(f)
        
        firewalls = [FirewallInfo(**fw) for fw in data.get("firewalls", [])]
        return cls(firewalls=firewalls)