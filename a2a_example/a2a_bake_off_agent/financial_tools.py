from google.adk.tools.tool import Tool

def get_user_profile(user_id: str) -> dict:
    """This function returns the user profile."""
    return {"user_id": user_id, "name": "John Doe", "email": "johndoe@example.com"}

def get_user_accounts(user_id: str) -> dict:
    """This function returns the user accounts."""
    return {"user_id": user_id, "accounts": [{"account_id": "123", "balance": 1000}, {"account_id": "456", "balance": 2000}]}

def get_user_transactions(user_id: str) -> dict:
    """This function returns the user transactions."""
    return {"user_id": user_id, "transactions": [{"transaction_id": "1", "amount": 100}, {"transaction_id": "2", "amount": 200}]}

def get_user_debts(user_id: str) -> dict:
    """This function returns the user debts."""
    return {"user_id": user_id, "debts": [{"debt_id": "1", "amount": 1000}, {"debt_id": "2", "amount": 2000}]}

def get_user_investments(user_id: str) -> dict:
    """This function returns the user investments."""
    return {"user_id": user_id, "investments": [{"investment_id": "1", "amount": 1000}, {"investment_id": "2", "amount": 2000}]}

def get_user_networth(user_id: str) -> dict:
    """This function returns the user networth."""
    return {"user_id": user_id, "networth": 10000}

def get_user_cashflow(user_id: str) -> dict:
    """This function returns the user cashflow."""
    return {"user_id": user_id, "cashflow": 1000}

def get_user_average_cashflow(user_id: str) -> dict:
    """This function returns the user average cashflow."""
    return {"user_id": user_id, "average_cashflow": 1000}

def get_user_goals(user_id: str) -> dict:
    """This function returns the user goals."""
    return {"user_id": user_id, "goals": [{"goal_id": "1", "name": "goal 1", "amount": 1000}, {"goal_id": "2", "name": "goal 2", "amount": 2000}]}

def update_user_goal(goal_id: str, goal_data: dict) -> dict:
    """This function updates the user goal."""
    return {"goal_id": goal_id, "goal_data": goal_data}
