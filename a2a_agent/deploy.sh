#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <PROJECT_ID> <SERVICE_NAME> <REGION>"
    exit 1
fi

PROJECT_ID=$1
SERVICE_NAME=$2
REGION=$3 

BACKEND_URL="https://backend-ep2-879168005744.us-west1.run.app"
FRONTEND_URL="https://frontend-ep2-879168005744.us-west1.run.app"

# The memory to allocate to the service
MEMORY="1Gi"

# --- Deployment ---

echo "Starting deployment of service '$SERVICE_NAME' to project '$PROJECT_ID' in region '$REGION'..."

# Deploy to Cloud Run from source code
gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --project "$PROJECT_ID" \
  --region "$REGION" \
  --memory "$MEMORY" \
  --allow-unauthenticated \
  --set-env-vars=GOOGLE_CLOUD_PROJECT="$PROJECT_ID",GOOGLE_CLOUD_LOCATION="$REGION",GOOGLE_GENAI_USE_VERTEXAI=TRUE,MODEL="gemini-2.5-flash",FRONTEND_URL="$FRONTEND_URL",BACKEND_URL="$BACKEND_URL"


echo "Deployment complete."
echo "Service URL: $(gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --project $PROJECT_ID --format 'value(status.url)')"

# After the initial deployment, get the service URL
SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --project="$PROJECT_ID" --region="$REGION" --format='value(status.url)')

# Update the service to set the AGENT_URL environment variable
echo "Updating service with its public URL: $SERVICE_URL"
gcloud run services update "$SERVICE_NAME"   --project="$PROJECT_ID"   --region="$REGION"   --update-env-vars=AGENT_URL=$SERVICE_URL


# # Get the token from the backend
# TOKEN=$(curl -s ${BACKEND_URL}/token | jq -r '.token')

# # Do a quick curl test
# echo "Doing a quick curl test to verify the service is working"
# curl -X POST \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer $TOKEN" \
# -d '{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "a-random-id", "role": "user", "parts": [{"text": "What is my user profile?"}]}}, "id": "1"}' \
# ${SERVICE_URL}

# # Test CORS preflight
# echo "Testing CORS preflight request..."
# curl -X OPTIONS \
# -H "Origin: $FRONTEND_URL" \
# -H "Access-Control-Request-Method: POST" \
# -H "Access-Control-Request-Headers: Content-Type,Authorization" \
# -v ${SERVICE_URL}
