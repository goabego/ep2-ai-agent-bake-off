# backend/api/endpoints/users.py

import json
from fastapi import APIRouter, HTTPException
from typing import List
from backend.api.models import User

router = APIRouter()

DATA_FILE = "db/users.json"

def read_users_data() -> List[User]:
    with open(DATA_FILE, "r") as f:
        users_data = json.load(f)
    return [User(**user) for user in users_data]

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    """
    Get user profile.
    """
    users = read_users_data()
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
