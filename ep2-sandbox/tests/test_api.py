# tests/test_api.py

import json
import os
from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch

# Adjust the path to import the app from the backend
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.main import app
from backend.api.endpoints import financials

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
        assert "category" in account
        assert "type" in account
        assert "sub_type" in account
        assert "description" in account

# --- Financials Endpoint Tests ---
def test_get_user_debts_success():
    """Test fetching debt accounts for a user."""
    user_id = "user-001"
    response = client.get(f"/api/users/{user_id}/debts")
    assert response.status_code == 200
    for account in response.json():
        assert account["user_id"] == user_id
        assert account["category"] == "liability"

def test_get_user_debts_not_found():
    """Test fetching debts for a user with no debt accounts."""
    # This user has no liability accounts
    response = client.get("/api/users/user-004/debts")
    assert response.status_code == 404

def test_get_user_investments_success():
    """Test fetching investment accounts for a user."""
    user_id = "user-002"
    response = client.get(f"/api/users/{user_id}/investments")
    assert response.status_code == 200
    for account in response.json():
        assert account["user_id"] == user_id
        assert account["category"] == "asset"
        assert account["type"] == "investment"

def test_get_user_investments_not_found():
    """Test fetching investments for a user with no investment accounts."""
    # This user has no investment accounts
    response = client.get("/api/users/user-004/investments")
    assert response.status_code == 404

def test_get_user_net_worth_success(db_data):
    """Test calculating net worth for a user."""
    user_id = "user-001"
    response = client.get(f"/api/users/{user_id}/networth")
    assert response.status_code == 200
    assert "net_worth" in response.json()
    
    user_accounts = [acc for acc in db_data["accounts"] if acc["user_id"] == user_id]
    expected_net_worth = sum(acc["balance"] for acc in user_accounts)
    assert response.json()["net_worth"] == expected_net_worth

def test_get_user_net_worth_normalization():
    """Test that user_id with underscore is normalized."""
    response_dash = client.get("/api/users/user-001/networth")
    response_underscore = client.get("/api/users/user_001/networth")
    assert response_dash.status_code == 200
    assert response_underscore.status_code == 200
    assert response_dash.json() == response_underscore.json()

def test_get_user_net_worth_no_accounts():
    """Test calculating net worth for a user with no accounts."""
    response = client.get("/api/users/user-999/networth")
    assert response.status_code == 404

def test_get_user_cash_flow_success(db_data):
    """Test calculating cash flow for a user with recent transactions."""
    user_id = "user-001"
    response = client.get(f"/api/users/{user_id}/cashflow")
    assert response.status_code == 200
    assert "cash_flow_last_30_days" in response.json()
    # This value will change based on the current date, so we check the type
    assert isinstance(response.json()["cash_flow_last_30_days"], float)

def test_get_user_cash_flow_no_recent_transactions():
    """Test cash flow for a user with no recent transactions."""
    # A user with no transactions in the last 30 days
    response = client.get("/api/users/user-004/cashflow")
    assert response.status_code == 200
    assert response.json()["cash_flow_last_30_days"] == 0

def test_get_user_average_cash_flow_success(db_data):
    """Test calculating average cash flow for a user."""
    user_id = "user-001"
    response = client.get(f"/api/users/{user_id}/average_cashflow")
    assert response.status_code == 200
    assert "average_monthly_cash_flow" in response.json()
    assert isinstance(response.json()["average_monthly_cash_flow"], float)

# --- Goals Endpoint Tests ---
def test_update_goal_success(db_data):
    """Test updating a financial goal and ensure data is restored."""
    goal_to_update = db_data["life_goals"][0].copy()
    goal_id = goal_to_update["goal_id"]
    
    updated_description = f"Updated Goal Description {goal_id}"
    goal_to_update["description"] = updated_description

    goals_file_path = get_data_path("life_goals.json")
    with open(goals_file_path, "r") as f:
        original_data = f.read()

    try:
        response = client.put(f"/api/goals/{goal_id}", json=goal_to_update)
        assert response.status_code == 200
        assert response.json()["description"] == updated_description
    finally:
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

# --- Data Integrity Tests ---
@patch('backend.api.endpoints.financials.load_data')
def test_get_debts_with_malformed_data(mock_load_data):
    """Test that the endpoint handles malformed account data gracefully."""
    malformed_account = {
        "account_id": "acc-malformed-001",
        "user_id": "user-001",
        # Missing 'category', 'type', etc.
        "balance": 100.00
    }
    mock_load_data.return_value = [malformed_account]
    
    with pytest.raises(KeyError):
        client.get("/api/users/user-001/debts")