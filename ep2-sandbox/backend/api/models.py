# app/api/models.py

from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Holding(BaseModel):
    symbol: str
    value: float

class Account(BaseModel):
    account_id: str
    user_id: str
    category: str
    type: str
    sub_type: str
    description: str
    balance: float
    institution: Optional[str] = None
    holdings: Optional[List[Holding]] = None
    interest_rate: Optional[float] = None

class User(BaseModel):
    user_id: str
    name: str
    age: int
    risk_tolerance: str
    life_goals: Optional[List[str]] = None
    profile_picture: Optional[str] = None
    credit_score: Optional[int] = None

class Transaction(BaseModel):
    transaction_id: str
    account_id: str
    date: str
    description: str
    amount: float
    category: str

class LifeGoal(BaseModel):
    goal_id: str
    user_id: str
    description: str
    target_amount: Optional[float] = None
    target_date: str
    current_amount_saved: float

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

class NetWorth(BaseModel):
    net_worth: float

class CashFlow(BaseModel):
    cash_flow_last_30_days: float

class AverageCashFlow(BaseModel):
    average_monthly_cash_flow: float
