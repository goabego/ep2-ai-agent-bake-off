#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Frontend Cloud Run deployment process..."

# Navigate to the frontend directory
cd frontend

# Build the Docker image
echo "📦 Building Docker image for frontend..."
docker build --platform linux/amd64 -t frontend:latest -f Dockerfile .

# Tag the image for Artifact Registry
echo "🏷️  Tagging image for Artifact Registry..."
docker tag frontend:latest us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/frontend:latest

# Push to Artifact Registry
echo "⬆️  Pushing to Artifact Registry..."
docker push us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/frontend:latest

# Deploy to Cloud Run
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy frontend \
  --image us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/frontend:latest \
  --platform managed \
  --region us-west1 \
  --allow-unauthenticated

echo "✅ Frontend deployment complete!"
