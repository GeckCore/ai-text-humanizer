FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium && \
    playwright install-deps chromium

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p output logs

# Pull Ollama model (this can be done at runtime instead)
# RUN ollama serve & sleep 5 && ollama pull qwen2.5:14b

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Expose port if needed (for future API)
# EXPOSE 8000

# Default command
CMD ["python", "-m", "src.main"]

# Note: This Dockerfile is optional and experimental.
# The recommended way is to install locally with install.sh
# To use Docker:
# 1. docker build -t ai-text-humanizer .
# 2. docker run -it --rm -v $(pwd)/output:/app/output ai-text-humanizer
