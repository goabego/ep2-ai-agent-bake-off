
import os
from google.adk.agents import LlmAgent
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from google.adk.tools import FunctionTool
from prompts import AGENT_INSTRUCTIONS
from financial_tools import (
    get_user_profile,
    get_user_accounts,
    get_user_transactions,
    get_user_debts,
    get_user_investments,
    get_user_networth,
    get_user_cashflow,
    get_user_average_cashflow,
    get_user_goals,
    update_user_goal,
    create_user_account,
    get_user_transactions_with_history,
    create_user_goal,
    delete_user_goal,
    get_bank_partners,
    get_user_eligible_partners,
    create_user_schedule,
    get_user_schedules,
    update_user_schedule,
    delete_user_schedule,
    get_all_advisors,
    get_advisors_by_type,
    schedule_meeting,
    get_user_meetings,
    cancel_meeting,
)
import random

def roll_dice(sides: int = 6) -> int:
    """Rolls an N sided dice. If number of sides aren't given, uses 6.

    Args:
    N: the number of the side of the dice to roll.

    Returns:
    A number between 1 and N, inclusive
    """
    return random.randint(1, sides)

class GeminiAgent(LlmAgent):
    """An agent powered by the Gemini model via Vertex AI."""

    # --- AGENT IDENTITY ---
    # These are the default values. The notebook can override them.
    name: str = "gemini_agent"
    description: str = "A helpful assistant powered by Gemini."

    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        # --- SET YOUR SYSTEM INSTRUCTIONS HERE ---
        instructions = AGENT_INSTRUCTIONS + """
            You can roll a dice by using the roll_dice tool using the number of sides as an argument.
            For example, if you want to roll a 6 sided dice, you can use the following command:
            roll_dice(sides=6)
            If you want to roll a 12 sided dice, you can use the following command:
            roll_dice(sides=12)
            If you want to roll a 20 sided dice, you can use the following command:
            roll_dice(sides=20)

            Tool Usage Examples:
            **User:** "Roll a 12 sided dice"
            **Response:** "I'll roll a 12 sided dice for you."
            <tool_code>
            roll_dice(sides=12)
            </tool_code>
        """
        

        # --- REGISTER YOUR TOOLS HERE ---
        tools = [
            get_user_profile,
            get_user_accounts,
            get_user_transactions,
            get_user_debts,
            get_user_investments,
            get_user_networth,
            get_user_cashflow,
            get_user_average_cashflow,
            get_user_goals,
            update_user_goal,
            create_user_account,
            get_user_transactions_with_history,
            create_user_goal,
            delete_user_goal,
            get_bank_partners,
            get_user_eligible_partners,
            create_user_schedule,
            get_user_schedules,
            update_user_schedule,
            delete_user_schedule,
            get_all_advisors,
            get_advisors_by_type,
            schedule_meeting,
            get_user_meetings,
            cancel_meeting,
            FunctionTool(roll_dice)
        ]

        super().__init__(
            model=os.environ.get("MODEL", "gemini-2.5-flash"),
            instruction=instructions,
            tools=tools,
            **kwargs,
        )


    def create_agent_card(self, agent_url: str) -> "AgentCard":
        return AgentCard(
            
            name=self.name,
            description=self.description,
            url=agent_url,
            version="1.0.0",
            defaultInputModes=["application/json", "text/plain"],
            defaultOutputModes=["text/plain"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[
                AgentSkill(
                    id="chat",
                    name="Chat Skill",
                    description="Chat with the Gemini agent.",
                    tags=["chat"],
                    examples=[
                        "What is my user profile?",
                        "Show me my bank accounts.",
                        "List my recent transactions.",
                        "What are my current debts?",
                        "Show me my investment portfolio.",
                        "What is my current net worth?",
                        "What was my cash flow for the last 30 days?",
                        "What is my average monthly cash flow?",
                        "What are my financial goals?",
                        "Help me update my goal to save for a new car.",
                    ]
                ),
                AgentSkill(
                    id="roll_dice",
                    name="Roll Dice Skill",
                    description="Roll a dice of any number of sides.",
                    tags=["roll_dice"],
                )
            ]

        )
