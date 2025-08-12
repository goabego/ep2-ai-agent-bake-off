import json
from fastapi import APIRouter, HTTPException
from pathlib import Path

router = APIRouter()

@router.get("/partners", tags=["Partners"])
def get_bank_partners():
    """
    Retrieves a list of all available bank partners and their associated benefits.
    """
    try:
        with open(f"db/bank_partners.json", "r") as f:
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
        with open(f"db/users.json", "r") as f:
            users_data = json.load(f)
        with open(f"db/user_personas.json", "r") as f:
            user_personas_data = json.load(f)
        with open(f"db/bank_partners.json", "r") as f:
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
