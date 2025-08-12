import os
import requests

API_BASE_URL = os.environ.get("API_BASE_URL", "https://backend-879168005744.us-west1.run.app/api")

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


# Updates below here only

def create_user_account(user_id: str, account_data: dict) -> dict:
    """Creates a new account for a specific user."""
    response = requests.post(f"{API_BASE_URL}/users/{user_id}/accounts", json=account_data)
    return response.json()

def get_user_transactions_with_history(user_id: str, history_days: int = 30) -> dict:
    """Retrieves all transactions for a user from the last N days."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/transactions", params={"history": history_days})
    return response.json()

def create_user_goal(goal_data: dict) -> dict:
    """Creates a new financial goal for a user."""
    response = requests.post(f"{API_BASE_URL}/goals", json=goal_data)
    return response.json()

def delete_user_goal(goal_id: str) -> dict:
    """Cancels/deletes a specific financial goal."""
    response = requests.delete(f"{API_BASE_URL}/goals/{goal_id}")
    return response.json()

def get_bank_partners() -> dict:
    """Retrieves a list of all available bank partners and their associated benefits."""
    response = requests.get(f"{API_BASE_URL}/partners")
    return response.json()

def get_user_eligible_partners(user_id: str) -> dict:
    """Identifies and returns a list of partners a specific user can benefit from."""
    response = requests.get(f"{API_BASE_URL}/partners/user/{user_id}")
    return response.json()

def create_user_schedule(user_id: str, schedule_data: dict) -> dict:
    """Creates a new scheduled transaction for a user."""
    response = requests.post(f"{API_BASE_URL}/users/{user_id}/schedules", json=schedule_data)
    return response.json()

def get_user_schedules(user_id: str) -> dict:
    """Retrieves all scheduled transactions for a specific user."""
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/schedules")
    return response.json()

def update_user_schedule(schedule_id: str, schedule_data: dict) -> dict:
    """Updates an existing scheduled transaction."""
    response = requests.put(f"{API_BASE_URL}/schedules/{schedule_id}", json=schedule_data)
    return response.json()

def delete_user_schedule(schedule_id: str) -> dict:
    """Deletes a scheduled transaction by its ID."""
    response = requests.delete(f"{API_BASE_URL}/schedules/{schedule_id}")
    return response.json()

def get_all_advisors() -> dict:
    """Gets a list of all available financial advisors."""
    response = requests.get(f"{API_BASE_URL}/advisors")
    return response.json()

def get_advisors_by_type(advisor_type: str) -> dict:
    """Gets advisors by their specialization type."""
    response = requests.get(f"{API_BASE_URL}/advisors/{advisor_type}")
    return response.json()

def schedule_meeting(meeting_data: dict) -> dict:
    """Schedules a new meeting with an advisor."""
    response = requests.post(f"{API_BASE_URL}/meetings", json=meeting_data)
    return response.json()

def get_user_meetings(user_id: str) -> dict:
    """Gets all scheduled meetings for a specific user."""
    response = requests.get(f"{API_BASE_URL}/meetings/{user_id}")
    return response.json()

def cancel_meeting(meeting_id: str) -> dict:
    """Cancels a scheduled meeting."""
    response = requests.delete(f"{API_BASE_URL}/meetings/{meeting_id}")
    return response.json()
