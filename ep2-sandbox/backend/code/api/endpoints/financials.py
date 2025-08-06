import json
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from datetime import datetime, timedelta
from api.models import Account, NetWorth, CashFlow, AverageCashFlow

router = APIRouter()

# Financials API Endpoints Summary
#
# Table of Contents:
# - load_data: Loads data from a JSON file in the db directory.
# - get_user_debts: Retrieves all debt (liability) accounts for a user.
#     API Endpoint: GET /users/{user_id}/debts
# - get_user_investments: Retrieves all investment accounts for a user.
#     API Endpoint: GET /users/{user_id}/investments
# - get_user_net_worth: Calculates the net worth of a user.
#     API Endpoint: GET /users/{user_id}/networth
# - get_user_cash_flow: Calculates the cash flow for a user over the last 30 days.
#     API Endpoint: GET /users/{user_id}/cashflow
# - get_user_average_cash_flow: Calculates the average monthly cash flow for a user over the last 3 months.
#     API Endpoint: GET /users/{user_id}/average_cashflow
# (See below for endpoint implementations.)


def load_data(file_name: str) -> List[Dict[str, Any]]:
    try:
        with open(f"db/{file_name}", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"{file_name} not found")

@router.get("/users/{user_id}/debts", response_model=List[Account], tags=["Financials"])
def get_user_debts(user_id: str) -> List[Account]:
    """
    Retrieves all debt accounts for a specific user.
    """
    normalized_user_id = user_id.replace("_", "-")
    accounts = load_data("accounts.json")
    debt_accounts = [
        acc for acc in accounts if acc["user_id"] == normalized_user_id and acc["category"] == "liability"
    ]
    if not debt_accounts:
        raise HTTPException(status_code=404, detail="No debt accounts found for this user")
    return debt_accounts

@router.get("/users/{user_id}/investments", response_model=List[Account], tags=["Financials"])
def get_user_investments(user_id: str) -> List[Account]:
    """
    Retrieves all investment accounts for a specific user.
    """
    normalized_user_id = user_id.replace("_", "-")
    accounts = load_data("accounts.json")
    investment_accounts = [
        acc for acc in accounts if acc["user_id"] == normalized_user_id and acc["category"] == "asset" and acc["type"] == "investment"
    ]
    if not investment_accounts:
        raise HTTPException(status_code=404, detail="No investment accounts found for this user")
    return investment_accounts

@router.get("/users/{user_id}/networth", response_model=NetWorth, tags=["Financials"])
def get_user_net_worth(user_id: str) -> NetWorth:
    """
    Calculates the net worth of a specific user.
    """
    normalized_user_id = user_id.replace("_", "-")
    accounts = load_data("accounts.json")
    user_accounts = [acc for acc in accounts if acc["user_id"] == normalized_user_id]
    if not user_accounts:
        raise HTTPException(status_code=404, detail="No accounts found for this user")

    net_worth = sum(acc["balance"] for acc in user_accounts)
    return NetWorth(net_worth=net_worth)

@router.get("/users/{user_id}/cashflow", response_model=CashFlow, tags=["Financials"])
def get_user_cash_flow(user_id: str) -> CashFlow:
    """
    Calculates the cash flow for a specific user over the last 30 days.
    """
    normalized_user_id = user_id.replace("_", "-")
    transactions = load_data("transactions.json")
    accounts = load_data("accounts.json")
    user_account_ids = [
        acc["account_id"] for acc in accounts if acc["user_id"] == normalized_user_id
    ]

    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_transactions = [
        t
        for t in transactions
        if t["account_id"] in user_account_ids
        and datetime.fromisoformat(t["date"].replace("Z", "")) > thirty_days_ago
    ]

    cash_flow = sum(t["amount"] for t in recent_transactions)
    return CashFlow(cash_flow_last_30_days=cash_flow)

@router.get("/users/{user_id}/average_cashflow", response_model=AverageCashFlow, tags=["Financials"])
def get_user_average_cash_flow(user_id: str) -> AverageCashFlow:
    """
    Calculates the average monthly cash flow for a specific user over the last 3 months.
    """
    normalized_user_id = user_id.replace("_", "-")
    transactions = load_data("transactions.json")
    accounts = load_data("accounts.json")
    user_account_ids = [
        acc["account_id"] for acc in accounts if acc["user_id"] == normalized_user_id
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
    return AverageCashFlow(average_monthly_cash_flow=average_cash_flow)
