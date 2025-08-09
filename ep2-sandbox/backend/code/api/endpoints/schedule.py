# backend/api/endpoints/transactions.py

import json
import uuid
from fastapi import APIRouter, HTTPException, status
from typing import List
from api.models import Schedule

from datetime import datetime, timedelta, timezone

router = APIRouter()

SCHEDULES_FILE = "db/schedule.json"

def read_schedules_data() -> List[Schedule]:
    """Reads schedule data from the JSON file."""
    try:
        with open(SCHEDULES_FILE, "r") as f:
            schedules_data = json.load(f)
        return [Schedule(**s) for s in schedules_data]
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, return an empty list
        return []

def write_schedules_data(schedules: List[Schedule]):
    """Writes the list of schedules back to the JSON file."""
    with open(SCHEDULES_FILE, "w") as f:
        json_data = [s.model_dump() for s in schedules]
        json.dump(json_data, f, indent=4)

@router.post("/users/{user_id}/schedules", response_model=Schedule, status_code=status.HTTP_201_CREATED)
def create_schedule_for_user(user_id: str, schedule_in: Schedule):
    """
    Create a new scheduled transaction for a specific user.
    """
    schedules = read_schedules_data()
    
    # Create a new schedule object with a unique ID and the user_id from the path
    new_schedule = Schedule(
        schedule_id=f"schedule_{uuid.uuid4()}",
        user_id=user_id.replace("_", "-"),
        **schedule_in.model_dump()
    )
    
    schedules.append(new_schedule)
    write_schedules_data(schedules)
    
    return new_schedule
@router.get("/users/{user_id}/schedules", response_model=List[Schedule])
def get_schedules_for_user(user_id: str):
    """
    Retrieve all scheduled transactions for a specific user.
    """
    schedules = read_schedules_data()
    normalized_user_id = user_id.replace("_", "-")
    user_schedules = [s for s in schedules if s.user_id == normalized_user_id]
        
    return user_schedules

@router.put("/schedules/{schedule_id}", response_model=Schedule)
def update_schedule(schedule_id: str, schedule_update: Schedule):
    """
    Update an existing scheduled transaction by its ID.
    """
    schedules = read_schedules_data()
    schedule_index = next((i for i, s in enumerate(schedules) if s.schedule_id == schedule_id), None)

    if schedule_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")
    
    # Get the existing schedule object and update its fields
    existing_schedule = schedules[schedule_index]
    update_data = schedule_update.model_dump(exclude_unset=True) # Only include fields that were provided
    updated_schedule = existing_schedule.model_copy(update=update_data)
    
    schedules[schedule_index] = updated_schedule
    write_schedules_data(schedules)
    
    return updated_schedule

@router.delete("/schedules/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_schedule(schedule_id: str):
    """
    Delete a scheduled transaction by its ID.
    """
    schedules = read_schedules_data()
    
    initial_length = len(schedules)
    schedules_to_keep = [s for s in schedules if s.schedule_id != schedule_id]
    
    if len(schedules_to_keep) == initial_length:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Schedule not found")
    
    write_schedules_data(schedules_to_keep)
    
    # A 204 response does not return any content in the body
    return
