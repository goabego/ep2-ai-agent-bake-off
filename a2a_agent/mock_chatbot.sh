#!/bin/bash

# Ask users for A2A Agent URL
SERVICE_URL="https://a2a-426194555180.us-central1.run.app"

echo "🤖 A2A Agent Mock Chatbot"
echo "=========================="
echo "Service URL: $SERVICE_URL"
echo ""

# Generate token
echo "🔑 Generating authentication token..."
TOKEN=$(gcloud auth print-identity-token)
if [ $? -ne 0 ]; then
    echo "❌ Failed to generate token. Make sure you're authenticated with gcloud."
    exit 1
fi
echo "✅ Token generated successfully"
echo ""

# Function to send message
send_message() {
    local message="$1"
    local message_id=$(uuidgen 2>/dev/null || echo "msg-$(date +%s)")
    
    echo "📤 Sending message: '$message'"
    echo "----------------------------------------"
    
    response=$(curl -s -X POST ${SERVICE_URL} \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $TOKEN" \
        -d "{
            \"jsonrpc\": \"2.0\",
            \"method\": \"message/send\",
            \"params\": {
                \"message\": {
                    \"messageId\": \"$message_id\",
                    \"role\": \"user\",
                    \"parts\": [
                        {
                            \"text\": \"$message\"
                        }
                    ]
                }
            },
            \"id\": \"user-001\"
        }")
    
    echo "📥 Response:"
    echo "$response" | jq '.' 2>/dev/null || echo "$response"
    echo ""
}

# Interactive mode
echo "💬 Interactive mode - type your messages (or 'quit' to exit)"
echo ""

while true; do
    read -p "You: " user_message
    
    if [ "$user_message" = "quit" ] || [ "$user_message" = "exit" ]; then
        echo "👋 Goodbye!"
        break
    fi
    
    if [ -n "$user_message" ]; then
        send_message "$user_message"
    fi
done

