"""
Tests for configuration loader
"""

import pytest
import yaml
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.config_loader import ConfigLoader


class TestConfigLoader:
    """Test ConfigLoader class"""
    
    def test_load_default_config(self):
        """Test loading default configuration"""
        loader = ConfigLoader()
        assert loader.config is not None
        assert isinstance(loader.config, dict)
    
    def test_config_has_required_keys(self):
        """Test that config has all required keys"""
        loader = ConfigLoader()
        config = loader.config
        
        required_keys = ['ollama', 'detectors', 'rewriting', 'languages', 'output']
        for key in required_keys:
            assert key in config, f"Missing required key: {key}"
    
    def test_get_existing_key(self):
        """Test getting existing configuration value"""
        loader = ConfigLoader()
        model = loader.get('ollama.model')
        assert model is not None
        assert isinstance(model, str)
    
    def test_get_nested_key(self):
        """Test getting nested configuration value"""
        loader = ConfigLoader()
        max_iterations = loader.get('rewriting.max_iterations')
        assert max_iterations is not None
        assert isinstance(max_iterations, int)
    
    def test_get_non_existing_key(self):
        """Test getting non-existing key with default"""
        loader = ConfigLoader()
        value = loader.get('non.existing.key', default='default_value')
        assert value == 'default_value'
    
    def test_get_without_default(self):
        """Test getting non-existing key without default"""
        loader = ConfigLoader()
        value = loader.get('non.existing.key')
        assert value is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
