# backend/api/endpoints/goals.py

import json
from fastapi import APIRouter, HTTPException
from typing import List
from backend.api.models import LifeGoal

router = APIRouter()

DATA_FILE = "db/life_goals.json"

def read_goals_data() -> List[LifeGoal]:
    with open(DATA_FILE, "r") as f:
        goals_data = json.load(f)
    return [LifeGoal(**goal) for goal in goals_data]

def write_goals_data(goals: List[LifeGoal]):
    with open(DATA_FILE, "w") as f:
        json.dump([goal.model_dump() for goal in goals], f, indent=2)

@router.get("/goals/{user_id}", response_model=List[LifeGoal])
def get_user_goals(user_id: str):
    """
    Get user's financial goals.
    """
    normalized_user_id = user_id.replace("_", "-")
    goals = read_goals_data()
    user_goals = [goal for goal in goals if goal.user_id == normalized_user_id]
    return user_goals

@router.put("/goals/{goal_id}", response_model=LifeGoal)
def update_goal(goal_id: str, updated_goal: LifeGoal):
    """
    Update a financial goal.
    """
    goals = read_goals_data()
    goal_index = next((i for i, goal in enumerate(goals) if goal.goal_id == goal_id), None)

    if goal_index is None:
        raise HTTPException(status_code=404, detail="Goal not found")

    goals[goal_index] = updated_goal
    write_goals_data(goals)
    return updated_goal
