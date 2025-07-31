# tests/test_api.py

import json
import os
from fastapi.testclient import TestClient
import pytest

# Adjust the path to import the app from the backend
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.main import app

client = TestClient(app)

# Helper to get the absolute path for data files
def get_data_path(filename):
    return os.path.join(os.path.dirname(__file__), '..', 'db', filename)

# --- Test Data Loading ---
@pytest.fixture(scope="module")
def db_data():
    """Fixture to load all mock DB data once."""
    data = {}
    for filename in ["users.json", "accounts.json", "transactions.json", "life_goals.json"]:
        key = filename.split('.')[0]
        with open(get_data_path(filename), "r") as f:
            data[key] = json.load(f)
    return data

# --- Root Endpoint Tests ---
def test_read_root():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Welcome to the AI Financial Steward API"}

# --- User Endpoint Tests ---
def test_get_user_success(db_data):
    """Test fetching a user that exists."""
    first_user_id = db_data["users"][0]["user_id"]
    response = client.get(f"/api/users/{first_user_id}")
    assert response.status_code == 200
    assert response.json()["user_id"] == first_user_id

def test_get_user_not_found():
    """Test fetching a user that does not exist."""
    response = client.get("/api/users/non-existent-user")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

# --- Accounts Endpoint Tests ---
def test_get_user_accounts(db_data):
    """Test fetching accounts for a user."""
    user_id_with_accounts = db_data["accounts"][0]["user_id"]
    response = client.get(f"/api/users/{user_id_with_accounts}/accounts")
    assert response.status_code == 200
    # Ensure all returned accounts belong to the user
    for account in response.json():
        assert account["user_id"] == user_id_with_accounts

# --- Transactions Endpoint Tests ---
def test_get_user_transactions(db_data):
    """Test fetching transactions for a user."""
    # Find a user with accounts and transactions
    account_with_tx = db_data["transactions"][0]["account_id"]
    user_id = next(acc["user_id"] for acc in db_data["accounts"] if acc["account_id"] == account_with_tx)
    
    response = client.get(f"/api/users/{user_id}/transactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# --- Goals Endpoint Tests ---
def test_get_user_goals(db_data):
    """Test fetching financial goals for a user."""
    user_id_with_goals = db_data["life_goals"][0]["user_id"]
    response = client.get(f"/api/goals/{user_id_with_goals}")
    assert response.status_code == 200
    for goal in response.json():
        assert goal["user_id"] == user_id_with_goals

def test_update_goal(db_data):
    """Test updating a financial goal and ensure data is restored."""
    goal_to_update = db_data["life_goals"][0].copy()
    goal_id = goal_to_update["goal_id"]
    
    updated_description = f"Updated Goal Description {goal_id}"
    goal_to_update["description"] = updated_description

    # Read original file content to restore it later
    goals_file_path = get_data_path("life_goals.json")
    with open(goals_file_path, "r") as f:
        original_data = f.read()

    try:
        response = client.put(f"/api/goals/{goal_id}", json=goal_to_update)
        assert response.status_code == 200
        assert response.json()["description"] == updated_description

        # Verify the change by reading again
        response = client.get(f"/api/goals/{goal_to_update['user_id']}")
        assert response.status_code == 200
        updated_goal_in_list = next(g for g in response.json() if g["goal_id"] == goal_id)
        assert updated_goal_in_list["description"] == updated_description

    finally:
        # Restore the original file content
        with open(goals_file_path, "w") as f:
            f.write(original_data)

def test_update_goal_not_found():
    """Test updating a goal that does not exist."""
    non_existent_goal = {
        "goal_id": "non-existent-goal",
        "user_id": "user-001",
        "description": "Test",
        "target_amount": 1000,
        "target_date": "2030-01-01",
        "current_amount_saved": 100
    }
    response = client.put("/api/goals/non-existent-goal", json=non_existent_goal)
    assert response.status_code == 404
    assert response.json() == {"detail": "Goal not found"}
