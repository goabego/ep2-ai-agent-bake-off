import os
import requests

API_BASE_URL = os.environ.get("API_BASE_URL", "https://backend-426194555180.us-west1.run.app/api")

def get_user_profile(user_id: str) -> dict:
    """Gets a user's profile."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}")
    return response.json()

def get_user_accounts(user_id: str) -> dict:
    """Fetches all accounts for a specific user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/accounts")
    return response.json()

def get_user_transactions(user_id: str) -> dict:
    """Retrieves all transactions for a user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/transactions")
    return response.json()

def get_user_debts(user_id: str) -> dict:
    """Retrieves all debt accounts for a user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/debts")
    return response.json()

def get_user_investments(user_id: str) -> dict:
    """Retrieves all investment accounts for a user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/investments")
    return response.json()

def get_user_networth(user_id: str) -> dict:
    """Calculates the net worth of a user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/networth")
    return response.json()

def get_user_cashflow(user_id: str) -> dict:
    """Calculates the cash flow for a user over the last 30 days."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/cashflow")
    return response.json()

def get_user_average_cashflow(user_id: str) -> dict:
    """Calculates the average monthly cash flow for a user over the last 3 months."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/average_cashflow")
    return response.json()

def get_user_goals(user_id: str) -> dict:
    """Retrieves a user's financial goals."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/goals")
    return response.json()

def update_user_goal(goal_id: str, goal_data: dict) -> dict:
    """Updates a specific financial goal."""
    response = requests.put(f"{API_BASE_URL}/goals/{goal_id}", json=goal_data)
    return response.json()
