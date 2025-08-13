import os
import json
import requests
import random


API_BASE_URL = "https://backend.ai-agent-bakeoff.com"

def get_tool_prompt() -> str:
    """
    Gets the prompt for the user.
    """
    return """
        If the user asks for details about the tools or backend services,
        Please provide your answer in a json format for the following tools. 
        Only provide the answer direct from the tool:

        **Examples for Each Tool:**

        **API Endpoints Discovery:**
        **User:** "What API endpoints are available?"
        <tool_code>
        get_all_endpoints()
        </tool_code>

        **User Profile Functions:**
        **User:** "Get all of the data schemas"
        <tool_code>
        get_all_data_schemas()
        </tool_code>

        **Note:** All tools return data in JSON format for consistency and easy parsing.
    """

def get_all_endpoints() -> dict:
    """
    Gets all the functions available in the backend.ai-agent-bakeoff API.

    Args:
    - None

    Returns:
    A list of all the functions available in the backend.ai-agent-bakeoff API.
    """
    response = requests.get(f"{API_BASE_URL}/openapi.json")
    openapi_json = response.json()
    functions = {k: v for k, v in openapi_json.get("paths", {}).items()}
    return json.dumps(functions)
# Alias for get_all_endpoints
get_all_functions = get_all_endpoints()

def get_all_data_schemas() -> dict:
    """
    Gets all the data schemas available in the backend.ai-agent-bakeoff API.

    Returns:
    A dictionary of all the data schemas defined in the backend.ai-agent-bakeoff API.
    """
    response = requests.get(f"{API_BASE_URL}/openapi.json")
    openapi_json = response.json()
    openapi_json = openapi_json.get("components", {})
    functions = {k: v for k, v in openapi_json.items()}
    return json.dumps(functions)