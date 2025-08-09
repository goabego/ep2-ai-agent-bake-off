import json
from fastapi import APIRouter, HTTPException, Body
from typing import List
from api.models import Advisor, Meeting
import datetime

router = APIRouter()

ADVISOR_DATA_FILE = "db/advisors.json"
MEETING_DATA_FILE = "db/meetings.json"

# Helper functions for data handling
def read_data(file_path: str) -> list:
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_data(file_path: str, data: list):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2, default=str) # Use default=str for datetime

def get_advisors() -> List[Advisor]:
    advisors_data = read_data(ADVISOR_DATA_FILE)
    return [Advisor(**advisor) for advisor in advisors_data]

def get_meetings() -> List[Meeting]:
    meetings_data = read_data(MEETING_DATA_FILE)
    return [Meeting(**meeting) for meeting in meetings_data]

# --- API Endpoints ---

@router.get("/advisors", response_model=List[Advisor])
def list_advisors():
    """
    Get a list of all available financial advisors.
    """
    return get_advisors()

@router.get("/advisors/{advisor_type}", response_model=List[Advisor])
def get_advisors_by_type(advisor_type: str):
    """
    Get advisors by their specialization type.
    """
    advisors = get_advisors()
    filtered_advisors = [adv for adv in advisors if adv.advisor_type.lower() == advisor_type.lower()]
    if not filtered_advisors:
        raise HTTPException(status_code=404, detail=f"No advisors found for type: {advisor_type}")
    return filtered_advisors

@router.post("/meetings", response_model=Meeting, status_code=201)
def schedule_meeting(meeting_request: Meeting):
    """
    Schedule a new meeting with an advisor.
    """
    meetings = [m.model_dump() for m in get_meetings()]
    
    # Simple validation to prevent double booking the exact same time
    for existing_meeting in meetings:
        if existing_meeting['advisor_id'] == meeting_request.advisor_id and \
           existing_meeting['meeting_time'] == meeting_request.meeting_time.isoformat():
            raise HTTPException(status_code=409, detail="This time slot is already booked with the advisor.")

    new_meeting = meeting_request.model_dump()
    meetings.append(new_meeting)
    write_data(MEETING_DATA_FILE, meetings)
    return Meeting(**new_meeting)


@router.get("/meetings/{user_id}", response_model=List[Meeting])
def get_user_meetings(user_id: str):
    """
    Get all scheduled meetings for a specific user.
    """
    meetings = get_meetings()
    user_meetings = [meeting for meeting in meetings if meeting.user_id == user_id]
    return user_meetings

@router.delete("/meetings/{meeting_id}", status_code=204)
def cancel_meeting(meeting_id: str):
    """
    Cancel a scheduled meeting.
    """
    meetings = get_meetings()
    meeting_to_delete = next((m for m in meetings if m.meeting_id == meeting_id), None)

    if not meeting_to_delete:
        raise HTTPException(status_code=404, detail="Meeting not found")

    updated_meetings = [m.model_dump() for m in meetings if m.meeting_id != meeting_id]
    write_data(MEETING_DATA_FILE, updated_meetings)
    return
