import os
import requests

API_BASE_URL = os.environ.get("API_BASE_URL", "https://backend-ep2-879168005744.us-west1.run.app/api")

def get_user_profile(user_id: str) -> dict:
    """
    Gets a user's profile.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}")
    return response.json()

def get_user_accounts(user_id: str) -> dict:
    """
    Fetches all accounts for a specific user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/accounts")
    return response.json()

def get_user_transactions(user_id: str) -> dict:
    """
    Retrieves all transactions for a user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/transactions")
    return response.json()

def get_user_debts(user_id: str) -> dict:
    """
    Retrieves all debt accounts for a user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/debts")
    return response.json()

def get_user_investments(user_id: str) -> dict:
    """
    Retrieves all investment accounts for a user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/investments")
    return response.json()

def get_user_networth(user_id: str) -> dict:
    """
    Calculates the net worth of a user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/networth")
    return response.json()

def get_user_cashflow(user_id: str) -> dict:
    """
    Calculates the cash flow for a user over the last 30 days.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/cashflow")
    return response.json()

def get_user_average_cashflow(user_id: str) -> dict:
    """
    Calculates the average monthly cash flow for a user over the last 3 months.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/average_cashflow")
    return response.json()

def get_user_goals(user_id: str) -> dict:
    """
    Retrieves a user's financial goals.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/goals")
    return response.json()

def update_user_goal(goal_id: str, goal_data: dict) -> dict:
    """
    Updates a specific financial goal.
    
    Required Inputs:
    - goal_id (str): The unique identifier for the goal (e.g., 'goal-001')
    - goal_data (dict): Dictionary containing goal fields to update
        Example: {'target_amount': 15000, 'deadline': '2026-12-31'}
    """
    response = requests.put(f"{API_BASE_URL}/goals/{goal_id}", json=goal_data)
    return response.json()


# Updates below here only

def create_user_account(user_id: str, account_data: dict) -> dict:
    """
    Creates a new account for a specific user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    - account_data (dict): Dictionary containing account information
        Example: {
            'type': 'savings',
            'description': 'Emergency Fund',
            'balance': 0,
            'institution': 'Cymbal Bank'
        }
    """
    response = requests.post(f"{API_BASE_URL}/users/{user_id}/accounts", json=account_data)
    return response.json()

def get_user_transactions_with_history(user_id: str, history_days: int = 30) -> dict:
    """
    Retrieves all transactions for a user from the last N days.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    - history_days (int): Number of days to look back (default: 30)
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/transactions", params={"history": history_days})
    return response.json()

def create_user_goal(goal_data: dict) -> dict:
    """
    Creates a new financial goal for a user.
    
    Required Inputs:
    - goal_data (dict): Dictionary containing goal information
        Example: {
            'user_id': 'user-001',
            'description': 'Save $10,000',
            'target_amount': 10000,
            'target_date': '2025-12-31',
            'current_amount_saved': 0
        }
    """
    response = requests.post(f"{API_BASE_URL}/goals", json=goal_data)
    return response.json()

def delete_user_goal(goal_id: str) -> dict:
    """
    Cancels/deletes a specific financial goal.
    
    Required Inputs:
    - goal_id (str): The unique identifier for the goal (e.g., 'goal-001')
    """
    response = requests.delete(f"{API_BASE_URL}/goals/{goal_id}")
    return response.json()

def get_bank_partners() -> dict:
    """
    Retrieves a list of all available bank partners and their associated benefits.
    
    Required Inputs:
    - None (no parameters required)
    """
    response = requests.get(f"{API_BASE_URL}/partners")
    return response.json()

def get_user_eligible_partners(user_id: str) -> dict:
    """
    Identifies and returns a list of partners a specific user can benefit from.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/partners/user/{user_id}")
    return response.json()

def create_user_schedule(user_id: str, schedule_data: dict) -> dict:
    """
    Creates a new scheduled transaction for a user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    - schedule_data (dict): Dictionary containing schedule information
        Example: {
            'source_account_id': 'acc-001',
            'destination_account_id': 'acc-002',
            'description': 'Monthly Savings',
            'frequency': 'monthly',
            'amount': 500
        }
    """
    response = requests.post(f"{API_BASE_URL}/users/{user_id}/schedules", json=schedule_data)
    return response.json()

def get_user_schedules(user_id: str) -> dict:
    """
    Retrieves all scheduled transactions for a specific user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/users/{user_id}/schedules")
    return response.json()

def update_user_schedule(schedule_id: str, schedule_data: dict) -> dict:
    """
    Updates an existing scheduled transaction.
    
    Required Inputs:
    - schedule_id (str): The unique identifier for the schedule (e.g., 'schedule-001')
    - schedule_data (dict): Dictionary containing schedule fields to update
        Example: {'amount': 600, 'frequency': 'bi-weekly'}
    """
    response = requests.put(f"{API_BASE_URL}/schedules/{schedule_id}", json=schedule_data)
    return response.json()

def delete_user_schedule(schedule_id: str) -> dict:
    """
    Deletes a scheduled transaction by its ID.
    
    Required Inputs:
    - schedule_id (str): The unique identifier for the schedule (e.g., 'schedule-001')
    """
    response = requests.delete(f"{API_BASE_URL}/schedules/{schedule_id}")
    return response.json()

def get_all_advisors() -> dict:
    """
    Gets a list of all available financial advisors.
    
    Required Inputs:
    - None (no parameters required)
    """
    response = requests.get(f"{API_BASE_URL}/advisors")
    return response.json()

def get_advisors_by_type(advisor_type: str) -> dict:
    """
    Gets advisors by their specialization type.
    
    Required Inputs:
    - advisor_type (str): The type of advisor specialization
        Examples: 'financial_planner', 'investment_advisor', 'tax_advisor'
    """
    response = requests.get(f"{API_BASE_URL}/advisors/{advisor_type}")
    return response.json()

def schedule_meeting(meeting_data: dict) -> dict:
    """
    Schedules a new meeting with an advisor.
    
    Required Inputs:
    - meeting_data (dict): Dictionary containing meeting information
        Example: {
            'user_id': 'user-001',
            'advisor_id': 'adv-001',
            'advisor_name': 'John Smith',
            'advisor_type': 'financial_planner',
            'meeting_time': '2024-12-20T10:00:00'
        }
    """
    response = requests.post(f"{API_BASE_URL}/meetings", json=meeting_data)
    return response.json()

def get_user_meetings(user_id: str) -> dict:
    """
    Gets all scheduled meetings for a specific user.
    
    Required Inputs:
    - user_id (str): The unique identifier for the user (e.g., 'user-001')
    """
    response = requests.get(f"{API_BASE_URL}/meetings/{user_id}")
    return response.json()

def cancel_meeting(meeting_id: str) -> dict:
    """
    Cancels a scheduled meeting.
    
    Required Inputs:
    - meeting_id (str): The unique identifier for the meeting (e.g., 'meet-001')
    """
    response = requests.delete(f"{API_BASE_URL}/meetings/{meeting_id}")
    return response.json()
