# backend/api/endpoints/accounts.py

import json
from fastapi import APIRouter, status, HTTPException
from typing import List
from api.models import Account, User

router = APIRouter()
USERS_FILE = "db/users.json"
DATA_FILE = "db/accounts.json"

# Map account types to their corresponding code letters
ACCOUNT_TYPE_MAP = {
    "investment": "i",
    "savings": "s",
    "checking": "c",
    "credit card": "d",
    "pension": "p"
}

def read_users_data() -> List[User]:
    """Reads user data from the JSON file."""
    try:
        with open(USERS_FILE, "r") as f:
            users_data = json.load(f)
        return [User(**user) for user in users_data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_accounts_data() -> List[Account]:
    with open(DATA_FILE, "r") as f:
        accounts_data = json.load(f)
    return [Account(**acc) for acc in accounts_data]

def write_accounts_data(accounts: List[Account]):
    """Writes the list of accounts back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json_data = [acc.model_dump() for acc in accounts]
        json.dump(json_data, f, indent=4)


@router.get("/users/{user_id}/accounts", response_model=List[Account])
def get_user_accounts(user_id: str):
    """
    Get all accounts for a user.
    """
    normalized_user_id = user_id.replace("_", "-")
    accounts = read_accounts_data()
    user_accounts = [acc for acc in accounts if acc.user_id == normalized_user_id]
    return user_accounts

@router.post("/users/{user_id}/accounts", response_model=Account, status_code=status.HTTP_201_CREATED)
def create_account_for_user(user_id: str, account_in: Account):
    """
    Create a new account for a specific user.
    The account_id is generated automatically based on user initials,
    account type, and an incremental number (e.g., acc-mw-i-001).
    """
    normalized_user_id = user_id.replace("_", "-")
    
    # 1. Get user's initials
    users = read_users_data()
    user = next((u for u in users if u.user_id == normalized_user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID '{normalized_user_id}' not found")
    
    name_parts = user.name.split()
    initials = "".join(part[0] for part in name_parts).lower()

    # 2. Get account type code, defaulting to 'x' if not found
    account_type = account_in.type.lower()
    type_code = ACCOUNT_TYPE_MAP.get(account_type, 'x')

    # 3. Find the next incremental number for this user and account type
    accounts = read_accounts_data()
    id_prefix = f"acc-{initials}-{type_code}-"
    
    relevant_accounts = [acc for acc in accounts if acc.account_id.startswith(id_prefix)]
    
    max_num = 0
    for acc in relevant_accounts:
        try:
            num_part = int(acc.account_id.split('-')[-1])
            if num_part > max_num:
                max_num = num_part
        except (ValueError, IndexError):
            # Ignore malformed IDs
            continue
            
    new_num = max_num + 1
    new_formatted_num = f"{new_num:03d}"
    
    # 4. Construct the new Account object
    new_account_id = f"{id_prefix}{new_formatted_num}"
    
    new_account = account_in.model_copy(update={
        "user_id": normalized_user_id,
        "account_id": new_account_id
    })
    
    # 5. Save and return the new account
    accounts.append(new_account)
    write_accounts_data(accounts)
    
    return new_account