# --- Stage 1: Builder (for Python dependencies) ---
FROM python:3.11-slim-bookworm AS builder

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy only the dependency definition files
COPY pyproject.toml ./

# Install dependencies into a virtual environment
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev --no-root

# --- Stage 2: Runtime ---
FROM python:3.11-slim-bookworm AS runtime

# Set the working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv/ .venv/

# Activate the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy your application code
COPY backend/ ./backend
COPY db/ ./db
COPY images/ ./images

# Expose the port the application listens on
EXPOSE 8080

# Command to run your application
# The --bind 0.0.0.0:8080 is important for Cloud Run
# The worker class is for running an ASGI app like FastAPI
CMD ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "backend.main:app"]
