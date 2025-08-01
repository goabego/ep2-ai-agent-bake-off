import json
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import re

# --- Configuration ---
# IMPORTANT: You must set your GOOGLE_API_KEY as an environment variable
# for this script to work.
# For example, in your terminal:
# export GOOGLE_API_KEY="YOUR_API_KEY"
API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-1.5-pro-latest" # Using a powerful, recent model
USER_PERSONAS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'user_personas.json')
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db')
USERS_DB_PATH = os.path.join(DB_PATH, 'users.json')
ACCOUNTS_DB_PATH = os.path.join(DB_PATH, 'accounts.json')
TRANSACTIONS_DB_PATH = os.path.join(DB_PATH, 'transactions.json')
LIFE_GOALS_DB_PATH = os.path.join(DB_PATH, 'life_goals.json')


def get_model():
    """Initializes and returns the generative model."""
    if not API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    genai.configure(api_key=API_KEY)

    # Safety settings to avoid blocking potentially relevant financial content
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    return genai.GenerativeModel(MODEL_NAME, safety_settings=safety_settings)

def read_user_personas():
    """Reads the user personas from the JSON file."""
    with open(USER_PERSONAS_PATH, 'r') as f:
        return json.load(f)["users"]

def generate_json_from_prompt(model, prompt):
    """Generates a JSON string from a given prompt using the model."""
    try:
        response = model.generate_content(prompt)
        text_response = response.text.strip()
        # The model sometimes wraps the JSON in ```json ... ```, so we need to extract it.
        if text_response.startswith("```json"):
            text_response = text_response[7:-3].strip()

        # Remove comments from the JSON string
        text_response = re.sub(r'//.*?\n', '\n', text_response)
        text_response = re.sub(r'/\*.*?\*/', '', text_response, flags=re.DOTALL)

        return json.loads(text_response)
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error generating or parsing JSON for prompt.")
        print(f"Prompt: {prompt[:200]}...") # Print first 200 chars of prompt
        print(f"Response text: {response.text if 'response' in locals() else 'No response'}")
        print(f"Error: {e}")
        return None


def generate_user_data(model, persona, user_id):
    """Generates user data based on a persona."""
    prompt = f"""
    Based on the following persona, generate a user JSON object.
    The user_id must be "{user_id}".
    The credit_score should be a realistic integer between 300 and 850.

    Persona:
    {json.dumps(persona, indent=2)}

    Your output must be a single JSON object. Do not include comments.
    Example format:
    {{
      "user_id": "user-001",
      "name": "Marcus W.",
      "age": 24,
      "risk_tolerance": "moderate-high",
      "profile_picture": "user01_marcus_w.jpg",
      "credit_score": 620
    }}
    """
    return generate_json_from_prompt(model, prompt)


def generate_accounts_data(model, persona, user_id):
    """Generates accounts data for a user."""
    prompt = f"""
    Based on the following persona, generate a list of financial account JSON objects for the user with user_id "{user_id}".
    - Create a mix of asset and liability accounts that are realistic for the persona.
    - Assets should have positive balances, liabilities should have negative balances.
    - Include checking, savings, investments (like 401k, IRA, brokerage), and liabilities (like student loans, credit cards, mortgage).
    - For investment accounts, include a 'holdings' list with stock symbols and values.
    - For liability accounts, include an 'interest_rate'.
    - Create a unique, descriptive account_id for each account.

    Persona:
    {json.dumps(persona, indent=2)}

    Your output must be a JSON list of objects. Do not include comments.
    Example format:
    [
      {{
        "account_id": "acc-mw-c-001",
        "user_id": "{user_id}",
        "category": "asset",
        "type": "cash",
        "sub_type": "checking",
        "description": "Primary Checking",
        "balance": 8500.00,
        "institution": "Acme Bank"
      }},
      {{
        "account_id": "acc-mw-d-006",
        "user_id": "{user_id}",
        "category": "liability",
        "type": "loan",
        "sub_type": "student_loan",
        "description": "Student Loan",
        "balance": -60000.00,
        "institution": "Acme Education Services",
        "interest_rate": 0.058
      }}
    ]
    """
    return generate_json_from_prompt(model, prompt)

