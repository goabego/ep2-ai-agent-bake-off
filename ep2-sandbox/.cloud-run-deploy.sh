#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Frontend Cloud Run deployment process..."

# Build the Docker image
echo "📦 Building Docker image for frontend..."
docker build --platform linux/amd64 -t frontend:latest -f Dockerfile frontend/Dockerfile

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

# Build the Docker image
echo "📦 Building Docker image for backend..."
docker build --platform linux/amd64 -t backend:latest -f Dockerfile backend/Dockerfile

# Tag the image for Artifact Registry
echo "🏷️  Tagging image for Artifact Registry..."
docker tag backend:latest us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/frontend:latest

# Push to Artifact Registry
echo "⬆️  Pushing to Artifact Registry..."
docker push us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/backend:latest

# Deploy to Cloud Run
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy backend \
  --image us-west1-docker.pkg.dev/agent-starter-pack-spend/ep2-sandbox/backend:latest \
  --platform managed \
  --region us-west1 \
  --allow-unauthenticated

echo "✅ Backend deployment complete!"
