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
    profile_picture: Optional[str] = None
    address: Optional[str] = None
    credit_score: Optional[int] = None
    net_worth: Optional[float] = None
    member_since: Optional[int] = None
    financial_blurb: str
    goals: List[str]

class Transaction(BaseModel):
    transaction_id: str
    account_id: str
    merchant_id: str
    date: str
    description: str
    amount: float
    category: str

class EligibilityCriteria(BaseModel):
    minimum_credit_score: Optional[int] = None

class BankPartner(BaseModel):
    partner_id: str
    merchant_id: str
    name: str
    category: str
    benefit_type: str
    benefit_value: float
    eligibility_criteria: Optional[EligibilityCriteria] = None

class LifeGoal(BaseModel):
    goal_id: str
    user_id: str
    description: str
    target_amount: float
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
