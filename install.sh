#!/bin/bash

# AI Text Humanizer - Installation Script
# This script automates the installation process

set -e  # Exit on error

echo "=================================="
echo "AI Text Humanizer - Installation"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "ℹ $1"
}

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_success "Python $PYTHON_VERSION found"

# Check pip
echo "Checking pip..."
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 is not installed"
    exit 1
fi
print_success "pip found"

# Check Ollama
echo "Checking Ollama..."
if ! command -v ollama &> /dev/null; then
    print_warning "Ollama is not installed"
    echo ""
    echo "Ollama is required for this application."
    echo "Install it from: https://ollama.ai"
    echo ""
    read -p "Do you want to install Ollama now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Installing Ollama..."
        curl -fsSL https://ollama.ai/install.sh | sh
        print_success "Ollama installed"
    else
        print_error "Ollama is required. Exiting."
        exit 1
    fi
else
    print_success "Ollama found"
fi

# Create virtual environment
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    print_warning "Virtual environment already exists"
    read -p "Do you want to recreate it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf venv
        python3 -m venv venv
        print_success "Virtual environment recreated"
    fi
else
    python3 -m venv venv
    print_success "Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
print_success "Virtual environment activated"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
print_success "pip upgraded"

# Install dependencies
echo "Installing Python dependencies..."
echo "(This may take a few minutes...)"
pip install -r requirements.txt > /dev/null 2>&1
print_success "Dependencies installed"

# Install Playwright browsers
echo "Installing Playwright browsers..."
playwright install chromium > /dev/null 2>&1
print_success "Playwright browsers installed"

# Pull Ollama model
echo "Checking Ollama models..."
if ollama list | grep -q "qwen2.5:14b"; then
    print_success "Model qwen2.5:14b already downloaded"
else
    print_warning "Model qwen2.5:14b not found"
    echo ""
    echo "The model is approximately 8GB and required for the application."
    read -p "Do you want to download it now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Downloading model (this will take a while)..."
        ollama pull qwen2.5:14b
        print_success "Model downloaded"
    else
        print_warning "You'll need to download it later with: ollama pull qwen2.5:14b"
    fi
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p output logs
print_success "Directories created"

# Run tests
echo "Running tests..."
if python -m pytest tests/ -v > /dev/null 2>&1; then
    print_success "Tests passed"
else
    print_warning "Some tests failed (this might be normal during initial setup)"
fi

echo ""
echo "=================================="
echo "Installation Complete!"
echo "=================================="
echo ""
echo "To get started:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Run the application:"
echo "     python -m src.main"
echo ""
echo "  3. Read the documentation:"
echo "     - README.md"
echo "     - docs/USAGE.md"
echo "     - docs/ETHICS.md  (IMPORTANT!)"
echo ""
print_warning "IMPORTANT: Read docs/ETHICS.md before using!"
echo ""
