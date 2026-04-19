"""
Tests for text processor module
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.text_processor import TextProcessor


@pytest.fixture
def config():
    """Mock configuration"""
    return {
        'text': {
            'min_length': 50,
            'max_length': 50000,
            'chunk_size': 2000
        }
    }


@pytest.fixture
def processor(config):
    """Create text processor instance"""
    return TextProcessor(config)


class TestTextProcessor:
    """Test TextProcessor class"""
    
    def test_validate_valid_text(self, processor):
        """Test validation with valid text"""
        text = "This is a valid text " * 10  # ~200 chars
        is_valid, error = processor.validate(text)
        assert is_valid
        assert error == ""
    
    def test_validate_empty_text(self, processor):
        """Test validation with empty text"""
        is_valid, error = processor.validate("")
        assert not is_valid
        assert "vacío" in error.lower()
    
    def test_validate_too_short(self, processor):
        """Test validation with too short text"""
        text = "Short"
        is_valid, error = processor.validate(text)
        assert not is_valid
        assert "corto" in error.lower()
    
    def test_validate_too_long(self, processor):
        """Test validation with too long text"""
        text = "x" * 60000
        is_valid, error = processor.validate(text)
        assert not is_valid
        assert "largo" in error.lower()
    
    def test_clean_text(self, processor):
        """Test text cleaning"""
        dirty = "Text  with   multiple    spaces\n\n\n\nand newlines"
        clean = processor.clean(dirty)
        assert "  " not in clean
        assert "\n\n\n" not in clean
    
    def test_count_words(self, processor):
        """Test word counting"""
        text = "One two three four five"
        count = processor.count_words(text)
        assert count == 5
    
    def test_get_stats(self, processor):
        """Test getting text statistics"""
        text = "First sentence. Second sentence.\n\nNew paragraph."
        stats = processor.get_stats(text)
        
        assert stats['characters'] > 0
        assert stats['words'] > 0
        assert stats['sentences'] >= 2
        assert stats['paragraphs'] >= 1
    
    def test_chunk_text_small(self, processor):
        """Test chunking with small text"""
        text = "Small text that doesn't need chunking."
        chunks = processor.chunk_text(text)
        assert len(chunks) == 1
        assert chunks[0] == text
    
    def test_chunk_text_large(self, processor):
        """Test chunking with large text"""
        # Create text larger than chunk_size
        text = "Sentence. " * 500
        chunks = processor.chunk_text(text)
        assert len(chunks) > 1
        
        # Each chunk should be under chunk_size
        for chunk in chunks:
            assert len(chunk) <= processor.chunk_size + 100  # Some margin


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
