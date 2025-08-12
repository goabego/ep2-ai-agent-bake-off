#!/usr/bin/env python3
"""
A2A Agent Test Script for Cymbal Bank Financial Tools

This script tests the A2A agent endpoint by sending predefined queries and validating:
1. The agent responds appropriately
2. The agent uses the correct financial tools
3. Response content is reasonable for financial queries

Test Endpoint: https://a2a-ep2-33wwy4ha3a-uw.a.run.app
"""

import requests
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple, Any
import sys

class A2AAgentTester:
    def __init__(self, agent_url: str = "https://a2a-ep2-33wwy4ha3a-uw.a.run.app"):
        self.agent_url = agent_url
        self.test_results = []
        self.start_time = datetime.now()
        
        # Test queries with expected tool usage patterns
        self.test_cases = [
            {
                "name": "User Profile Query",
                "query": "What's my financial profile?",
                "expected_tools": ["get_user_profile"],
                "expected_content": ["user_id", "name", "age", "risk_tolerance", "net_worth"],
                "description": "Test basic user profile retrieval"
            },
            {
                "name": "Bank Accounts Query",
                "query": "Show me my bank accounts",
                "expected_tools": ["get_user_accounts"],
                "expected_content": ["account_id", "balance", "type", "category"],
                "description": "Test account listing functionality"
            },
            {
                "name": "Recent Transactions Query",
                "query": "What are my recent transactions?",
                "expected_tools": ["get_user_transactions"],
                "expected_content": ["transaction_id", "amount", "description", "date"],
                "description": "Test transaction history retrieval"
            },
            {
                "name": "Net Worth Query",
                "query": "Calculate my net worth",
                "expected_tools": ["get_user_networth"],
                "expected_content": ["net_worth"],
                "description": "Test net worth calculation"
            },
            {
                "name": "Cash Flow Query",
                "query": "Show my cash flow for the last 30 days",
                "expected_tools": ["get_user_cashflow"],
                "expected_content": ["cash_flow_last_30_days"],
                "description": "Test cash flow analysis"
            },
            {
                "name": "Debt Information Query",
                "query": "Show my current debts",
                "expected_tools": ["get_user_debts"],
                "expected_content": ["account_id", "balance", "category"],
                "description": "Test debt account retrieval"
            },
            {
                "name": "Investment Portfolio Query",
                "query": "What's in my investment portfolio?",
                "expected_tools": ["get_user_investments"],
                "expected_content": ["account_id", "type", "holdings"],
                "description": "Test investment account retrieval"
            },
            {
                "name": "Financial Goals Query",
                "query": "What are my financial goals?",
                "expected_tools": ["get_user_goals"],
                "expected_content": ["goal_id", "description", "target_amount", "current_amount_saved"],
                "description": "Test goal retrieval"
            },
            {
                "name": "Bank Partners Query",
                "query": "Show available bank partners",
                "expected_tools": ["get_bank_partners"],
                "expected_content": ["partner_id", "name", "benefit_type", "benefit_value"],
                "description": "Test bank partner listing"
            },
            {
                "name": "Scheduled Transactions Query",
                "query": "Show my scheduled transactions",
                "expected_tools": ["get_user_schedules"],
                "expected_content": ["schedule_id", "description", "amount", "frequency"],
                "description": "Test scheduled transaction retrieval"
            },
            {
                "name": "Financial Advisors Query",
                "query": "Show available financial advisors",
                "expected_tools": ["get_all_advisors"],
                "expected_content": ["advisor_id", "name", "advisor_type"],
                "description": "Test advisor listing"
            },
            {
                "name": "Complex Financial Query",
                "query": "Give me a complete overview of my financial situation",
                "expected_tools": ["get_user_profile", "get_user_accounts", "get_user_networth"],
                "expected_content": ["user_id", "balance", "net_worth"],
                "description": "Test complex multi-tool query handling"
            }
        ]

    def send_query_to_agent(self, query: str) -> Dict[str, Any]:
        """Send a query to the A2A agent and return the response."""
        try:
            # Prepare the request payload for A2A agent
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "chat",
                "params": {
                    "skill": "chat",
                    "input": query,
                    "inputMode": "text/plain"
                }
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(
                f"{self.agent_url}/jsonrpc",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}: {response.text}"}
                
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON response: {str(e)}"}

    def analyze_tool_usage(self, response: str) -> List[str]:
        """Analyze the response to identify which financial tools were likely used."""
        response_lower = response.lower()
        tools_used = []
        
        # Map tool names to response patterns
        tool_patterns = {
            "get_user_profile": ["profile", "user", "personal", "financial profile"],
            "get_user_accounts": ["account", "banking", "balance", "checking", "savings"],
            "get_user_transactions": ["transaction", "recent", "spending", "income", "activity"],
            "get_user_debts": ["debt", "liability", "owe", "credit card", "loan"],
            "get_user_investments": ["investment", "portfolio", "stocks", "bonds", "holdings"],
            "get_user_networth": ["net worth", "networth", "total", "financial position"],
            "get_user_cashflow": ["cash flow", "cashflow", "income", "expenses", "30 days"],
            "get_user_average_cashflow": ["average", "monthly", "typical", "3 months"],
            "get_user_goals": ["goal", "target", "saving", "financial goal"],
            "get_bank_partners": ["partner", "benefit", "bank partner", "offers"],
            "get_user_schedules": ["schedule", "recurring", "monthly", "automatic"],
            "get_all_advisors": ["advisor", "financial planner", "consultant", "expert"]
        }
        
        for tool, patterns in tool_patterns.items():
            if any(pattern in response_lower for pattern in patterns):
                tools_used.append(tool)
        
        return tools_used

    def validate_response_content(self, response: str, expected_content: List[str]) -> bool:
        """Validate that the response contains expected content elements."""
        response_lower = response.lower()
        found_content = []
        
        for content in expected_content:
            if content.lower() in response_lower:
                found_content.append(content)
        
        # Require at least 60% of expected content to be present
        return len(found_content) >= len(expected_content) * 0.6

    def run_single_test(self, test_case: Dict[str, Any]) -> Dict[str, Any]:
        """Run a single test case and return results."""
        print(f"Running test: {test_case['name']}")
        print(f"Query: {test_case['query']}")
        
        # Send query to agent
        start_time = time.time()
        agent_response = self.send_query_to_agent(test_case['query'])
        response_time = time.time() - start_time
        
        test_result = {
            "test_name": test_case['name'],
            "query": test_case['query'],
            "response_time": round(response_time, 2),
            "status": "FAILED",
            "details": []
        }
        
        # Check for errors
        if "error" in agent_response:
            test_result["details"].append(f"Error: {agent_response['error']}")
            return test_result
        
        # Extract the actual response text
        try:
            if "result" in agent_response and "output" in agent_response["result"]:
                response_text = agent_response["result"]["output"]
            elif "result" in agent_response:
                response_text = str(agent_response["result"])
            else:
                response_text = str(agent_response)
        except:
            response_text = str(agent_response)
        
        # Analyze tool usage
        tools_used = self.analyze_tool_usage(response_text)
        test_result["tools_used"] = tools_used
        test_result["response_text"] = response_text[:500] + "..." if len(response_text) > 500 else response_text
        
        # Validate tool usage
        tool_usage_correct = any(tool in tools_used for tool in test_case["expected_tools"])
        if tool_usage_correct:
            test_result["details"].append("✓ Correct tool usage detected")
        else:
            test_result["details"].append(f"✗ Expected tools: {test_case['expected_tools']}")
            test_result["details"].append(f"✗ Detected tools: {tools_used}")
        
        # Validate response content
        content_valid = self.validate_response_content(response_text, test_case["expected_content"])
        if content_valid:
            test_result["details"].append("✓ Response content validation passed")
        else:
            test_result["details"].append(f"✗ Expected content: {test_case['expected_content']}")
        
        # Determine overall test status
        if tool_usage_correct and content_valid:
            test_result["status"] = "PASSED"
        
        return test_result

    def run_all_tests(self) -> None:
        """Run all test cases and collect results."""
        print("🚀 Starting A2A Agent Test Suite")
        print(f"Agent Endpoint: {self.agent_url}")
        print(f"Test Cases: {len(self.test_cases)}")
        print("=" * 60)
        
        for test_case in self.test_cases:
            result = self.run_single_test(test_case)
            self.test_results.append(result)
            
            # Print immediate results
            status_icon = "✅" if result["status"] == "PASSED" else "❌"
            print(f"{status_icon} {result['test_name']} - {result['status']} ({result['response_time']}s)")
            print()
        
        self.generate_report()

    def generate_report(self) -> None:
        """Generate and save test report."""
        end_time = datetime.now()
        total_duration = (end_time - self.start_time).total_seconds()
        
        # Calculate summary statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r["status"] == "PASSED")
        failed_tests = total_tests - passed_tests
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        # Generate console summary
        print("=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Success Rate: {success_rate:.1f}%")
        print(f"Total Duration: {total_duration:.1f} seconds")
        print("=" * 60)
        
        # Generate detailed report file
        report_filename = f"a2a_agent_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        report_path = f"ep2-sandbox/tests/{report_filename}"
        
        with open(report_path, 'w') as f:
            f.write("A2A AGENT TEST REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Agent Endpoint: {self.agent_url}\n")
            f.write(f"Total Tests: {total_tests}\n")
            f.write(f"Passed: {passed_tests}\n")
            f.write(f"Failed: {failed_tests}\n")
            f.write(f"Success Rate: {success_rate:.1f}%\n")
            f.write(f"Total Duration: {total_duration:.1f} seconds\n\n")
            
            for result in self.test_results:
                f.write(f"TEST: {result['test_name']}\n")
                f.write(f"Status: {result['status']}\n")
                f.write(f"Query: {result['query']}\n")
                f.write(f"Response Time: {result['response_time']}s\n")
                f.write(f"Tools Used: {result.get('tools_used', [])}\n")
                f.write("Details:\n")
                for detail in result['details']:
                    f.write(f"  {detail}\n")
                f.write(f"Response: {result.get('response_text', 'N/A')}\n")
                f.write("-" * 40 + "\n\n")
        
        print(f"📄 Detailed report saved to: {report_path}")

def main():
    """Main function to run the test suite."""
    if len(sys.argv) > 1:
        agent_url = sys.argv[1]
    else:
        agent_url = "https://a2a-ep2-33wwy4ha3a-uw.a.run.app"
    
    tester = A2AAgentTester(agent_url)
    tester.run_all_tests()

if __name__ == "__main__":
    main()
