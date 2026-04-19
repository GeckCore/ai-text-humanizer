"""
Logging utilities for AI Text Humanizer
"""

import sys
from pathlib import Path
from loguru import logger


def setup_logger(name: str = None, level: str = "INFO"):
    """
    Setup logger with file and console output
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
    
    Returns:
        Logger instance
    """
    # Remove default handler
    logger.remove()
    
    # Console handler with colors
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <level>{message}</level>",
        level=level,
        colorize=True
    )
    
    # File handler
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logger.add(
        log_dir / "ai_text_humanizer_{time:YYYY-MM-DD}.log",
        rotation="10 MB",
        retention="7 days",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} | {message}",
        encoding="utf-8"
    )
    
    if name:
        return logger.bind(name=name)
    
    return logger


# Create default logger
default_logger = setup_logger()
