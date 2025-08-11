# backend/api/endpoints/goals.py

import json
from fastapi import APIRouter, HTTPException
from typing import List
from api.models import LifeGoal

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

@router.post("/goals", response_model=LifeGoal, status_code=status.HTTP_201_CREATED)
def create_goal(goal_payload: LifeGoal):
    """
    Create a new financial goal. The goal_id is generated automatically.
    """
    goals = read_goals_data()
    
    # Create a new LifeGoal instance to ensure a server-generated UUID
    new_goal = LifeGoal(
        user_id=goal_payload.user_id,
        name=goal_payload.name,
        target_amount=goal_payload.target_amount,
        current_amount=goal_payload.current_amount
    )
    
    goals.append(new_goal)
    write_goals_data(goals)
    return new_goal

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

@router.delete("/goals/{goal_id}", status_code=204)
def cancel_goal(goal_id: str):
    """
    Cancel a customer goal.
    """
    goals = read_goals_data()
    goal_to_delete = next((g for g in goals if g.goal_id == goal_id), None)

    if not goal_to_delete:
        raise HTTPException(status_code=404, detail="Goal not found")

    updated_goals = [g.model_dump() for g in goals if g.goal_id != goal_id]
    write_goals_data(updated_goals)
    return