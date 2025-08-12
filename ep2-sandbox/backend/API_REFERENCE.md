# Cymbal Bank API Reference

Complete API reference with request/response examples, error codes, and data schemas.

## 🔗 Base Information

- **Base URL**: `http://localhost:8080`
- **API Prefix**: `/api`
- **Content Type**: `application/json`
- **Authentication**: Google Cloud ID tokens (for A2A proxy endpoints)

## 📋 Endpoint Index

### 🔐 Authentication
- [Get Auth Token](#get-auth-token)

### 👥 User Management
- [Get User Profile](#get-user-profile)
- [Get User Accounts](#get-user-accounts)
- [Get User Transactions](#get-user-transactions)

### 🏦 Financial Data
- [Get User Debts](#get-user-debts)
- [Get User Investments](#get-user-investments)
- [Get User Net Worth](#get-user-net-worth)
- [Get User Cash Flow](#get-user-cash-flow)
- [Get User Average Cash Flow](#get-user-average-cash-flow)

### 🎯 Goals & Planning
- [Get User Goals](#get-user-goals)
- [Update Goal](#update-goal)

### 🤝 Partners & Benefits
- [Get Bank Partners](#get-bank-partners)
- [Get User Benefits](#get-user-benefits)

### 📅 Scheduling
- [Create Schedule](#create-schedule)
- [Get User Schedules](#get-user-schedules)
- [Update Schedule](#update-schedule)
- [Delete Schedule](#delete-schedule)

### 📋 Meetings
- [Get User Meetings](#get-user-meetings)
- [Create Meeting](#create-meeting)
- [Update Meeting](#update-meeting)
- [Delete Meeting](#delete-meeting)

### 🔄 A2A Proxy
- [Proxy A2A Request](#proxy-a2a-request)

---

## 🔐 Authentication

### Get Auth Token
**GET** `/token`

Get Google Cloud ID token for A2A service authentication.

**Response:**
```json
{
  "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "status": "success"
}
```

**Error Response:**
```json
{
  "detail": "Failed to fetch token: 500"
}
```

---

## 👥 User Management

### Get User Profile
**GET** `/api/users/{user_id}`

Retrieve complete user profile with calculated net worth.

**Parameters:**
- `user_id` (path, required): User identifier (e.g., `user01_marcus_w`)

**Response:**
```json
{
  "user_id": "user01_marcus_w",
  "name": "Marcus W.",
  "age": 35,
  "risk_tolerance": "moderate",
  "profile_picture": "user01_marcus_w.jpg",
  "address": "123 Main St, Anytown, USA",
  "credit_score": 750,
  "net_worth": 125000.0,
  "member_since": 2020,
  "financial_blurb": "Tech professional focused on long-term wealth building",
  "goals": ["retirement", "home_purchase", "emergency_fund"]
}
```

**Error Response:**
```json
{
  "detail": "User not found"
}
```

### Get User Accounts
**GET** `/api/users/{user_id}/accounts`

Get all financial accounts for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "account_id": "acc_001",
    "user_id": "user01_marcus_w",
    "category": "asset",
    "type": "checking",
    "sub_type": "primary",
    "description": "Primary Checking Account",
    "balance": 5000.0,
    "institution": "Cymbal Bank",
    "holdings": null,
    "interest_rate": null
  },
  {
    "account_id": "acc_002",
    "user_id": "user01_marcus_w",
    "category": "asset",
    "type": "savings",
    "sub_type": "high_yield",
    "description": "High Yield Savings",
    "balance": 25000.0,
    "institution": "Cymbal Bank",
    "holdings": null,
    "interest_rate": 4.25
  }
]
```

### Get User Transactions
**GET** `/api/users/{user_id}/transactions`

Get transaction history for all user accounts.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "transaction_id": "txn_001",
    "account_id": "acc_001",
    "merchant_id": "merch_001",
    "date": "2024-01-15",
    "description": "Grocery Store Purchase",
    "amount": -85.50,
    "category": "food"
  },
  {
    "transaction_id": "txn_002",
    "account_id": "acc_001",
    "merchant_id": "merch_002",
    "date": "2024-01-14",
    "description": "Salary Deposit",
    "amount": 5000.0,
    "category": "income"
  }
]
```

---

## 🏦 Financial Data

### Get User Debts
**GET** `/api/users/{user_id}/debts`

Get all liability (debt) accounts for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "account_id": "acc_003",
    "user_id": "user01_marcus_w",
    "category": "liability",
    "type": "credit",
    "sub_type": "rewards",
    "description": "Credit Card",
    "balance": -2500.0,
    "institution": "Cymbal Bank",
    "holdings": null,
    "interest_rate": 18.99
  }
]
```

### Get User Investments
**GET** `/api/users/{user_id}/investments`

Get all investment accounts for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "account_id": "acc_004",
    "user_id": "user01_marcus_w",
    "category": "asset",
    "type": "investment",
    "sub_type": "401k",
    "description": "401(k) Retirement Plan",
    "balance": 95000.0,
    "institution": "Cymbal Bank",
    "holdings": [
      {
        "symbol": "SPY",
        "value": 45000.0
      },
      {
        "symbol": "VTI",
        "value": 50000.0
      }
    ],
    "interest_rate": null
  }
]
```

### Get User Net Worth
**GET** `/api/users/{user_id}/networth`

Calculate user's current net worth from all accounts.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
{
  "net_worth": 125000.0
}
```

### Get User Cash Flow
**GET** `/api/users/{user_id}/cashflow`

Calculate cash flow for the last 30 days.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
{
  "cash_flow_last_30_days": 2500.0
}
```

### Get User Average Cash Flow
**GET** `/api/users/{user_id}/average_cashflow`

Calculate average monthly cash flow over the last 3 months.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
{
  "average_monthly_cash_flow": 3200.0
}
```

---

## 🎯 Goals & Planning

### Get User Goals
**GET** `/api/goals/{user_id}`

Get all financial goals for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "goal_id": "goal_001",
    "user_id": "user01_marcus_w",
    "description": "Emergency Fund",
    "target_amount": 15000.0,
    "target_date": "2024-06-30",
    "current_amount_saved": 10000.0
  },
  {
    "goal_id": "goal_002",
    "user_id": "user01_marcus_w",
    "description": "Home Down Payment",
    "target_amount": 50000.0,
    "target_date": "2025-12-31",
    "current_amount_saved": 25000.0
  }
]
```

### Update Goal
**PUT** `/api/goals/{goal_id}`

Update an existing financial goal.

**Parameters:**
- `goal_id` (path, required): Goal identifier

**Request Body:**
```json
{
  "goal_id": "goal_001",
  "user_id": "user01_marcus_w",
  "description": "Emergency Fund",
  "target_amount": 20000.0,
  "target_date": "2024-08-31",
  "current_amount_saved": 15000.0
}
```

**Response:**
```json
{
  "goal_id": "goal_001",
  "user_id": "user01_marcus_w",
  "description": "Emergency Fund",
  "target_amount": 20000.0,
  "target_date": "2024-08-31",
  "current_amount_saved": 15000.0
}
```

---

## 🤝 Partners & Benefits

### Get Bank Partners
**GET** `/api/partners`

Get all available bank partners and their benefits.

**Response:**
```json
[
  {
    "partner_id": "partner_001",
    "merchant_id": "merch_001",
    "name": "Local Grocery Store",
    "category": "food",
    "benefit_type": "cashback",
    "benefit_value": 2.0,
    "eligibility_criteria": {
      "minimum_credit_score": 700
    }
  }
]
```

### Get User Benefits
**GET** `/api/partners/user/{user_id}`

Get partner benefits available to a specific user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "partner_id": "partner_001",
    "merchant_id": "merch_001",
    "name": "Local Grocery Store",
    "category": "food",
    "benefit_type": "cashback",
    "benefit_value": 2.0,
    "eligibility_criteria": {
      "minimum_credit_score": 700
    }
  }
]
```

---

## 📅 Scheduling

### Create Schedule
**POST** `/api/users/{user_id}/schedules`

Create a new scheduled transaction.

**Parameters:**
- `user_id` (path, required): User identifier

**Request Body:**
```json
{
  "source_account_id": "acc_001",
  "destination_account_id": "acc_002",
  "description": "Monthly Savings Transfer",
  "frequency": "monthly",
  "start_date": "2024-02-01",
  "end_date": "2024-12-31",
  "amount": 1000.0
}
```

**Response:**
```json
{
  "user_id": "user01_marcus_w",
  "schedule_id": "sched_001",
  "source_account_id": "acc_001",
  "destination_account_id": "acc_002",
  "description": "Monthly Savings Transfer",
  "frequency": "monthly",
  "start_date": "2024-02-01",
  "end_date": "2024-12-31",
  "amount": 1000.0
}
```

### Get User Schedules
**GET** `/api/users/{user_id}/schedules`

Get all scheduled transactions for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "user_id": "user01_marcus_w",
    "schedule_id": "sched_001",
    "source_account_id": "acc_001",
    "destination_account_id": "acc_002",
    "description": "Monthly Savings Transfer",
    "frequency": "monthly",
    "start_date": "2024-02-01",
    "end_date": "2024-12-31",
    "amount": 1000.0
  }
]
```

### Update Schedule
**PUT** `/api/schedules/{schedule_id}`

Update an existing scheduled transaction.

**Parameters:**
- `schedule_id` (path, required): Schedule identifier

**Request Body:**
```json
{
  "user_id": "user01_marcus_w",
  "schedule_id": "sched_001",
  "source_account_id": "acc_001",
  "destination_account_id": "acc_002",
  "description": "Monthly Savings Transfer",
  "frequency": "monthly",
  "start_date": "2024-02-01",
  "end_date": "2024-12-31",
  "amount": 1500.0
}
```

**Response:**
```json
{
  "user_id": "user01_marcus_w",
  "schedule_id": "sched_001",
  "source_account_id": "acc_001",
  "destination_account_id": "acc_002",
  "description": "Monthly Savings Transfer",
  "frequency": "monthly",
  "start_date": "2024-02-01",
  "end_date": "2024-12-31",
  "amount": 1500.0
}
```

### Delete Schedule
**DELETE** `/api/schedules/{schedule_id}`

Delete a scheduled transaction.

**Parameters:**
- `schedule_id` (path, required): Schedule identifier

**Response:**
- **Status**: 204 No Content

---

## 📋 Meetings

### Get User Meetings
**GET** `/api/users/{user_id}/meetings`

Get all meetings for a user.

**Parameters:**
- `user_id` (path, required): User identifier

**Response:**
```json
[
  {
    "meeting_id": "meet_001",
    "user_id": "user01_marcus_w",
    "advisor_name": "Sarah Johnson",
    "advisor_type": "financial_planner",
    "meeting_time": "2024-02-15T14:00:00",
    "notes": "Annual financial review and goal setting"
  }
]
```

### Create Meeting
**POST** `/api/users/{user_id}/meetings`

Create a new meeting.

**Parameters:**
- `user_id` (path, required): User identifier

**Request Body:**
```json
{
  "advisor_name": "Sarah Johnson",
  "advisor_type": "financial_planner",
  "meeting_time": "2024-02-20T15:00:00",
  "notes": "Investment portfolio review"
}
```

**Response:**
```json
{
  "meeting_id": "meet_002",
  "user_id": "user01_marcus_w",
  "advisor_name": "Sarah Johnson",
  "advisor_type": "financial_planner",
  "meeting_time": "2024-02-20T15:00:00",
  "notes": "Investment portfolio review"
}
```

---

## 🔄 A2A Proxy

### Proxy A2A Request
**POST** `/proxy/a2a`

Proxy requests to the A2A service with proper authentication.

**Request Body:**
```json
{
  "message": "What is my current net worth?",
  "user_id": "user01_marcus_w"
}
```

**Response:**
```json
{
  "response": "Based on your accounts, your current net worth is $125,000. This includes your checking account ($5,000), savings ($25,000), 401(k) ($95,000), minus your credit card balance ($2,500).",
  "status": "success"
}
```

---

## 🚨 Error Handling

### Standard Error Response Format
```json
{
  "detail": "Error message description"
}
```

### HTTP Status Codes

| Code | Description | Common Use Cases |
|------|-------------|------------------|
| 200 | OK | Successful GET, PUT, POST requests |
| 201 | Created | Successful resource creation |
| 204 | No Content | Successful DELETE requests |
| 400 | Bad Request | Invalid request parameters |
| 404 | Not Found | Resource doesn't exist |
| 500 | Internal Server Error | Server-side processing errors |

### Common Error Messages

- **User not found**: `{"detail": "User not found"}`
- **No accounts found**: `{"detail": "No accounts found for user"}`
- **Goal not found**: `{"detail": "Goal not found"}`
- **Schedule not found**: `{"detail": "Schedule not found"}`
- **Failed to fetch token**: `{"detail": "Failed to fetch token: 500"}`

---

## 🔧 Development Notes

### Data Normalization
- User IDs are automatically normalized (underscores replaced with hyphens)
- All endpoints handle this normalization transparently

### CORS Support
- All endpoints support CORS for frontend integration
- Configured to allow all origins, methods, and headers

### Rate Limiting
- Currently no rate limiting implemented
- Consider adding for production use

### Logging
- Basic error logging implemented
- Consider adding structured logging for production

---

## 📚 Additional Resources

- [API Overview](code/api/API_OVERVIEW.md) - Detailed endpoint documentation
- [Data Models](code/api/models.py) - Pydantic model definitions
- [Main Application](code/main.py) - FastAPI app configuration
- [Requirements](code/requirements.txt) - Python dependencies
