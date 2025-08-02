# AI Financial Steward API Overview

## Table of Contents
- [Overview](#overview)
- [Data Models](#data-models)
- [API Endpoints](#api-endpoints)
  - [Users](#users)
  - [Accounts](#accounts)
  - [Transactions](#transactions)
  - [Goals](#goals)
  - [Financials](#financials)
- [Error Handling](#error-handling)
- [Data Sources](#data-sources)

## Overview

The AI Financial Steward API is a FastAPI-based REST API that provides comprehensive financial data management and analysis capabilities. The API is designed to support personal financial management with features for user profiles, account management, transaction tracking, goal setting, and financial analytics.

**Base URL**: `/api`
**API Version**: 0.1.0
**Title**: AI Financial Steward API

## Data Models

### Core Models

#### User
```python
class User(BaseModel):
    user_id: str
    name: str
    age: int
    risk_tolerance: str
    profile_picture: Optional[str] = None
    address: Optional[str] = None
    credit_score: Optional[int] = None
    net_worth: Optional[float] = None
    member_since: Optional[int] = None
    financial_blurb: str
    goals: List[str]
```

#### Account
```python
class Account(BaseModel):
    account_id: str
    user_id: str
    category: str  # "asset" or "liability"
    type: str      # "checking", "savings", "investment", "credit", etc.
    sub_type: str
    description: str
    balance: float
    institution: Optional[str] = None
    holdings: Optional[List[Holding]] = None
    interest_rate: Optional[float] = None
```

#### Transaction
```python
class Transaction(BaseModel):
    transaction_id: str
    account_id: str
    merchant_id: str
    date: str
    description: str
    amount: float
    category: str
```

#### BankPartner
```python
class BankPartner(BaseModel):
    partner_id: str
    merchant_id: str
    name: str
    category: str
    benefit_type: str
    benefit_value: float
    eligibility_criteria: Optional[EligibilityCriteria] = None
```

#### LifeGoal
```python
class LifeGoal(BaseModel):
    goal_id: str
    user_id: str
    description: str
    target_amount: float
    target_date: str
    current_amount_saved: float
```

#### Financial Analytics Models
```python
class NetWorth(BaseModel):
    net_worth: float

class CashFlow(BaseModel):
    cash_flow_last_30_days: float

class AverageCashFlow(BaseModel):
    average_monthly_cash_flow: float
```

## API Endpoints

### Users

#### GET `/api/users/{user_id}`
- **Description**: Get user profile with calculated net worth
- **Parameters**: 
  - `user_id` (path): User identifier
- **Response**: `User` object with calculated net worth
- **Error Codes**: 404 (User not found)
- **Function**: `get_user(user_id: str)`

**Features**:
- Normalizes user ID (replaces underscores with hyphens)
- Calculates net worth from user's accounts
- Returns complete user profile

### Accounts

#### GET `/api/users/{user_id}/accounts`
- **Description**: Get all accounts for a user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Account` objects
- **Function**: `get_user_accounts(user_id: str)`

**Features**:
- Returns all accounts associated with the user
- Supports various account types (checking, savings, investment, credit, etc.)

### Transactions

#### GET `/api/users/{user_id}/transactions`
- **Description**: Get all transactions for a user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Transaction` objects
- **Error Codes**: 404 (User or user accounts not found)
- **Function**: `get_user_transactions(user_id: str)`

**Features**:
- Retrieves transactions from all user accounts
- Filters transactions by user's account IDs

### Goals

#### GET `/api/goals/{user_id}`
- **Description**: Get user's financial goals
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `LifeGoal` objects
- **Function**: `get_user_goals(user_id: str)`

#### PUT `/api/goals/{goal_id}`
- **Description**: Update a financial goal
- **Parameters**:
  - `goal_id` (path): Goal identifier
  - `updated_goal` (body): Updated `LifeGoal` object
- **Response**: Updated `LifeGoal` object
- **Error Codes**: 404 (Goal not found)
- **Function**: `update_goal(goal_id: str, updated_goal: LifeGoal)`

**Features**:
- Supports goal creation and updates
- Persists changes to JSON file storage

### Financials

#### GET `/api/users/{user_id}/debts`
- **Description**: Get all debt (liability) accounts for a user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Account` objects (liability accounts only)
- **Error Codes**: 404 (No debt accounts found)
- **Function**: `get_user_debts(user_id: str)`

### Partners

#### GET `/api/partners`
- **Description**: Retrieves a list of all available bank partners and their associated benefits.
- **Parameters**: None
- **Response**: List of `BankPartner` objects
- **Function**: `get_bank_partners()`

#### GET `/api/partners/user/{user_id}`
- **Description**: Identifies and returns a list of partners a specific user can benefit from.
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `BankPartner` objects
- **Error Codes**: 404 (User not found)
- **Function**: `get_user_benefits(user_id: str)`


#### GET `/api/users/{user_id}/investments`
- **Description**: Get all investment accounts for a user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Account` objects (investment accounts only)
- **Error Codes**: 404 (No investment accounts found)
- **Function**: `get_user_investments(user_id: str)`

#### GET `/api/users/{user_id}/networth`
- **Description**: Calculate user's net worth
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: `NetWorth` object
- **Error Codes**: 404 (No accounts found)
- **Function**: `get_user_net_worth(user_id: str)`

#### GET `/api/users/{user_id}/cashflow`
- **Description**: Calculate cash flow for the last 30 days
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: `CashFlow` object
- **Function**: `get_user_cash_flow(user_id: str)`

#### GET `/api/users/{user_id}/average_cashflow`
- **Description**: Calculate average monthly cash flow over the last 3 months
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: `AverageCashFlow` object
- **Function**: `get_user_average_cash_flow(user_id: str)`

## Error Handling

The API implements comprehensive error handling with standard HTTP status codes:

- **404 Not Found**: When requested resources (users, accounts, goals) don't exist
- **500 Internal Server Error**: For file system errors or data processing issues

All endpoints include proper error responses with descriptive messages.

## Data Sources

The API uses JSON files stored in the `db/` directory as its data source:

- `users.json`: User profiles and personal information
- `accounts.json`: Account information and balances
- `transactions.json`: Transaction history
- `bank_partners.json`: Bank partner information and benefits
- `life_goals.json`: Financial goals and targets

### Data Loading Functions

Each endpoint module includes utility functions for data loading:

- `read_users_data()`: Loads user data from JSON
- `read_accounts_data()`: Loads account data from JSON
- `read_transactions_data()`: Loads transaction data from JSON
- `read_goals_data()`: Loads goal data from JSON
- `load_data(file_name: str)`: Generic data loading function

## API Features

### User ID Normalization
All endpoints normalize user IDs by replacing underscores with hyphens to ensure consistent data access.

### CORS Support
The API includes CORS middleware configured to allow all origins, methods, and headers for frontend integration.

### Comprehensive Financial Analytics
- Net worth calculation
- Cash flow analysis (30-day and 3-month averages)
- Debt and investment account filtering
- Transaction categorization and tracking

### Data Persistence
- Read operations from JSON files
- Write operations for goal updates
- Structured data models with Pydantic validation

This API provides a complete foundation for personal financial management applications with robust data handling and comprehensive financial analytics capabilities. 