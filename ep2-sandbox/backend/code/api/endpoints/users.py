# backend/api/endpoints/users.py

import json
from fastapi import APIRouter, HTTPException
from typing import List
from api.models import User, Account

router = APIRouter()

USERS_DATA_FILE = "db/users.json"
ACCOUNTS_DATA_FILE = "db/accounts.json"

def read_users_data() -> List[User]:
    with open(USERS_DATA_FILE, "r") as f:
        users_data = json.load(f)
    return [User(**user) for user in users_data]

def read_accounts_data() -> List[Account]:
    with open(ACCOUNTS_DATA_FILE, "r") as f:
        accounts_data = json.load(f)
    return [Account(**acc) for acc in accounts_data]

@router.get("/users", response_model=List[User])
def get_users():
    """
    Get all users.
    """
    return read_users_data()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    """
    Get user profile.
    """
    normalized_user_id = user_id.replace("_", "-")
    
    users = read_users_data()
    user = next((u for u in users if u.user_id == normalized_user_id), None)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    accounts = read_accounts_data()
    user_accounts = [acc for acc in accounts if acc.user_id == normalized_user_id]
    
    net_worth = sum(acc.balance for acc in user_accounts)
    user.net_worth = net_worth
    
    return user
