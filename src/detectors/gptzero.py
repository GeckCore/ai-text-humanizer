"""
GPTZero AI detector implementation
"""

from playwright.sync_api import Page
import time
import re
from .base_detector import BaseDetector


class GPTZeroDetector(BaseDetector):
    """GPTZero AI content detector"""
    
    @property
    def name(self) -> str:
        return "gptzero"
    
    @property
    def url(self) -> str:
        return self.config['detectors']['gptzero']['url']
    
    def _submit_text(self, page: Page, text: str):
        """Submit text to GPTZero"""
        try:
            # Wait for textarea to be ready
            page.wait_for_selector('textarea', timeout=10000)
            
            # Fill textarea
            textarea = page.query_selector('textarea')
            if textarea:
                textarea.fill(text)
                
                # Click analyze button
                # Try multiple possible selectors
                button_selectors = [
                    'button:has-text("Get Results")',
                    'button:has-text("Check")',
                    'button:has-text("Analyze")',
                    'button[type="submit"]',
                    '.btn-primary'
                ]
                
                for selector in button_selectors:
                    try:
                        button = page.query_selector(selector)
                        if button:
                            button.click()
                            break
                    except:
                        continue
                
                # Wait for results
                time.sleep(5)
                
        except Exception as e:
            raise Exception(f"Error submitting text to GPTZero: {e}")
    
    def _extract_result(self, page: Page) -> float:
        """Extract AI detection percentage from GPTZero"""
        try:
            # Wait for results to load
            page.wait_for_load_state('networkidle')
            time.sleep(3)
            
            # Try to extract percentage from various elements
            # GPTZero typically shows results like "85% AI Generated"
            selectors = [
                '.result-percentage',
                '.ai-score',
                'text=/\\d+%/',
                '*:has-text("%")'
            ]
            
            content = page.content()
            
            # Look for percentage patterns
            patterns = [
                r'(\d+)%\s*(?:AI|ai|generated)',
                r'(?:AI|ai).*?(\d+)%',
                r'probability.*?(\d+)%',
                r'(\d+(?:\.\d+)?)\s*%'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    # Get the first percentage found
                    percentage = float(matches[0])
                    if 0 <= percentage <= 100:
                        return percentage
            
            # If no clear percentage found, try to infer from text
            if 'human' in content.lower() and 'likely' in content.lower():
                return 10.0  # Low AI probability
            elif 'ai' in content.lower() and 'likely' in content.lower():
                return 85.0  # High AI probability
            
            raise Exception("Could not extract percentage from results")
            
        except Exception as e:
            raise Exception(f"Error extracting GPTZero results: {e}")
