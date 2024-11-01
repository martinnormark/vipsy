# Use the official Python image as a base
FROM python:3.11-slim

# Install dependencies for libvips
RUN apt-get update && \
    apt-get install -y \
    libvips-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your application code to the container
COPY . /app

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Make the script executable
RUN chmod +x vipsy/main.py

# Set the entrypoint
ENTRYPOINT ["python3", "vipsy/main.py"]

# Default command (can be overridden)
CMD ["--help"]