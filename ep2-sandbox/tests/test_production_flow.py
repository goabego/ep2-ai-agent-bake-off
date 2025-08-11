#!/usr/bin/env python3
"""
Production Flow Test Script
Tests the complete chatbot flow in production environment
"""

import requests
import json
import sys
import time
from typing import Dict, Any

# # Production URLs
# BACKEND_URL = "https://backend-ep2-426194555180.us-west1.run.app"
# FRONTEND_URL = "https://frontend-ep2-426194555180.us-west1.run.app"
# A2A_URL = "https://a2a-bfpwtp2iiq-uc.a.run.app"

# Production URLs
BACKEND_URL = "https://backend-ep2-879168005744.us-west1.run.app"
FRONTEND_URL = "https://frontend-ep2-879168005744.us-west1.run.app"
A2A_URL = "https://a2a-33wwy4ha3a-uc.a.run.app"

class ProductionTester:
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name: str, success: bool, details: str = ""):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   {details}")
        self.test_results.append({
            "test": test_name,
            "success": success,
            "details": details
        })
        return success
    
    def test_backend_health(self) -> bool:
        """Test backend health endpoint"""
        try:
            response = self.session.get(f"{BACKEND_URL}/")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "ok":
                    return self.log_test("Backend Health Check", True, f"Status: {data.get('message')}")
                else:
                    return self.log_test("Backend Health Check", False, f"Unexpected response: {data}")
            else:
                return self.log_test("Backend Health Check", False, f"HTTP {response.status_code}")
        except Exception as e:
            return self.log_test("Backend Health Check", False, f"Error: {str(e)}")
    
    def test_backend_token(self) -> bool:
        """Test backend token endpoint"""
        try:
            response = self.session.get(f"{BACKEND_URL}/token")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success" and data.get("token"):
                    token_length = len(data["token"])
                    return self.log_test("Backend Token Endpoint", True, f"Token received ({token_length} chars)")
                else:
                    return self.log_test("Backend Token Endpoint", False, f"Invalid response: {data}")
            else:
                return self.log_test("Backend Token Endpoint", False, f"HTTP {response.status_code}")
        except Exception as e:
            return self.log_test("Backend Token Endpoint", False, f"Error: {str(e)}")
    
    def test_frontend_accessibility(self) -> bool:
        """Test frontend accessibility"""
        try:
            response = self.session.get(f"{FRONTEND_URL}/")
            if response.status_code == 200:
                if "Vite + React + TS" in response.text:
                    return self.log_test("Frontend Accessibility", True, "Frontend HTML loaded successfully")
                else:
                    return self.log_test("Frontend Accessibility", False, "Expected content not found in HTML")
            else:
                return self.log_test("Frontend Accessibility", False, f"HTTP {response.status_code}")
        except Exception as e:
            return self.log_test("Frontend Accessibility", False, f"Error: {str(e)}")
    
    def test_a2a_direct_access(self) -> bool:
        """Test direct A2A service access (should fail without auth)"""
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "message/send",
                "params": {
                    "message": {
                        "messageId": "test-direct-access",
                        "role": "user",
                        "parts": [{"text": "Hello"}]
                    }
                },
                "id": "1"
            }
            
            response = self.session.post(A2A_URL, json=payload)
            # Should fail without auth (401 or 403)
            if response.status_code in [401, 403]:
                return self.log_test("A2A Direct Access (No Auth)", True, f"Correctly blocked: HTTP {response.status_code}")
            else:
                return self.log_test("A2A Direct Access (No Auth)", False, f"Unexpected response: HTTP {response.status_code}")
        except Exception as e:
            return self.log_test("A2A Direct Access (No Auth)", False, f"Error: {str(e)}")
    
    def test_backend_proxy_flow(self) -> bool:
        """Test the complete backend proxy flow to A2A"""
        try:
            # Test proxy endpoint directly (backend handles authentication internally)
            payload = {
                "jsonrpc": "2.0",
                "method": "message/send",
                "params": {
                    "message": {
                        "messageId": "test-proxy-flow",
                        "role": "user",
                        "parts": [{"text": "Hello from production test!"}]
                    }
                },
                "id": "1"
            }
            
            print(f"DEBUG: Making request to {BACKEND_URL}/proxy/a2a")
            print(f"DEBUG: Payload: {json.dumps(payload, indent=2)}")
            
            proxy_response = self.session.post(f"{BACKEND_URL}/proxy/a2a", json=payload)
            print(f"DEBUG: Response status: {proxy_response.status_code}")
            print(f"DEBUG: Response headers: {dict(proxy_response.headers)}")
            print(f"DEBUG: Response text: {proxy_response.text[:200]}...")
            
            if proxy_response.status_code == 200:
                proxy_data = proxy_response.json()
                if proxy_data.get("result") and proxy_data["result"].get("artifacts"):
                    response_text = proxy_data["result"]["artifacts"][0]["parts"][0]["text"]
                    return self.log_test("Backend Proxy Flow", True, f"A2A Response: {response_text[:50]}...")
                else:
                    return self.log_test("Backend Proxy Flow", False, f"Invalid proxy response: {proxy_data}")
            else:
                return self.log_test("Backend Proxy Flow", False, f"Proxy failed: HTTP {proxy_response.status_code}")
                
        except Exception as e:
            return self.log_test("Backend Proxy Flow", False, f"Error: {str(e)}")
    
    def test_frontend_dashboard(self) -> bool:
        """Test frontend dashboard page"""
        try:
            response = self.session.get(f"{FRONTEND_URL}/dashboard?userId=user-002")
            if response.status_code == 200:
                if "dashboard" in response.text.lower() or "react" in response.text.lower():
                    return self.log_test("Frontend Dashboard", True, "Dashboard page loaded successfully")
                else:
                    return self.log_test("Frontend Dashboard", False, "Dashboard content not found")
            else:
                return self.log_test("Frontend Dashboard", False, f"HTTP {response.status_code}")
        except Exception as e:
            return self.log_test("Frontend Dashboard", False, f"Error: {str(e)}")
    
    def run_all_tests(self) -> bool:
        """Run all production tests"""
        print("🚀 Starting Production Flow Tests...")
        print("=" * 50)
        
        tests = [
            self.test_backend_health,
            self.test_backend_token,
            self.test_frontend_accessibility,
            self.test_a2a_direct_access,
            self.test_backend_proxy_flow,
            self.test_frontend_dashboard
        ]
        
        all_passed = True
        for test in tests:
            if not test():
                all_passed = False
            time.sleep(1)  # Small delay between tests
        
        print("=" * 50)
        self.print_summary()
        
        return all_passed
    
    def print_summary(self):
        """Print test summary"""
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results if result["success"])
        failed_tests = total_tests - passed_tests
        
        print(f"\n📊 Test Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {failed_tests}")
        
        if failed_tests > 0:
            print(f"\n❌ Failed Tests:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"   - {result['test']}: {result['details']}")
        
        if passed_tests == total_tests:
            print(f"\n🎉 All tests passed! Your production deployment is working correctly.")
            print(f"🌐 Frontend: {FRONTEND_URL}")
            print(f"🔧 Backend: {BACKEND_URL}")
            print(f"🤖 A2A Service: {A2A_URL}")
            print(f"💡 Test the chatbot at: {FRONTEND_URL}/dashboard?userId=user-002")
        else:
            print(f"\n⚠️  Some tests failed. Please check the deployment and configuration.")

def main():
    """Main function"""
    tester = ProductionTester()
    
    try:
        success = tester.run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
