#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting Cloud Run deployment process..."

A2A_URL="https://a2a-ep2-33wwy4ha3a-uw.a.run.app"
BACKEND_URL="https://backend-ep2-879168005744.us-west1.run.app"
FRONTEND_URL="https://frontend-ep2-879168005744.us-west1.run.app"

# Deploy Backend first (since frontend depends on it)
echo "📦 Deploying Backend..."
cd backend
gcloud builds submit --config cloudbuild.yaml .
echo "✅ Backend deployment complete!"

# Deploy Frontend
echo "📦 Deploying Frontend..."
cd ../frontend
gcloud builds submit --config cloudbuild.yaml .
echo "✅ Frontend deployment complete!"

# Wait a moment for services to be fully ready
echo "⏳ Waiting for services to be ready..."
sleep 30

# Simple tests to verify deployment
echo "🧪 Running deployment tests..."

# Test 1: Backend health check
echo "🔍 Testing Backend health..."
if curl -s "$BACKEND_URL/" | grep -q "Welcome to the AI Financial Steward API"; then
    echo "✅ Backend health check passed"
else
    echo "❌ Backend health check failed"
    exit 1
fi

# Test 2: Backend token endpoint
echo "🔍 Testing Backend token endpoint..."
if curl -s "$BACKEND_URL/token" | grep -q "token"; then
    echo "✅ Backend token endpoint working"
else
    echo "❌ Backend token endpoint failed"
    exit 1
fi

# Test 3: Frontend accessibility
echo "🔍 Testing Frontend accessibility..."
if curl -s "$FRONTEND_URL/" | grep -q "Vite + React + TS"; then
    echo "✅ Frontend accessibility check passed"
else
    echo "❌ Frontend accessibility check failed"
    exit 1
fi

# Test 4: Test chatbot authentication flow
echo "🔍 Testing Chatbot authentication flow..."
TOKEN_RESPONSE=$(curl -s "$BACKEND_URL/token")
TOKEN=$(echo "$TOKEN_RESPONSE" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

if [ -n "$TOKEN" ]; then
    echo "✅ Successfully obtained authentication token"
    
    # Test A2A service with token
    TEST_PAYLOAD='{"jsonrpc": "2.0", "method": "message/send", "params": {"message": {"messageId": "test-deploy", "role": "user", "parts": [{"text": "Hello"}]}}, "id": "1"}'
    
    if curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" -d "$TEST_PAYLOAD" "$A2A_URL" | grep -q "result"; then
        echo "✅ A2A service authentication test passed"
    else
        echo "❌ A2A service authentication test failed"
        exit 1
    fi
else
    echo "❌ Failed to obtain authentication token"
    exit 1
fi

echo ""
echo "🎉 All deployment tests passed!"
echo "🌐 Frontend: $FRONTEND_URL"
echo "🔧 Backend: $BACKEND_URL"
echo "🤖 A2A Agent: $A2A_URL"
echo ""
echo "💡 Test the chatbot at: $FRONTEND_URL/dashboard?userId=user-001"
