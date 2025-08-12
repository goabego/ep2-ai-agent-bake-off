# Cymbal Bank FastAPI Backend

A comprehensive FastAPI-based REST API for personal financial management, providing access to financial data, user profiles, account management, and financial analytics.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Podman/Docker

### Running with Podman
```bash
cd ep2-sandbox/backend
podman build -t cymbal-bank-api .
podman run -p 8080:8080 cymbal-bank-api
```

### Running with Docker
```bash
cd ep2-sandbox/backend
docker build -t cymbal-bank-api .
docker run -p 8080:8080 cymbal-bank-api
```

### Development Mode
```bash
cd ep2-sandbox/backend/code
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

## 📚 API Documentation

Once running, access the interactive API documentation at:
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc
- **OpenAPI JSON**: http://localhost:8080/openapi.json

## 🏗️ Architecture

### Project Structure
```
backend/
├── code/
│   ├── api/
│   │   ├── endpoints/          # API route handlers
│   │   ├── models.py          # Pydantic data models
│   │   └── API_OVERVIEW.md    # Detailed API documentation
│   ├── core/
│   │   └── config.py          # Configuration settings
│   ├── db/                    # JSON data storage
│   ├── images/                # User profile images
│   ├── main.py                # FastAPI application entry point
│   └── requirements.txt       # Python dependencies
├── Dockerfile                 # Container configuration
├── pyproject.toml            # Poetry configuration
└── README.md                 # This file
```

### Technology Stack
- **Framework**: FastAPI 0.104.1
- **Data Validation**: Pydantic 2.11.7
- **Server**: Uvicorn + Gunicorn
- **Data Storage**: JSON files (simulated database)
- **Authentication**: Google Cloud ID tokens
- **CORS**: Enabled for all origins

## 🔌 API Endpoints

### Base Configuration
- **Base URL**: `/api`
- **API Version**: 0.1.0
- **Title**: Cymbal Bank API

### Core Endpoints

#### 🔐 Authentication
- `GET /token` - Get Google Cloud ID token for A2A service authentication

#### 👥 Users
- `GET /api/users/{user_id}` - Get user profile with calculated net worth
- `GET /api/users/{user_id}/accounts` - Get all user accounts
- `GET /api/users/{user_id}/transactions` - Get user transaction history
- `GET /api/users/{user_id}/debts` - Get user debt accounts
- `GET /api/users/{user_id}/investments` - Get user investment accounts
- `GET /api/users/{user_id}/networth` - Calculate user's net worth
- `GET /api/users/{user_id}/cashflow` - Calculate 30-day cash flow
- `GET /api/users/{user_id}/average_cashflow` - Calculate average monthly cash flow

#### 🏦 Accounts
- `GET /api/users/{user_id}/accounts` - Get all user accounts

#### 💰 Transactions
- `GET /api/users/{user_id}/transactions` - Get all user transactions

#### 🎯 Goals
- `GET /api/goals/{user_id}` - Get user's financial goals
- `PUT /api/goals/{goal_id}` - Update a financial goal

#### 📊 Financials
- `GET /api/users/{user_id}/debts` - Get debt accounts
- `GET /api/users/{user_id}/investments` - Get investment accounts
- `GET /api/users/{user_id}/networth` - Calculate net worth
- `GET /api/users/{user_id}/cashflow` - Calculate cash flow
- `GET /api/users/{user_id}/average_cashflow` - Calculate average cash flow

#### 🤝 Partners
- `GET /api/partners` - Get all bank partners and benefits
- `GET /api/partners/user/{user_id}` - Get user-specific partner benefits

#### 📅 Schedule
- `POST /api/users/{user_id}/schedules` - Create scheduled transaction
- `GET /api/users/{user_id}/schedules` - Get user's scheduled transactions
- `PUT /api/schedules/{schedule_id}` - Update scheduled transaction
- `DELETE /api/schedules/{schedule_id}` - Delete scheduled transaction

#### 📋 Meeting
- Full CRUD operations for financial advisor meetings

#### 🔄 Proxy
- `POST /proxy/a2a` - Proxy requests to A2A service with authentication

## 📊 Data Models

### Core Financial Models

#### User Profile
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

#### Account Information
```python
class Account(BaseModel):
    account_id: str
    user_id: str
    category: str          # "asset" or "liability"
    type: str              # "checking", "savings", "investment", "credit"
    sub_type: str
    description: str
    balance: float
    institution: Optional[str] = None
    holdings: Optional[List[Holding]] = None
    interest_rate: Optional[float] = None
