"""
Detector Manager - Orchestrates all AI detectors
"""

from typing import Dict, List
from concurrent.futures import ThreadPoolExecutor, as_completed
from .gptzero import GPTZeroDetector
from .writer import WriterDetector
from .zerogpt import ZeroGPTDetector
from .sapling import SaplingDetector
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class DetectorManager:
    """Manages multiple AI detectors"""
    
    def __init__(self, config: dict):
        """
        Initialize detector manager
        
        Args:
            config: Application configuration
        """
        self.config = config
        self.enabled_detectors = config['detectors']['enabled']
        self.parallel = config['performance']['parallel_detection']
        self.max_workers = config['performance']['max_concurrent_detectors']
        
        # Initialize detectors
        self.detectors = self._initialize_detectors()
    
    def _initialize_detectors(self) -> Dict:
        """Initialize all enabled detectors"""
        detector_classes = {
            'gptzero': GPTZeroDetector,
            'writer': WriterDetector,
            'zerogpt': ZeroGPTDetector,
            'sapling': SaplingDetector
        }
        
        detectors = {}
        for name in self.enabled_detectors:
            if name in detector_classes:
                try:
                    detectors[name] = detector_classes[name](self.config)
                    logger.info(f"Initialized detector: {name}")
                except Exception as e:
                    logger.error(f"Failed to initialize detector {name}: {e}")
        
        return detectors
    
    def detect(self, text: str) -> Dict[str, dict]:
        """
        Run all detectors on text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary of results from each detector
        """
        if self.parallel:
            return self._detect_parallel(text)
        else:
            return self._detect_sequential(text)
    
    def _detect_sequential(self, text: str) -> Dict[str, dict]:
        """Run detectors sequentially"""
        results = {}
        
        for name, detector in self.detectors.items():
            logger.info(f"Running detector: {name}")
            try:
                result = detector.detect(text)
                results[name] = result
                
                if result['success']:
                    logger.info(f"{name} result: {result['ai_percentage']:.1f}% AI")
                else:
                    logger.warning(f"{name} failed: {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                logger.error(f"Error running {name}: {e}")
                results[name] = {
                    'success': False,
                    'error': str(e),
                    'detector': name
                }
        
        return results
    
    def _detect_parallel(self, text: str) -> Dict[str, dict]:
        """Run detectors in parallel"""
        results = {}
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all detector tasks
            futures = {
                executor.submit(detector.detect, text): name
                for name, detector in self.detectors.items()
            }
            
            # Collect results as they complete
            for future in as_completed(futures):
                name = futures[future]
                try:
                    result = future.result()
                    results[name] = result
                    
                    if result['success']:
                        logger.info(f"{name} result: {result['ai_percentage']:.1f}% AI")
                    else:
                        logger.warning(f"{name} failed: {result.get('error', 'Unknown error')}")
                        
                except Exception as e:
                    logger.error(f"Error running {name}: {e}")
                    results[name] = {
                        'success': False,
                        'error': str(e),
                        'detector': name
                    }
        
        return results
    
    def get_average_score(self, results: Dict[str, dict]) -> float:
        """
        Calculate average AI detection score
        
        Args:
            results: Detection results
            
        Returns:
            Average AI percentage (0-100)
        """
        scores = [
            result['ai_percentage']
            for result in results.values()
            if result['success']
        ]
        
        if not scores:
            return 0.0
        
        return sum(scores) / len(scores)
    
    def get_successful_count(self, results: Dict[str, dict]) -> int:
        """Get count of successful detections"""
        return sum(1 for r in results.values() if r['success'])
