# agent/council/banker.py

from agent.tools import financial_tools

class PersonalBankerAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def analyze_cash_flow(self):
        """
        Analyzes the user's cash flow and spending habits.
        """
        transactions = financial_tools.get_user_transactions(self.user_id)
        if not transactions:
            return "No transactions found for this user."

        # In a real implementation, this would involve more complex logic
        # to analyze transactions and provide insights.
        total_spending = sum(tx['amount'] for tx in transactions if tx['amount'] < 0)
        total_income = sum(tx['amount'] for tx in transactions if tx['amount'] > 0)

        return f"Your total income is ${total_income:,.2f} and your total spending is ${abs(total_spending):,.2f}. Let's review your recent transactions to find opportunities to save."
