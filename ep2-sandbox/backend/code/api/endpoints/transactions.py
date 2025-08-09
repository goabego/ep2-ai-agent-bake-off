# backend/api/endpoints/transactions.py

import json
from fastapi import APIRouter, HTTPException
from typing import List
from api.models import Transaction, Account

from datetime import datetime, timedelta, timezone

router = APIRouter()

TRANSACTIONS_FILE = "db/transactions.json"
ACCOUNTS_FILE = "db/accounts.json"

def read_transactions_data() -> List[Transaction]:
    with open(TRANSACTIONS_FILE, "r") as f:
        transactions_data = json.load(f)
    return [Transaction(**tx) for tx in transactions_data]

def read_accounts_data() -> List[Account]:
    with open(ACCOUNTS_FILE, "r") as f:
        accounts_data = json.load(f)
    return [Account(**acc) for acc in accounts_data]

@router.get("/users/{user_id}/transactions", response_model=List[Transaction])
def get_user_transactions(user_id: str, history: int = 30):
    """
    Get all transactions for a user from the last N days.
    """
    # Calculate the cutoff date for the history period
    now = datetime.now(timezone.utc)
    cutoff_date = now - timedelta(days=history)

    normalized_user_id = user_id.replace("_", "-")
    accounts = read_accounts_data()
    user_account_ids = [acc.account_id for acc in accounts if acc.user_id == normalized_user_id]

    if not user_account_ids:
        raise HTTPException(status_code=404, detail="User or user accounts not found")

    transactions = read_transactions_data()
    
    # Filter transactions by account and date
    user_transactions = [
        tx for tx in transactions 
        if tx.account_id in user_account_ids and 
           datetime.fromisoformat(tx.date.replace('Z', '+00:00')) >= cutoff_date
    ]
    
    return user_transactions
