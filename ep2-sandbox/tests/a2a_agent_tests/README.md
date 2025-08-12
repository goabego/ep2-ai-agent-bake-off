# A2A Agent Test Suite

This directory contains comprehensive testing tools for the Cymbal Bank A2A Agent.

## Test Scripts

### `test_a2a_agent.py` - Main A2A Agent Test Suite

A comprehensive test script that validates the A2A agent's ability to:
- Respond to financial queries appropriately
- Use the correct financial tools for each query type
- Provide reasonable financial information in responses

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run with default endpoint:
```bash
python test_a2a_agent.py
```

### Run with custom endpoint:
```bash
python test_a2a_agent.py "https://your-custom-endpoint.com"
```

## Test Coverage

The test suite covers 12 key financial scenarios:

1. **User Profile Query** - Tests basic profile retrieval
2. **Bank Accounts Query** - Tests account listing
3. **Recent Transactions Query** - Tests transaction history
4. **Net Worth Query** - Tests net worth calculation
5. **Cash Flow Query** - Tests cash flow analysis
6. **Debt Information Query** - Tests debt account retrieval
7. **Investment Portfolio Query** - Tests investment accounts
8. **Financial Goals Query** - Tests goal retrieval
9. **Bank Partners Query** - Tests partner listing
10. **Scheduled Transactions Query** - Tests schedule retrieval
11. **Financial Advisors Query** - Tests advisor listing
12. **Complex Financial Query** - Tests multi-tool usage

## Output

- **Console Output**: Real-time test results with pass/fail indicators
- **Test Report**: Detailed report saved as timestamped .txt file
- **Success Rate**: Overall test performance metrics

## Validation Criteria

### Tool Usage Validation (Primary)
- Detects which financial tools the agent uses based on response patterns
- Compares against expected tool usage for each query type
- **This is the primary focus** - ensuring the agent uses the right tools

### Content Validation (Secondary)
- Validates that responses contain expected financial data elements
- Requires 60% of expected content to be present
- Ensures responses are relevant to financial queries

## Example Test Case

```python
{
    "name": "Net Worth Query",
    "query": "Calculate my net worth",
    "expected_tools": ["get_user_networth"],
    "expected_content": ["net_worth"],
    "description": "Test net worth calculation"
}
```

## Troubleshooting

- **Connection Issues**: Verify the agent endpoint is accessible
- **Timeout Errors**: Increase timeout in the script if needed
- **Tool Detection**: Check response patterns if tool usage isn't detected correctly

## Customization

You can modify the test cases in the `test_cases` list to:
- Add new financial scenarios
- Adjust expected tool usage patterns
- Modify content validation requirements
- Change query language or complexity
