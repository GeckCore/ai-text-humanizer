"""
Setup script for AI Text Humanizer
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = (this_directory / "requirements.txt").read_text().splitlines()
requirements = [r.strip() for r in requirements if r.strip() and not r.startswith('#')]

setup(
    name="ai-text-humanizer",
    version="1.0.0",
    author="AI Text Humanizer Contributors",
    author_email="contact@example.com",
    description="Herramienta para analizar y humanizar texto generado por IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/ai-text-humanizer",
    project_urls={
        "Bug Tracker": "https://github.com/tu-usuario/ai-text-humanizer/issues",
        "Documentation": "https://github.com/tu-usuario/ai-text-humanizer/blob/main/docs/USAGE.md",
        "Source Code": "https://github.com/tu-usuario/ai-text-humanizer",
    },
    packages=find_packages(exclude=["tests", "tests.*", "docs", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Spanish",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: German",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=8.1.1",
            "pytest-cov>=4.1.0",
            "black>=24.2.0",
            "flake8>=7.0.0",
            "mypy>=1.9.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "ai-text-humanizer=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["config/*.yaml"],
    },
    keywords=[
        "ai",
        "text",
        "humanizer",
        "detection",
        "nlp",
        "natural-language-processing",
        "ai-detection",
        "text-rewriting",
        "ollama",
        "gpt",
    ],
    zip_safe=False,
)
