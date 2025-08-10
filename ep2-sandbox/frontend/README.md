# AI Financial Steward - Frontend

This directory contains the frontend for the AI Financial Steward application. It is a React application built with Vite, TypeScript, and styled with Tailwind CSS and Shadcn/UI. It provides the user interface for the mock bank and interacts with the backend API to display user data and financial information.

For more information about the overall project, please see the main [README.md](../../README.md).

## Getting Started

### Prerequisites

-   Node.js (which includes npm)
-   A running instance of the backend server. See the main [README.md](../../README.md) for instructions on how to run the backend.
-   A2A Agent service running (for chatbot functionality)

### Installation

1.  **Install dependencies:**
    ```bash
    npm install
    ```

## Environment Configuration

### Development Environment Variables

Create a `.env.local` file in the frontend root directory:

```bash
# A2A Agent API Key for development
VITE_A2A_API_KEY=your_development_api_key_here
```

**Note**: The `.env.local` file is gitignored for security. Never commit API keys to version control.

### Production Environment

No environment variables are needed in production. The frontend automatically uses the backend proxy endpoint for authentication.

## Running the Application

### Local Development

1.  **Run the frontend development server:**
    ```bash
    npm run dev
    ```
    The frontend application will be available at `http://localhost:5173` (or another port if 5173 is in use).

2.  **Test the chatbot locally:**
    - Navigate to `http://localhost:5173/dashboard?userId=user-002`
    - Try sending a message in the chatbot
    - The Vite proxy will forward requests to your A2A service using the `VITE_A2A_API_KEY`

### Production Testing

1.  **Access the deployed frontend:**
    - URL: `https://frontend-ep2-426194555180.us-west1.run.app/dashboard?userId=user-002`
    - The chatbot will automatically use the backend proxy endpoint

2.  **Verify chatbot functionality:**
    - Send a message and verify you get a response
    - Check browser console for any errors
    - Confirm authentication is working (no CORS errors)

## Service URLs and Configuration

### Current Service URLs

| Service | Environment | URL |
|---------|-------------|-----|
| **Frontend** | Production | `https://frontend-ep2-426194555180.us-west1.run.app` |
| **Backend** | Production | `https://backend-ep2-426194555180.us-west1.run.app` |
| **A2A Agent** | Production | `https://a2a-bfpwtp2iiq-uc.a.run.app` |

### How to Change Service URLs

#### 1. Frontend URL Changes

If you need to change the frontend service name or region:

1. **Update Cloud Build configuration:**
   ```yaml
   # ep2-sandbox/frontend/cloudbuild.yaml
   - name: 'gcr.io/cloud-builders/gcloud'
     args:
       - 'run'
       - 'deploy'
       - 'frontend-ep2'  # Change this service name
       - '--region'
       - 'us-west1'      # Change this region if needed
   ```

2. **Update backend CORS configuration:**
   ```python
   # ep2-sandbox/backend/code/main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://your-new-frontend-url.run.app",  # Update this
           # ... other origins
       ],
   )
   ```

3. **Update A2A service CORS configuration:**
   ```python
   # a2a_agent/main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://your-new-frontend-url.run.app",  # Update this
           # ... other origins
       ],
   )
   ```

4. **Redeploy all services:**
   ```bash
   # Deploy backend
   cd ep2-sandbox/backend
   gcloud builds submit --config cloudbuild.yaml .
   
   # Deploy A2A agent
   cd ../../a2a_agent
   ./deploy.sh agent-starter-pack-spend a2a
   
   # Deploy frontend
   cd ../ep2-sandbox/frontend
   gcloud builds submit --config cloudbuild.yaml .
   ```

#### 2. Backend URL Changes

If you need to change the backend service name or region:

1. **Update Cloud Build configuration:**
   ```yaml
   # ep2-sandbox/backend/cloudbuild.yaml
   - name: 'gcr.io/cloud-builders/gcloud'
     args:
       - 'run'
       - 'deploy'
       - 'backend-ep2'   # Change this service name
       - '--region'
       - 'us-west1'      # Change this region if needed
   ```

2. **Update frontend API endpoint:**
   ```typescript
   // ep2-sandbox/frontend/src/components/Chatbot.tsx
   const API_ENDPOINT = import.meta.env.DEV 
       ? '/api'  // Development proxy
       : 'https://your-new-backend-url.run.app/proxy/a2a';  // Update this
   ```

