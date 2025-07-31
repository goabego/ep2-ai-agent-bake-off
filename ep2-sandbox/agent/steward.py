# agent/steward.py

from agent.council.banker import PersonalBankerAgent
from agent.council.wealth_planner import WealthPlannerAgent
from agent.council.tax_strategist import TaxStrategistAgent

class FinancialStewardAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.council = {
            "banker": PersonalBankerAgent(user_id),
            "wealth_planner": WealthPlannerAgent(user_id),
            "tax_strategist": TaxStrategistAgent(user_id),
        }

    def generate_living_briefing(self, query: str):
        """
        Generates a "Living Briefing" by consulting the AI council.
        """
        # This is a simplified example of the multi-agent collaboration.
        # A real implementation would use a more sophisticated orchestration engine.
        
        briefing = f"Living Briefing for query: '{query}'\n\n"
        
        banker_insight = self.council["banker"].analyze_cash_flow()
        briefing += f"[Personal Banker]: {banker_insight}\n"
        
        wealth_planner_insight = self.council["wealth_planner"].review_investments()
        briefing += f"[Wealth Planner]: {wealth_planner_insight}\n"
        
        tax_strategist_insight = self.council["tax_strategist"].find_tax_savings()
        briefing += f"[Tax Strategist]: {tax_strategist_insight}\n"
        
        return briefing