```

#### Transaction Records
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

#### Financial Goals
```python
class LifeGoal(BaseModel):
    goal_id: str
    user_id: str
    description: str
    target_amount: float
    target_date: str
    current_amount_saved: float
```

## 🔐 Authentication & Security

### Google Cloud Integration
- **ID Token Authentication**: Uses Google Cloud metadata server for service-to-service authentication
- **A2A Service Integration**: Supports Agent-to-Agent communication with proper token handling
- **Environment Configuration**: Configurable A2A agent URL via `A2A_AGENT_URL` environment variable

### CORS Configuration
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 💾 Data Storage

### JSON File Storage
The API uses JSON files in the `db/` directory as a simulated database:

- `users.json` - User profiles and personal information
- `accounts.json` - Account information and balances
- `transactions.json` - Transaction history
- `bank_partners.json` - Bank partner information and benefits
- `life_goals.json` - Financial goals and targets
- `meetings.json` - Financial advisor meetings
- `schedule.json` - Scheduled transactions

### Data Loading Functions
Each endpoint module includes utility functions:
- `read_users_data()` - Load user data from JSON
- `read_accounts_data()` - Load account data from JSON
- `read_transactions_data()` - Load transaction data from JSON
- `load_data(file_name: str)` - Generic data loading function

## 🚀 Deployment

### Docker Configuration
```dockerfile
FROM python:3.11-slim-bookworm
WORKDIR /app
COPY code/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "main:app"]
```

### Environment Variables
- `A2A_AGENT_URL` - URL for the A2A service (defaults to production URL)

### Production Considerations
- Configure CORS origins for production
- Implement proper logging and monitoring
- Add rate limiting and request validation
- Consider database migration from JSON files
- Implement proper error tracking

## 🧪 Testing

### Health Check
```bash
curl http://localhost:8080/
# Response: {"status": "ok", "message": "Welcome to the AI Financial Steward API"}
```

### API Testing
```bash
# Get user profile
curl http://localhost:8080/api/users/user01_marcus_w

# Get user accounts
curl http://localhost:8080/api/users/user01_marcus_w/accounts

# Get user transactions
curl http://localhost:8080/api/users/user01_marcus_w/transactions
```

## 🔧 Development

### Adding New Endpoints
1. Create endpoint handler in `api/endpoints/`
2. Define data models in `api/models.py`
3. Add router to `main.py`
4. Update `API_OVERVIEW.md` documentation

### Data Model Updates
1. Modify Pydantic models in `api/models.py`
2. Update corresponding JSON data files
3. Test endpoint functionality
4. Update API documentation

## 📈 Features

### Financial Analytics
- **Net Worth Calculation**: Automatic calculation from asset and liability accounts
- **Cash Flow Analysis**: 30-day and 3-month average calculations
- **Account Categorization**: Asset, liability, investment, and credit account filtering
- **Transaction Tracking**: Comprehensive transaction history with categorization

### User Management
- **Profile Management**: Complete user profiles with financial information
- **Goal Setting**: Financial goal creation and tracking
- **Risk Assessment**: Risk tolerance and financial profile management

### Integration Capabilities
- **A2A Service Proxy**: Seamless integration with Agent-to-Agent services
- **Google Cloud Authentication**: Production-ready authentication system
- **CORS Support**: Frontend integration ready

## 🤝 Contributing

1. Follow the existing code structure
2. Add comprehensive error handling
3. Update API documentation
4. Test with sample data
5. Ensure CORS compatibility

## 📄 License

This project is part of the EP2 AI Agent Bake-off sandbox environment.

---

For detailed API endpoint documentation, see [API_OVERVIEW.md](code/api/API_OVERVIEW.md)
