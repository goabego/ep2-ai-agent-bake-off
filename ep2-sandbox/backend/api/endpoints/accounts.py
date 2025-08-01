# backend/api/endpoints/accounts.py

import json
from fastapi import APIRouter
from typing import List
from backend.api.models import Account

router = APIRouter()

DATA_FILE = "db/accounts.json"

def read_accounts_data() -> List[Account]:
    with open(DATA_FILE, "r") as f:
        accounts_data = json.load(f)
    return [Account(**acc) for acc in accounts_data]

@router.get("/users/{user_id}/accounts", response_model=List[Account])
def get_user_accounts(user_id: str):
    """
    Get all accounts for a user.
    """
    normalized_user_id = user_id.replace("_", "-")
    accounts = read_accounts_data()
    user_accounts = [acc for acc in accounts if acc.user_id == normalized_user_id]
    return user_accounts
