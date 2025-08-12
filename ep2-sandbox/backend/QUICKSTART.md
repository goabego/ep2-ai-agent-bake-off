# Cymbal Bank API - Quick Start Guide

Get up and running with the Cymbal Bank FastAPI backend in under 5 minutes.

## 🚀 Prerequisites

- Python 3.11+
- Podman or Docker
- Git

## ⚡ Quick Start (3 Options)

### Option 1: Docker (Fastest)
```bash
# Clone and run
git clone <your-repo>
cd ep2-sandbox/backend
docker build -t cymbal-bank-api .
docker run -p 8080:8080 cymbal-bank-api

# Test it
curl http://localhost:8080/
# Should return: {"status": "ok", "message": "Welcome to the AI Financial Steward API"}
```

### Option 2: Podman
```bash
# Clone and run
git clone <your-repo>
cd ep2-sandbox/backend
podman build -t cymbal-bank-api .
podman run -p 8080:8080 cymbal-bank-api

# Test it
curl http://localhost:8080/
```

### Option 3: Local Development
```bash
# Clone and setup
git clone <your-repo>
cd ep2-sandbox/backend/code
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8080

# Test it
curl http://localhost:8080/
```

## 📚 API Documentation

Once running, access the interactive docs:
- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

## 🧪 Test the API

### Health Check
```bash
curl http://localhost:8080/
```

### Get User Profile
```bash
curl http://localhost:8080/api/users/user01_marcus_w
```

### Get User Accounts
```bash
curl http://localhost:8080/api/users/user01_marcus_w/accounts
```

### Get User Transactions
```bash
curl http://localhost:8080/api/users/user01_marcus_w/transactions
```

## 🔍 Sample Data

The API comes with sample data for 10 users:

| User ID | Name | Age | Risk Profile |
|---------|------|-----|--------------|
| `user01_marcus_w` | Marcus W. | 35 | Moderate |
| `user02_janet_d` | Janet D. | 42 | Conservative |
| `user03_david_p` | David P. | 28 | Aggressive |
| `user04_fiona_r` | Fiona R. | 38 | Moderate |
| `user05_priya_s` | Priya S. | 31 | Conservative |
| `user06_dmitri_v` | Dmitri V. | 45 | Aggressive |
| `user07_montserrat_p` | Montserrat P. | 33 | Moderate |
| `user08_dusty_p` | Dusty P. | 29 | Conservative |
| `user09_margaret_t` | Margaret T. | 52 | Moderate |
| `user10_ashwin_k` | Ashwin K. | 26 | Aggressive |

## 🏗️ Project Structure

```
backend/
├── code/
│   ├── api/
│   │   ├── endpoints/          # API routes
│   │   ├── models.py          # Data models
│   │   └── API_OVERVIEW.md    # Detailed docs
│   ├── core/
│   │   └── config.py          # Configuration
│   ├── db/                    # JSON data files
│   ├── images/                # User profile images
│   ├── main.py                # FastAPI app
│   └── requirements.txt       # Dependencies
├── Dockerfile                 # Container config
├── README.md                  # Full documentation
├── API_REFERENCE.md           # API reference
└── QUICKSTART.md              # This file
```

## 🔧 Key Features

### Financial Analytics
- ✅ Net worth calculation
- ✅ Cash flow analysis (30-day & 3-month)
- ✅ Account categorization (assets, liabilities, investments)
- ✅ Transaction tracking

### User Management
- ✅ Complete user profiles
- ✅ Financial goal setting
- ✅ Risk assessment
- ✅ Profile pictures

### Integration Ready
- ✅ CORS enabled for frontend
- ✅ A2A service proxy
- ✅ Google Cloud authentication
- ✅ JSON data storage

## 🚨 Common Issues

### Port Already in Use
```bash
# Find what's using port 8080
lsof -i :8080
# Kill the process
kill -9 <PID>

# Or use a different port
uvicorn main:app --reload --host 0.0.0.0 --port 8081
```

### Permission Denied (Docker)
```bash
# On macOS/Linux, you might need sudo
sudo docker run -p 8080:8080 cymbal-bank-api
```

### Module Not Found
```bash
# Make sure you're in the right directory
cd ep2-sandbox/backend/code
pip install -r requirements.txt
```

## 📱 Frontend Integration

### CORS Configuration
The API is configured to allow all origins:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Example Frontend Request
```javascript
// Get user profile
fetch('http://localhost:8080/api/users/user01_marcus_w')
  .then(response => response.json())
  .then(data => console.log(data));

// Get user accounts
fetch('http://localhost:8080/api/users/user01_marcus_w/accounts')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🔄 Development Workflow

### 1. Make Changes
```bash
# Edit endpoint files in code/api/endpoints/
# Edit models in code/api/models.py
# Edit main app in code/main.py
```

### 2. Test Locally
```bash
cd code
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

### 3. Test with Sample Data
```bash
curl http://localhost:8080/api/users/user01_marcus_w
```

### 4. Rebuild Container (if needed)
```bash
docker build -t cymbal-bank-api .
docker run -p 8080:8080 cymbal-bank-api
```

## 📊 Data Models

### Quick Reference
- **User**: Profile, risk tolerance, goals
- **Account**: Financial accounts (checking, savings, investments, credit)
- **Transaction**: Purchase history, amounts, categories
- **Goal**: Financial targets and progress
- **Schedule**: Recurring transactions
- **Meeting**: Financial advisor appointments

### Sample Data Access
```bash
# View raw JSON data
cat code/db/users.json
cat code/db/accounts.json
cat code/db/transactions.json
```

## 🎯 Next Steps

1. **Explore the API**: Use the Swagger UI at http://localhost:8080/docs
2. **Test Endpoints**: Try the sample requests above
3. **Read Documentation**: Check README.md and API_REFERENCE.md
4. **Build Frontend**: Integrate with your React/Vue/Angular app
5. **Customize**: Modify data models and endpoints as needed

## 📞 Need Help?

- **API Documentation**: http://localhost:8080/docs
- **Full Documentation**: README.md
- **API Reference**: API_REFERENCE.md
- **Code Examples**: Check the endpoint files in `code/api/endpoints/`

---

**Happy Coding! 🚀**

The Cymbal Bank API is designed to be developer-friendly with comprehensive documentation, sample data, and easy setup. Get started quickly and build amazing financial applications!
