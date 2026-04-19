"""
Configuration loader for AI Text Humanizer
"""

import yaml
from pathlib import Path
from typing import Dict, Any


class ConfigLoader:
    """Load and manage application configuration"""
    
    DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"
    
    def __init__(self, config_path: str = None):
        """
        Initialize configuration loader
        
        Args:
            config_path: Path to custom config file
        """
        self.config_path = Path(config_path) if config_path else self.DEFAULT_CONFIG_PATH
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        return config
    
    def get(self, key: str, default=None):
        """Get configuration value by key"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default
        
        return value
