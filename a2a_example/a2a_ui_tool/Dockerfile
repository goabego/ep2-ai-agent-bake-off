# Use a slim Python base image
FROM python:3.11-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the application will run on
EXPOSE 8080

# Command to run the application using Gunicorn with Uvicorn workers
CMD ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "server:app"]
