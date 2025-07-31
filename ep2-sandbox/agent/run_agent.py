# run_agent.py

from agent.steward import FinancialStewardAgent
import os
import sys

# This script is for demonstrating the agent's functionality.
# Before running this, make this sure the FastAPI server is running.
# You can run the server with the following command from the project root:
# uvicorn backend.main:app --reload

def main():
    # This is a bit of a hack to make the imports work when running from the root directory.
    # In a real application, this would be handled by a proper package installation.
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    print("Initializing the AI Financial Steward...")
    # We'll use the mock user for this demonstration
    user_id = "user-123"
    steward = FinancialStewardAgent(user_id)

    print("\n--- Generating a Living Briefing ---")
    query = "I want to buy a new car. What should I consider?"
    briefing = steward.generate_living_briefing(query)
    print(briefing)

if __name__ == "__main__":
    main()
