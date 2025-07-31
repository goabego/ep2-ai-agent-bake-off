# agent/council/wealth_planner.py

from agent.tools import financial_tools

class WealthPlannerAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def review_investments(self):
        """
        Reviews the user's investment portfolio.
        """
        accounts = financial_tools.get_user_accounts(self.user_id)
        investment_account = next((acc for acc in accounts if acc['type'] == 'investment'), None)
        if investment_account:
            return f"Your investment portfolio is valued at ${investment_account['balance']}. Let's check your holdings."
        return "No investment account found."
