# Chatbot Architecture Summary

## Overview
This document explains how the AI Financial Steward chatbot works, detailing the interaction between the frontend React application, the backend FastAPI service, and the A2A (AI-to-AI) agent service.

## Architecture Components

### 1. Frontend (React + TypeScript)
- **Location**: `ep2-sandbox/frontend/`
- **Technology**: React with TypeScript, Vite build tool
- **Key Component**: `Chatbot.tsx` - Main chatbot interface component
- **URL**: `https://frontend-ep2-879168005744.us-west1.run.app`

### 2. Backend (FastAPI)
- **Location**: `ep2-sandbox/backend/`
- **Technology**: FastAPI (Python), Google Cloud Run
- **Key Endpoints**: 
  - `/proxy/a2a` - Proxies requests to A2A service
  - `/token` - Provides authentication tokens
- **URL**: `https://backend-ep2-879168005744.us-west1.run.app`

### 3. A2A Service (AI Agent)
- **Location**: `a2a_agent/`
- **Technology**: Python-based AI agent service
- **Purpose**: Processes user messages and generates AI responses
- **URL**: `https://a2a-ep2-33wwy4ha3a-uw.a.run.app`

## How It Works

### Step 1: User Interaction
1. User types a message in the chatbot interface
2. Frontend captures the message and prepares a JSON-RPC payload
3. Message is sent to the backend proxy endpoint

### Step 2: Backend Processing
1. **Authentication**: Backend automatically fetches a Google Cloud ID token from the metadata server
2. **Token Audience**: Token is specifically scoped for the A2A service
3. **Request Forwarding**: Backend forwards the user's message to the A2A service with proper authentication

### Step 3: A2A Service Response
1. A2A service receives the authenticated request
2. Processes the message using AI capabilities
3. Returns a structured response with:
   - Response text
   - Context ID for conversation continuity
   - Message artifacts and metadata

### Step 4: Response Delivery
1. Backend receives the A2A response
2. Forwards the response back to the frontend
3. Frontend displays the AI response to the user

## Key Technical Details

### Authentication Flow
```
Frontend → Backend → Google Cloud Metadata Server → A2A Service
```
- **No frontend authentication required** - Backend handles all auth
- **Service-to-service authentication** using Google Cloud ID tokens
- **Automatic token refresh** via metadata server

### Request Format (JSON-RPC 2.0)
```json
{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "messageId": "unique-id",
      "role": "user",
      "parts": [{"text": "User message"}]
    }
  },
  "id": "1"
}
```

### Response Format
```json
{
  "id": "1",
  "jsonrpc": "2.0",
  "result": {
    "artifacts": [{
      "artifactId": "uuid",
      "name": "response",
      "parts": [{"kind": "text", "text": "AI response"}]
    }],
    "contextId": "conversation-context-uuid"
  }
}
```

## Why This Architecture?

### 1. **CORS Avoidance**
- Frontend can't directly call A2A service due to CORS restrictions
- Backend acts as a proxy, eliminating CORS issues

### 2. **Security**
- Authentication tokens never exposed to frontend
- Service-to-service communication with proper IAM controls

### 3. **Scalability**
- Each component can scale independently
- Backend can handle multiple frontend instances
- A2A service can serve multiple backends

### 4. **Maintainability**
- Clear separation of concerns
- Easy to update individual components
- Centralized authentication logic

## Required Permissions

### Backend Service Account
- **`roles/run.invoker`** - Allows backend to invoke A2A service
- **`roles/vertex.ai.user`** - Provides access to AI/ML services
- **Service account**: `backend-ep2-879168005744@bake-off-hosting.iam.gserviceaccount.com`

### A2A Service
- **Public endpoint** with authentication required
- **Accepts Google Cloud ID tokens** for service-to-service auth

## Deployment URLs

| Component | Environment | URL |
|-----------|-------------|-----|
| **Frontend** | Production | `https://frontend-ep2-879168005744.us-west1.run.app` |
| **Backend** | Production | `https://backend-ep2-879168005744.us-west1.run.app` |
| **A2A Service** | Production | `https://a2a-ep2-33wwy4ha3a-uw.a.run.app` |

## Testing

### Production Flow Test
- **Script**: `ep2-sandbox/tests/test_production_flow.py`
- **Tests**: Backend health, authentication, proxy flow, frontend accessibility
- **Status**: ✅ All tests passing

### Manual Testing
- **Chatbot URL**: `https://frontend-ep2-879168005744.us-west1.run.app/dashboard?userId=user-002`
- **Direct Backend Test**: `curl -X POST "https://backend-ep2-879168005744.us-west1.run.app/proxy/a2a"`

## Troubleshooting

### Common Issues
1. **HTTP 500 on proxy endpoint**
   - Check IAM permissions (`run.invoker` role)
   - Verify A2A service URL configuration
   - Check backend logs for detailed error messages

2. **Authentication failures**
   - Verify service account has correct roles
   - Check token audience configuration
   - Ensure A2A service accepts the authentication method

3. **CORS errors**
   - Verify backend proxy is working
   - Check frontend is using backend proxy endpoint

## Benefits

✅ **User Experience**: Seamless chatbot interaction  
✅ **Security**: Proper authentication without exposing tokens  
✅ **Reliability**: Service-to-service communication with error handling  
✅ **Scalability**: Independent scaling of components  
✅ **Maintainability**: Clear architecture and separation of concerns  

---

*This architecture provides a robust, secure, and scalable foundation for AI-powered chatbot functionality in the AI Financial Steward application.*
