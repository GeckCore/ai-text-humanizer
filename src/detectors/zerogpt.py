"""
ZeroGPT AI detector implementation
"""

from playwright.sync_api import Page
import time
import re
from .base_detector import BaseDetector


class ZeroGPTDetector(BaseDetector):
    """ZeroGPT AI content detector"""
    
    @property
    def name(self) -> str:
        return "zerogpt"
    
    @property
    def url(self) -> str:
        return self.config['detectors']['zerogpt']['url']
    
    def _submit_text(self, page: Page, text: str):
        """Submit text to ZeroGPT"""
        try:
            # Wait for textarea
            page.wait_for_selector('textarea', timeout=10000)
            
            textarea = page.query_selector('textarea')
            if textarea:
                textarea.fill(text)
                
                # Click detect button
                button_selectors = [
                    'button:has-text("Detect")',
                    'button:has-text("Check")',
                    '#detectButton',
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
            raise Exception(f"Error submitting text to ZeroGPT: {e}")
    
    def _extract_result(self, page: Page) -> float:
        """Extract AI detection percentage from ZeroGPT"""
        try:
            page.wait_for_load_state('networkidle')
            time.sleep(3)
            
            content = page.content()
            
            # ZeroGPT typically shows "X% of your text is AI generated"
            patterns = [
                r'(\d+(?:\.\d+)?)\s*%.*?(?:AI|ai)',
                r'(?:AI|ai).*?(\d+(?:\.\d+)?)\s*%',
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
            raise Exception(f"Error extracting ZeroGPT results: {e}")
