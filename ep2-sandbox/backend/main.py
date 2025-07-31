# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.endpoints import users, accounts, goals, transactions, financials
from backend.core.config import API_PREFIX

app = FastAPI(
    title="AI Financial Steward API",
    description="API for the AI Financial Steward, providing access to financial data.",
    version="0.1.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(users.router, prefix=API_PREFIX, tags=["Users"])
app.include_router(accounts.router, prefix=API_PREFIX, tags=["Accounts"])
app.include_router(goals.router, prefix=API_PREFIX, tags=["Goals"])
app.include_router(transactions.router, prefix=API_PREFIX, tags=["Transactions"])
app.include_router(financials.router, prefix=API_PREFIX, tags=["Financials"])

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for health checks.
    """
    return {"status": "ok", "message": "Welcome to the AI Financial Steward API"}