def generate_transactions_data(model, persona, accounts):
    """Generates transactions data for a user's accounts."""
    if not accounts:
        return []
    account_ids = [acc['account_id'] for acc in accounts]
    prompt = f"""
    Based on the following persona and list of accounts, generate a realistic list of at least 20 transaction JSON objects for the past 3 months.
    - The transactions must be for the account_ids listed below.
    - Transactions should reflect the user's income, spending habits, savings, and debt repayments as described in the persona.
    - Income transactions should be positive amounts.
    - Expense and debt payment transactions should be negative amounts.
    - Create a variety of categories (e.g., 'Income', 'Housing', 'Groceries', 'Dining', 'Transfers', 'Debt', 'Shopping', 'Entertainment').
    - Create a unique transaction_id for each transaction.

    Persona:
    {json.dumps(persona, indent=2)}

    Accounts:
    {json.dumps(accounts, indent=2)}

    Your output must be a JSON list of objects. Do not include comments.
    Example format:
    [
      {{
        "transaction_id": "txn-unique-001",
        "account_id": "{account_ids[0]}",
        "date": "2025-07-15T09:00:00Z",
        "description": "Paycheck - Tech Company",
        "amount": 4000.00,
        "category": "Income"
      }},
      {{
        "transaction_id": "txn-unique-002",
        "account_id": "{account_ids[0]}",
        "date": "2025-07-01T10:00:00Z",
        "description": "Rent Payment",
        "amount": -2000.00,
        "category": "Housing"
      }}
    ]
    """
    return generate_json_from_prompt(model, prompt)


def generate_life_goals_data(model, persona, user_id):
    """Generates life goals data for a user."""
    prompt = f"""
    Based on the following persona, generate a list of life goal JSON objects for the user with user_id "{user_id}".
    - The goals should be based on the "goals" section of the persona.
    - Create realistic target amounts and target dates.
    - 'current_amount_saved' should be a plausible amount given the persona's financial situation.
    - Create a unique goal_id for each goal.

    Persona:
    {json.dumps(persona, indent=2)}

    Your output must be a JSON list of objects. Do not include comments.
    Example format:
    [
      {{
        "goal_id": "goal-buy-house-001",
        "user_id": "{user_id}",
        "description": "Buy a house",
        "target_amount": 750000.00,
        "target_date": "2030-01-01",
        "current_amount_saved": 120000.00
      }}
    ]
    """
    return generate_json_from_prompt(model, prompt)


def generate_mock_data():
    """
    Generates all mock data and saves it to the database files.
    """
    print("Initializing generative model...")
    try:
        model = get_model()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please make sure the GOOGLE_API_KEY environment variable is set.")
        return

    print("Reading user personas...")
    personas = read_user_personas()

    all_users = []
    all_accounts = []
    all_transactions = []
    all_life_goals = []

    for i, persona in enumerate(personas):
        user_id = f"user-{i+1:03d}"
        print(f"--- Generating data for {persona['name']} ({user_id}) ---")

        print("Generating user data...")
        user_data = generate_user_data(model, persona, user_id)
        if user_data:
            all_users.append(user_data)

        print("Generating accounts data...")
        accounts_data = generate_accounts_data(model, persona, user_id)
        if accounts_data:
            all_accounts.extend(accounts_data)

            print("Generating transactions data...")
            transactions_data = generate_transactions_data(model, persona, accounts_data)
            if transactions_data:
                all_transactions.extend(transactions_data)

        print("Generating life goals data...")
        life_goals_data = generate_life_goals_data(model, persona, user_id)
        if life_goals_data:
            all_life_goals.extend(life_goals_data)

    print("\n--- Writing data to database files ---")

    os.makedirs(DB_PATH, exist_ok=True)

    with open(USERS_DB_PATH, 'w') as f:
        json.dump(all_users, f, indent=2)
    print(f"Wrote {len(all_users)} users to {USERS_DB_PATH}")

    with open(ACCOUNTS_DB_PATH, 'w') as f:
        json.dump(all_accounts, f, indent=2)
    print(f"Wrote {len(all_accounts)} accounts to {ACCOUNTS_DB_PATH}")

    with open(TRANSACTIONS_DB_PATH, 'w') as f:
        json.dump(all_transactions, f, indent=2)
    print(f"Wrote {len(all_transactions)} transactions to {TRANSACTIONS_DB_PATH}")

    with open(LIFE_GOALS_DB_PATH, 'w') as f:
        json.dump(all_life_goals, f, indent=2)
    print(f"Wrote {len(all_life_goals)} life goals to {LIFE_GOALS_DB_PATH}")

    print("\nMock data generation complete!")


if __name__ == "__main__":
    generate_mock_data()
