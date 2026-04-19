"""
Text processing utilities
"""

import re
from typing import List


class TextProcessor:
    """Process and validate text"""
    
    def __init__(self, config: dict):
        """Initialize text processor"""
        self.config = config
        self.min_length = config['text']['min_length']
        self.max_length = config['text']['max_length']
        self.chunk_size = config['text']['chunk_size']
    
    def validate(self, text: str) -> tuple[bool, str]:
        """
        Validate text
        
        Returns:
            (is_valid, error_message)
        """
        if not text or not text.strip():
            return False, "Texto vacío"
        
        text_length = len(text)
        
        if text_length < self.min_length:
            return False, f"Texto muy corto (mín. {self.min_length} caracteres)"
        
        if text_length > self.max_length:
            return False, f"Texto muy largo (máx. {self.max_length} caracteres)"
        
        return True, ""
    
    def clean(self, text: str) -> str:
        """Clean text by removing extra whitespace"""
        # Remove multiple spaces
        text = re.sub(r' +', ' ', text)
        
        # Remove multiple newlines (keep max 2)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
    
    def chunk_text(self, text: str) -> List[str]:
        """
        Split text into chunks for processing
        
        Args:
            text: Input text
            
        Returns:
            List of text chunks
        """
        if len(text) <= self.chunk_size:
            return [text]
        
        chunks = []
        sentences = self._split_sentences(text)
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= self.chunk_size:
                current_chunk += sentence + " "
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence + " "
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitting
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s for s in sentences if s.strip()]
    
    def count_words(self, text: str) -> int:
        """Count words in text"""
        return len(text.split())
    
    def get_stats(self, text: str) -> dict:
        """Get text statistics"""
        return {
            'characters': len(text),
            'words': self.count_words(text),
            'sentences': len(self._split_sentences(text)),
            'paragraphs': len([p for p in text.split('\n\n') if p.strip()])
        }
