import json
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from datetime import datetime, timedelta

router = APIRouter()

def load_data(file_name: str) -> List[Dict[str, Any]]:
    try:
        with open(f"db/{file_name}", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"{file_name} not found")

@router.get("/users/{user_id}/debts", tags=["Financials"])
def get_user_debts(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves all debt accounts for a specific user.
    """
    accounts = load_data("accounts.json")
    debt_accounts = [
        acc for acc in accounts if acc["user_id"] == user_id and acc["type"] == "debt"
    ]
    if not debt_accounts:
        raise HTTPException(status_code=404, detail="No debt accounts found for this user")
    return debt_accounts

@router.get("/users/{user_id}/investments", tags=["Financials"])
def get_user_investments(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieves all investment accounts for a specific user.
    """
    accounts = load_data("accounts.json")
    investment_accounts = [
        acc for acc in accounts if acc["user_id"] == user_id and acc["type"] == "investment"
    ]
    if not investment_accounts:
        raise HTTPException(status_code=404, detail="No investment accounts found for this user")
    return investment_accounts

@router.get("/users/{user_id}/networth", tags=["Financials"])
def get_user_net_worth(user_id: str) -> Dict[str, float]:
    """
    Calculates the net worth of a specific user.
    """
    accounts = load_data("accounts.json")
    user_accounts = [acc for acc in accounts if acc["user_id"] == user_id]
    if not user_accounts:
        raise HTTPException(status_code=404, detail="No accounts found for this user")

    net_worth = sum(acc["balance"] for acc in user_accounts)
    return {"net_worth": net_worth}

@router.get("/users/{user_id}/cashflow", tags=["Financials"])
def get_user_cash_flow(user_id: str) -> Dict[str, float]:
    """
    Calculates the cash flow for a specific user over the last 30 days.
    """
    transactions = load_data("transactions.json")
    accounts = load_data("accounts.json")
    user_account_ids = [
        acc["account_id"] for acc in accounts if acc["user_id"] == user_id
    ]

    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_transactions = [
        t
        for t in transactions
        if t["account_id"] in user_account_ids
        and datetime.fromisoformat(t["date"].replace("Z", "")) > thirty_days_ago
    ]

    cash_flow = sum(t["amount"] for t in recent_transactions)
    return {"cash_flow_last_30_days": cash_flow}

@router.get("/users/{user_id}/average_cashflow", tags=["Financials"])
def get_user_average_cash_flow(user_id: str) -> Dict[str, float]:
    """
    Calculates the average monthly cash flow for a specific user over the last 3 months.
    """
    transactions = load_data("transactions.json")
    accounts = load_data("accounts.json")
    user_account_ids = [
        acc["account_id"] for acc in accounts if acc["user_id"] == user_id
    ]

    ninety_days_ago = datetime.now() - timedelta(days=90)
    recent_transactions = [
        t
        for t in transactions
        if t["account_id"] in user_account_ids
        and datetime.fromisoformat(t["date"].replace("Z", "")) > ninety_days_ago
    ]

    total_cash_flow = sum(t["amount"] for t in recent_transactions)
    average_cash_flow = total_cash_flow / 3 if total_cash_flow else 0
    return {"average_monthly_cash_flow": average_cash_flow}
