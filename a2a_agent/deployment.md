# Deploying the Financial Agent to Google Cloud Run

This document provides instructions on how to deploy the financial agent to Google Cloud Run.

## Prerequisites

Before you can deploy the agent, you will need to have the following installed and configured:

*   [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
*   An active Google Cloud project

## Deployment Steps

To deploy the agent, you will need to run the `deploy.sh` script from within the `to_deploy` directory. This script will build a container image, push it to the Google Container Registry, and deploy it to Cloud Run.

To run the script, you will need to provide your Google Cloud project ID and a name for your service. For example:

```bash
bash deploy.sh my-gcp-project my-financial-agent
```

Once the script has finished, it will output the URL of your newly deployed service.

## Environment Variables

The `deploy.sh` script will automatically set the following environment variables:

*   `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID.
*   `GOOGLE_CLOUD_LOCATION`: The region where the service is deployed (`us-central1`).
*   `GOOGLE_GENAI_USE_VERTEXAI`: Set to `TRUE` to use Vertex AI.
*   `MODEL`: The name of the Gemini model to use (`gemini-pro-2.5`).
*   `AGENT_URL`: The public URL of your deployed service.

## Accessing the Agent

Once the agent is deployed, you can interact with it by sending JSON-RPC 2.0 requests to the service URL. For example, you can use `curl` to send a request to the agent:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "a-random-id", "role": "user", "parts": [{"text": "What is my user profile?"}]}}, "id": "1"}' <YOUR_SERVICE_URL>
```

Replace `<YOUR_SERVICE_URL>` with the URL of your deployed service.

## Accessing the Agent (Authenticated)

Since the service is deployed with `--no-allow-unauthenticated`, you need to provide an identity token to make requests.

First, get a token:

```bash
TOKEN=$(gcloud auth print-identity-token)
```

Then, use the token in your `curl` command:

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $TOKEN" \
-d '{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "a-random-id", "role": "user", "parts": [{"text": "What is my user profile?"}]}}, "id": "1"}' \
${SERVICE_URL}
```

Replace `<SERVICE_URL>` with the URL of your deployed service.