import json
from fastapi import APIRouter, HTTPException
from pathlib import Path

router = APIRouter()

# Define the path to the JSON files
db_path = Path(__file__).resolve().parent.parent.parent.parent / "db"
partners_file_path = db_path / "bank_partners.json"
users_file_path = db_path / "users.json"
user_personas_file_path = db_path / "user_personas.json"

@router.get("/partners", tags=["Partners"])
def get_bank_partners():
    """
    Retrieves a list of all available bank partners and their associated benefits.
    """
    try:
        with open(partners_file_path, "r") as f:
            partners_data = json.load(f)
        return partners_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Bank partners file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding bank partners JSON.")

@router.get("/partners/user/{user_id}", tags=["Partners"])
def get_user_benefits(user_id: str):
    """
    Identifies and returns a list of partners a specific user can benefit from.
    """
    try:
        with open(users_file_path, "r") as f:
            users_data = json.load(f)
        with open(user_personas_file_path, "r") as f:
            user_personas_data = json.load(f)
        with open(partners_file_path, "r") as f:
            partners_data = json.load(f)

        user = next((user for user in users_data if user["user_id"] == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        user_persona = next((persona for persona in user_personas_data if persona["user_id"] == user_id), None)
        if not user_persona:
            raise HTTPException(status_code=404, detail="User persona not found.")

        user_credit_score = user_persona.get("credit_score")

        eligible_partners = []
        for partner in partners_data:
            eligibility = partner.get("eligibility_criteria")
            if not eligibility or "minimum_credit_score" not in eligibility:
                eligible_partners.append(partner)
            elif user_credit_score and user_credit_score >= eligibility["minimum_credit_score"]:
                eligible_partners.append(partner)

        return eligible_partners

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding JSON.")
