#!/usr/bin/env python3
"""
Debug script to test the proxy endpoint
"""

import requests
import json

BACKEND_URL = "https://backend-ep2-426194555180.us-west1.run.app"

def test_proxy_direct():
    """Test proxy endpoint directly"""
    payload = {
        "jsonrpc": "2.0",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": "test-debug",
                "role": "user",
                "parts": [{"text": "Hello debug test!"}]
            }
        },
        "id": "1"
    }
    
    print("Testing proxy endpoint directly...")
    response = requests.post(f"{BACKEND_URL}/proxy/a2a", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    return response.status_code == 200

def test_proxy_with_session():
    """Test proxy endpoint with session"""
    session = requests.Session()
    
    payload = {
        "jsonrpc": "2.0",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": "test-debug-session",
                "role": "user",
                "parts": [{"text": "Hello debug session test!"}]
            }
        },
        "id": "1"
    }
    
    print("\nTesting proxy endpoint with session...")
    response = session.post(f"{BACKEND_URL}/proxy/a2a", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
    return response.status_code == 200

if __name__ == "__main__":
    print("🔍 Debug Proxy Endpoint")
    print("=" * 30)
    
    success1 = test_proxy_direct()
    success2 = test_proxy_with_session()
    
    print("\n" + "=" * 30)
    print(f"Direct test: {'✅ PASS' if success1 else '❌ FAIL'}")
    print(f"Session test: {'✅ PASS' if success2 else '❌ FAIL'}")
    
    if success1 and success2:
        print("🎉 Both tests passed!")
    else:
        print("⚠️  Some tests failed!")
