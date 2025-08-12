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
  - [Partners](#partners)
  - [Schedule](#schedule)
  - [Meeting](#meeting)
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

#### Holding
```python
class Holding(BaseModel):
    symbol: str
    value: float
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

#### EligibilityCriteria
```python
class EligibilityCriteria(BaseModel):
    minimum_credit_score: Optional[int] = None
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
    goal_id: str = Field(default_factory=lambda: f"goal-{uuid4()}")
    user_id: str
    description: str
    target_amount: float
    target_date: str
    current_amount_saved: float
```

#### Schedule
```python
class Schedule(BaseModel):
    user_id: str
    schedule_id: str
    source_account_id: str
    destination_account_id: str
    description: str
    frequency: str
    start_date: str
    end_date: str
    amount: float
```

#### Advisor
```python
class Advisor(BaseModel):
    advisor_id: str = Field(default_factory=lambda: f"adv-{uuid4()}")
    name: str
    advisor_type: str
    availability: List[str] = []
```

#### Meeting
```python
class Meeting(BaseModel):
    meeting_id: str = Field(default_factory=lambda: f"meet-{uuid4()}")
    user_id: str
    advisor_name: str
    advisor_type: str
    meeting_time: datetime.datetime
    notes: Optional[str] = None
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

#### Additional Models
```python
class MarketData(BaseModel):
    timestamp: str
    indices: Dict[str, Dict[str, float]]
    news_headline: str

class Event(BaseModel):
    event_id: str
    type: str
    description: str
    amount: Optional[float] = None
    triggered: bool
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

#### POST `/api/users/{user_id}/accounts`
- **Description**: Create a new account for a user
- **Parameters**:
  - `user_id` (path): User identifier
  - `account_in` (body): Account object to create
- **Response**: Created `Account` object, 201 Created
- **Function**: `create_account_for_user(user_id: str, account_in: Account)`

**Features**:
- Automatically generates account IDs based on user initials and account type
- Supports various account types (checking, savings, investment, credit, etc.)
- Account ID format: `acc-{initials}-{type_code}-{number}` (e.g., `acc-mw-i-001`)

### Transactions

#### GET `/api/users/{user_id}/transactions`
- **Description**: Get all transactions for a user from the last N days
- **Parameters**:
  - `user_id` (path): User identifier
  - `history` (query, optional): Number of days to look back (default: 30)
- **Response**: List of `Transaction` objects
- **Error Codes**: 404 (User or user accounts not found)
- **Function**: `get_user_transactions(user_id: str, history: int = 30)`

**Features**:
- Retrieves transactions from all user accounts
- Filters transactions by user's account IDs and date range
- Default history is 30 days

### Goals

#### GET `/api/goals/{user_id}`
- **Description**: Get user's financial goals
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `LifeGoal` objects
- **Function**: `get_user_goals(user_id: str)`

#### POST `/api/goals`
- **Description**: Create a new financial goal
- **Parameters**:
  - `goal_payload` (body): `LifeGoal` object to create
- **Response**: Created `LifeGoal` object, 201 Created
- **Function**: `create_goal(goal_payload: LifeGoal)`

#### PUT `/api/goals/{goal_id}`
- **Description**: Update a financial goal
- **Parameters**:
  - `goal_id` (path): Goal identifier
  - `updated_goal` (body): Updated `LifeGoal` object
- **Response**: Updated `LifeGoal` object
- **Error Codes**: 404 (Goal not found)
- **Function**: `update_goal(goal_id: str, updated_goal: LifeGoal)`

#### DELETE `/api/goals/{goal_id}`
- **Description**: Cancel a financial goal
- **Parameters**:
  - `goal_id` (path): Goal identifier
- **Response**: 204 No Content
- **Error Codes**: 404 (Goal not found)
- **Function**: `cancel_goal(goal_id: str)`

**Features**:
- Full CRUD operations for financial goals
- Goal IDs are automatically generated with UUIDs
- Persists changes to JSON file storage

### Financials

#### GET `/api/users/{user_id}/debts`
- **Description**: Get all debt (liability) accounts for a user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Account` objects (liability accounts only)
- **Error Codes**: 404 (No debt accounts found)
- **Function**: `get_user_debts(user_id: str)`

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

### Partners

#### GET `/api/partners`
- **Description**: Retrieves a list of all available bank partners and their associated benefits
- **Parameters**: None
- **Response**: List of `BankPartner` objects
- **Function**: `get_bank_partners()`

#### GET `/api/partners/user/{user_id}`
- **Description**: Identifies and returns a list of partners a specific user can benefit from
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `BankPartner` objects
- **Error Codes**: 404 (User not found, User persona not found)
- **Function**: `get_user_benefits(user_id: str)`

**Features**:
- Filters partners based on user eligibility criteria
- Considers user credit score for partner recommendations
- Integrates with user personas for personalized benefits

### Schedule
Provides full CRUD (Create, Read, Update, Delete) operations for managing scheduled transactions, such as recurring payments or transfers.

#### POST `/api/users/{user_id}/schedules`
- **Description**: Create a new scheduled transaction for a user
- **Parameters**:
  - `user_id` (path): The user's identifier
  - `schedule_in` (body): A `Schedule` object (without `schedule_id` and `user_id`)
- **Response**: `Schedule` object, 201 Created
- **Function**: `create_schedule_for_user(user_id: str, schedule_in: Schedule)`

#### GET `/api/users/{user_id}/schedules`
- **Description**: Retrieve all scheduled transactions for a specific user
- **Parameters**:
  - `user_id` (path): The user's identifier
- **Response**: List of `Schedule` objects
- **Function**: `get_schedules_for_user(user_id: str)`

#### PUT `/api/schedules/{schedule_id}`
- **Description**: Update an existing scheduled transaction
- **Parameters**:
  - `schedule_id` (path): The identifier of the schedule to update
  - `schedule_update` (body): A `Schedule` object containing the fields to update
- **Response**: The updated `Schedule` object
- **Error Codes**: 404 (Schedule not found)
- **Function**: `update_schedule(schedule_id: str, schedule_update: Schedule)`

#### DELETE `/api/schedules/{schedule_id}`
- **Description**: Delete a scheduled transaction by its ID
- **Parameters**:
  - `schedule_id` (path): The identifier of the schedule to delete
- **Response**: 204 No Content
- **Error Codes**: 404 (Schedule not found)
- **Function**: `delete_schedule(schedule_id: str)`

**Features**:
- Schedule IDs are automatically generated with UUIDs
- Supports partial updates using `exclude_unset=True`
- Handles file I/O errors gracefully

### Meeting

#### GET `/api/advisors`
- **Description**: Get a list of all available financial advisors
- **Parameters**: None
- **Response**: List of `Advisor` objects
- **Function**: `list_advisors()`

#### GET `/api/advisors/{advisor_type}`
- **Description**: Get advisors by their specialization type
- **Parameters**:
  - `advisor_type` (path): Type of advisor (e.g., "financial_planner", "investment_advisor")
- **Response**: List of `Advisor` objects
- **Error Codes**: 404 (No advisors found for type)
- **Function**: `get_advisors_by_type(advisor_type: str)`

#### POST `/api/meetings`
- **Description**: Schedule a new meeting with an advisor
- **Parameters**:
  - `meeting_request` (body): `Meeting` object to create
- **Response**: Created `Meeting` object, 201 Created
- **Error Codes**: 409 (Time slot already booked)
- **Function**: `schedule_meeting(meeting_request: Meeting)`

#### GET `/api/meetings/{user_id}`
- **Description**: Get all scheduled meetings for a specific user
- **Parameters**:
  - `user_id` (path): User identifier
- **Response**: List of `Meeting` objects
- **Function**: `get_user_meetings(user_id: str)`

#### DELETE `/api/meetings/{meeting_id}`
- **Description**: Cancel a scheduled meeting
- **Parameters**:
  - `meeting_id` (path): Meeting identifier
- **Response**: 204 No Content
- **Error Codes**: 404 (Meeting not found)
- **Function**: `cancel_meeting(meeting_id: str)`

**Features**:
- Prevents double-booking of advisor time slots
- Meeting IDs are automatically generated with UUIDs
- Handles datetime serialization for JSON storage

## Error Handling

The API implements comprehensive error handling with standard HTTP status codes:

- **404 Not Found**: When requested resources (users, accounts, goals, schedules, meetings) don't exist
- **409 Conflict**: When trying to book an already booked time slot
- **500 Internal Server Error**: For file system errors or data processing issues

All endpoints include proper error responses with descriptive messages.

## Data Sources

The API uses JSON files stored in the `db/` directory as its data source:

- `users.json`: User profiles and personal information
- `accounts.json`: Account information and balances
- `transactions.json`: Transaction history
- `bank_partners.json`: Bank partner information and benefits
- `life_goals.json`: Financial goals and targets
- `schedule.json`: Scheduled transactions
- `meetings.json`: Financial advisor meetings
- `advisors.json`: Available financial advisors
- `user_personas.json`: User persona information for partner eligibility

### Data Loading Functions

Each endpoint module includes utility functions for data loading:

- `read_users_data()`: Loads user data from JSON
- `read_accounts_data()`: Loads account data from JSON
- `read_transactions_data()`: Loads transaction data from JSON
- `read_goals_data()`: Loads goal data from JSON
- `read_schedules_data()`: Loads schedule data from JSON
- `get_advisors()`: Loads advisor data from JSON
- `get_meetings()`: Loads meeting data from JSON
- `load_data(file_name: str)`: Generic data loading function

## API Features

### User ID Normalization
All endpoints normalize user IDs by replacing underscores with hyphens to ensure consistent data access.

### CORS Support
The API includes CORS middleware configured to allow all origins, methods, and headers for frontend integration.

### Comprehensive Financial Analytics
- Net worth calculation from all user accounts
- Cash flow analysis (30-day and 3-month averages)
- Debt and investment account filtering
- Transaction categorization and tracking with date-based filtering

### Data Persistence
- Read operations from JSON files
- Write operations for goals, accounts, schedules, and meetings
- Structured data models with Pydantic validation
- Automatic ID generation for new resources

### Advanced Features
- Account ID generation based on user initials and account type
- Double-booking prevention for advisor meetings
- Partner eligibility filtering based on user credit scores
- Transaction history with configurable time periods

This API provides a complete foundation for personal financial management applications with robust data handling, comprehensive financial analytics capabilities, and full CRUD operations for all major entities. 