#!/usr/bin/env python3
"""
A2A Agent Mock Chatbot - Python Version
Sends messages to the A2A Agent service via HTTP POST requests
"""

import json
import subprocess
import sys
from typing import Optional


class A2AAgentChatbot:
    def __init__(self, service_url: str):
        self.service_url = service_url
        self.token = None
    
    def generate_token(self) -> bool:
        """Generate Google Cloud authentication token"""
        try:
            print("🔑 Generating authentication token...")
            result = subprocess.run(
                ["gcloud", "auth", "print-identity-token"],
                capture_output=True,
                text=True,
                check=True
            )
            self.token = result.stdout.strip()
            print("✅ Token generated successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate token: {e}")
            print("Make sure you're authenticated with gcloud: gcloud auth login")
            return False
        except FileNotFoundError:
            print("❌ gcloud CLI not found. Please install Google Cloud SDK")
            return False
    
    def send_message(self, message: str) -> Optional[dict]:
        """Send a message to the A2A Agent service"""
        if not self.token:
            print("❌ No authentication token available")
            return None
        
        import requests
        
        message_id = f"msg-{int(subprocess.run(['date', '+%s'], capture_output=True, text=True).stdout.strip())}"
        
        payload = {
            "jsonrpc": "2.0",
            "method": "message/send",
            "params": {
                "message": {
                    "messageId": message_id,
                    "role": "user",
                    "parts": [
                        {
                            "text": message
                        }
                    ]
                }
            },
            "id": "user-001"
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        
        try:
            # print(f"📤 Sending message: '{message}'")
            # print("----------------------------------------")
            
            response = requests.post(
                self.service_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            print("📥 Response:")
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    pretty_text = ""
                    # Extract and pretty print only the text content
                    if response_json['result']:
                        pretty_text = response_json['result']['artifacts'][0]['parts'][0]['text']
                    else:
                        pretty_text = response_json
                        # Fallback to full response if structure is different
                        print(json.dumps(pretty_text, indent=2))
                    
                    print(json.dumps(pretty_text, indent=2))
                    return response_json
                except json.JSONDecodeError:
                    print(response.text)
            else:
                print(f"❌ HTTP {response.status_code}: {response.text}")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        
        return None
    
    def run_interactive(self):
        """Run the chatbot in interactive mode"""
        print("🤖 A2A Agent Mock Chatbot (Python)")
        print("=====================================")
        print(f"Service URL: {self.service_url}")
        print()
        
        if not self.generate_token():
            return
        
        print("💬 Interactive mode - type your messages (or 'quit' to exit)")
        print()
        
        while True:
            try:
                user_message = input("You: ").strip()
                
                if user_message.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if user_message:
                    self.send_message(user_message)
                    print()
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break


def main():
    service_url = "https://a2a-426194555180.us-central1.run.app"
    
    # Check if requests is available
    try:
        import requests
    except ImportError:
        print("❌ requests library not found. Install it with: pip install requests")
        sys.exit(1)
    
    chatbot = A2AAgentChatbot(service_url)
    chatbot.run_interactive()


if __name__ == "__main__":
    main() 