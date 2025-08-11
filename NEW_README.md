# Deploying the Services

This document explains how to deploy the three services (`a2a_agent`, `backend`, `frontend`) with configurable URLs.

## Prerequisites

- Google Cloud SDK (`gcloud`) installed and authenticated.
- A Google Cloud project with the Cloud Run and Cloud Build APIs enabled.

## Deploying the `a2a_agent` Service

The `a2a_agent` service now requires the `FRONTEND_URL` to be passed as an argument to the deployment script.

To deploy the `a2a_agent` service, run the following command from the `a2a_agent` directory:

```bash
./deploy.sh <PROJECT_ID> <SERVICE_NAME> <FRONTEND_URL>
```

**Example:**

```bash
./deploy.sh my-gcp-project a2a-agent-prod https://my-frontend-url.run.app
```

## Deploying the `backend` Service

The `backend` service now requires the `A2A_AGENT_URL` to be passed as a substitution variable to the Cloud Build pipeline.

To deploy the `backend` service, run the following command from the `ep2-sandbox/backend` directory:

```bash
gcloud builds submit --config cloudbuild.yaml --substitutions=_A2A_AGENT_URL=<YOUR_A2A_AGENT_URL>
```

**Example:**

```bash
gcloud builds submit --config cloudbuild.yaml --substitutions=_A2A_AGENT_URL=https://my-a2a-agent-url.run.app
```

## Deploying the `frontend` Service

The `frontend` service now requires the `VITE_API_URL` and `VITE_TOKEN_URL` to be passed as substitution variables to the Cloud Build pipeline.

To deploy the `frontend` service, run the following command from the `ep2-sandbox/frontend` directory:

```bash
gcloud builds submit --config cloudbuild.yaml --substitutions=_VITE_API_URL=<YOUR_BACKEND_API_URL>,_VITE_TOKEN_URL=<YOUR_BACKEND_TOKEN_URL>
```

**Example:**

```bash
gcloud builds submit --config cloudbuild.yaml --substitutions=_VITE_API_URL=https://my-backend-url.run.app/api,_VITE_TOKEN_URL=https://my-backend-url.run.app/token
```
