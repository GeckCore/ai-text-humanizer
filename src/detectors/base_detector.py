"""
Base detector class for AI content detection
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional
from playwright.sync_api import sync_playwright, Page, Browser
import time


class BaseDetector(ABC):
    """Abstract base class for AI detectors"""
    
    def __init__(self, config: dict):
        """
        Initialize detector
        
        Args:
            config: Application configuration
        """
        self.config = config
        self.browser_config = config['browser']
        self.timeout = config['detectors'].get(self.name, {}).get('timeout', 30)
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Detector name"""
        pass
    
    @property
    @abstractmethod
    def url(self) -> str:
        """Detector URL"""
        pass
    
    @abstractmethod
    def _extract_result(self, page: Page) -> float:
        """
        Extract AI detection percentage from page
        
        Args:
            page: Playwright page object
            
        Returns:
            AI detection percentage (0-100)
        """
        pass
    
    def detect(self, text: str) -> Dict[str, any]:
        """
        Detect AI content in text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dict with detection results
        """
        try:
            with sync_playwright() as p:
                browser = self._launch_browser(p)
                page = browser.new_page()
                
                # Set longer timeout
                page.set_default_timeout(self.timeout * 1000)
                
                # Navigate to detector
                page.goto(self.url, wait_until='networkidle')
                
                # Submit text
                self._submit_text(page, text)
                
                # Extract result
                ai_percentage = self._extract_result(page)
                
                browser.close()
                
                return {
                    'success': True,
                    'ai_percentage': ai_percentage,
                    'detector': self.name
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'detector': self.name
            }
    
    def _launch_browser(self, playwright) -> Browser:
        """Launch browser with configuration"""
        return playwright.chromium.launch(
            headless=self.browser_config['headless']
        )
    
    @abstractmethod
    def _submit_text(self, page: Page, text: str):
        """
        Submit text to detector
        
        Args:
            page: Playwright page object
            text: Text to analyze
        """
        pass
    
    def _wait_for_result(self, page: Page, timeout: int = None):
        """Wait for result to be ready"""
        if timeout is None:
            timeout = self.timeout
        time.sleep(timeout)