3. **Update A2A service audience:**
   ```python
   # ep2-sandbox/backend/code/main.py
   params = {"audience": "https://a2a-bfpwtp2iiq-uc.a.run.app"}  # Keep A2A URL
   ```

4. **Redeploy services:**
   ```bash
   # Deploy backend first
   cd ep2-sandbox/backend
   gcloud builds submit --config cloudbuild.yaml .
   
   # Deploy frontend
   cd ../frontend
   gcloud builds submit --config cloudbuild.yaml .
   ```

#### 3. A2A Agent URL Changes

If you need to change the A2A agent service name or region:

1. **Update A2A deployment:**
   ```bash
   # a2a_agent/deploy.sh
   ./deploy.sh agent-starter-pack-spend a2a
   ```

2. **Update backend audience parameter:**
   ```python
   # ep2-sandbox/backend/code/main.py
   params = {"audience": "https://your-new-a2a-url.run.app"}  # Update this
   ```

3. **Update A2A service CORS origins (if needed):**
   ```python
   # a2a_agent/main.py
   app.add_middleware(
       CORSMiddleware,
       allow_origins=[
           "https://frontend-ep2-426194555180.us-west1.run.app",  # Keep frontend URL
           # ... other origins
       ],
   )
   ```

4. **Redeploy services:**
   ```bash
   # Deploy A2A agent first
   cd a2a_agent
   ./deploy.sh agent-starter-pack-spend a2a
   
   # Deploy backend
   cd ../ep2-sandbox/backend
   gcloud builds submit --config cloudbuild.yaml .
   ```

### Testing After URL Changes

After changing any service URLs:

1. **Test the backend proxy endpoint:**
   ```bash
   curl -s -X POST -H "Content-Type: application/json" \
     -d '{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "test", "role": "user", "parts": [{"text": "Hello"}]}}, "id": "1"}' \
     https://your-new-backend-url.run.app/proxy/a2a
   ```

2. **Test the frontend chatbot:**
   - Navigate to your new frontend URL
   - Send a test message
   - Verify no CORS errors
   - Confirm you get a response

3. **Check browser console:**
   - Look for any network errors
   - Verify requests are going to correct endpoints
   - Confirm authentication is working

## Troubleshooting

### Common Issues

#### CORS Errors
- **Symptom**: `No 'Access-Control-Allow-Origin' header is present`
- **Solution**: Ensure CORS is configured on all services and URLs are updated consistently

#### Authentication Errors
- **Symptom**: `401 Unauthorized` or `403 Forbidden`
- **Solution**: Check that backend service account has `roles/run.invoker` on A2A service

#### Proxy Errors
- **Symptom**: `404 Not Found` on `/proxy/a2a`
- **Solution**: Ensure backend is deployed with the latest proxy endpoint code

### Debug Commands

#### Test Backend Health
```bash
curl https://backend-ep2-426194555180.us-west1.run.app/
```

#### Test A2A Service Directly
```bash
# Get token first
TOKEN=$(curl -s "https://backend-ep2-426194555180.us-west1.run.app/token" | jq -r '.token')

# Test A2A service
curl -s -X POST -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "test", "role": "user", "parts": [{"text": "Hello"}]}}, "id": "1"}' \
  https://a2a-bfpwtp2iiq-uc.a.run.app/
```

#### Check Service Status
```bash
# List Cloud Run services
gcloud run services list --region=us-west1
gcloud run services list --region=us-central1
```

## Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend       │    │   A2A Agent     │
│   (React)       │───▶│   (FastAPI)      │───▶│   (Cloud Run)   │
│                 │    │                  │    │                 │
│ Development:    │    │ - /token         │    │ - JSON-RPC API  │
│ Vite Proxy      │    │ - /proxy/a2a     │    │ - Authentication│
│ Production:     │    │ - CORS config    │    │ - CORS config   │
│ Backend Proxy   │    │ - Auth handling  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

- **Development**: Frontend → Vite Proxy → A2A Service
- **Production**: Frontend → Backend Proxy → A2A Service
- **Authentication**: Handled automatically by backend service account
- **CORS**: Configured on both backend and A2A services
