# agent/tools/financial_tools.py

import requests
import json
from typing import Dict, Any, List

# Assuming the FastAPI server is running locally on the default port
BASE_URL = "http://127.0.0.1:8000/api"

def get_user(user_id: str) -> Dict[str, Any]:
    """
    Retrieves a user's profile from the API.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

def get_user_accounts(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves all financial accounts for a given user from the API.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}/accounts")
    response.raise_for_status()
    return response.json()

def get_user_goals(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves the financial goals for a given user from the API.
    """
    response = requests.get(f"{BASE_URL}/goals/{user_id}")
    response.raise_for_status()
    return response.json()

def get_user_transactions(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves all transactions for a given user from the API.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}/transactions")
    response.raise_for_status()
    return response.json()

def update_goal(goal_id: str, updated_goal_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates a user's financial goal using the API.
    """
    response = requests.put(
        f"{BASE_URL}/goals/{goal_id}",
        data=json.dumps(updated_goal_data),
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return response.json()
