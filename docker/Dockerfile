FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY pan_os_upgrade/ ./pan_os_upgrade/
COPY pyproject.toml .

# Create a non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Set the entry point
ENTRYPOINT ["python", "-m", "pan_os_upgrade"]
CMD ["--help"]