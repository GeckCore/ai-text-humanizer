# Makefile for AI Text Humanizer

.PHONY: help install install-dev test lint format clean run

help:
	@echo "AI Text Humanizer - Available Commands:"
	@echo ""
	@echo "  make install      - Install project dependencies"
	@echo "  make install-dev  - Install dev dependencies"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make format       - Format code with black"
	@echo "  make clean        - Clean generated files"
	@echo "  make run          - Run the application"
	@echo "  make setup-ollama - Setup Ollama and download model"
	@echo ""

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	playwright install chromium

install-dev: install
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ -v --cov=src --cov-report=term --cov-report=html

lint:
	flake8 src tests
	mypy src
	black --check src tests

format:
	black src tests
	isort src tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf dist
	rm -rf build

run:
	python -m src.main

setup-ollama:
	@echo "Checking Ollama installation..."
	@command -v ollama >/dev/null 2>&1 || { echo "Installing Ollama..."; curl -fsSL https://ollama.ai/install.sh | sh; }
	@echo "Pulling qwen2.5:14b model..."
	ollama pull qwen2.5:14b
	@echo "Setup complete!"

docker-build:
	docker build -t ai-text-humanizer .

docker-run:
	docker run -it --rm -v $(PWD)/output:/app/output ai-text-humanizer
