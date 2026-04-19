"""
Sapling AI detector implementation
"""

from playwright.sync_api import Page
import time
import re
from .base_detector import BaseDetector


class SaplingDetector(BaseDetector):
    """Sapling AI content detector"""
    
    @property
    def name(self) -> str:
        return "sapling"
    
    @property
    def url(self) -> str:
        return self.config['detectors']['sapling']['url']
    
    def _submit_text(self, page: Page, text: str):
        """Submit text to Sapling"""
        try:
            # Wait for textarea
            page.wait_for_selector('textarea', timeout=10000)
            
            textarea = page.query_selector('textarea')
            if textarea:
                textarea.fill(text)
                
                # Click check button
                button_selectors = [
                    'button:has-text("Check")',
                    'button:has-text("Detect")',
                    'button:has-text("Analyze")',
                    'button[type="submit"]'
                ]
                
                for selector in button_selectors:
                    try:
                        button = page.query_selector(selector)
                        if button:
                            button.click()
                            time.sleep(5)
                            break
                    except:
                        continue
                        
        except Exception as e:
            raise Exception(f"Error submitting text to Sapling: {e}")
    
    def _extract_result(self, page: Page) -> float:
        """Extract AI detection percentage from Sapling"""
        try:
            page.wait_for_load_state('networkidle')
            time.sleep(3)
            
            content = page.content()
            
            patterns = [
                r'(\d+(?:\.\d+)?)\s*%.*?(?:AI|fake|generated)',
                r'(?:AI|fake|generated).*?(\d+(?:\.\d+)?)\s*%',
                r'probability.*?(\d+(?:\.\d+)?)',
                r'(\d+(?:\.\d+)?)\s*%'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    percentage = float(matches[0])
                    if 0 <= percentage <= 100:
                        return percentage
            
            raise Exception("Could not extract percentage from results")
            
        except Exception as e:
            raise Exception(f"Error extracting Sapling results: {e}")
