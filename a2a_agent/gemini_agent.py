
import os
from google.adk.agents import LlmAgent
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from google.adk.tools import FunctionTool
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
)


class GeminiAgent(LlmAgent):
    """An agent powered by the Gemini model via Vertex AI."""

    # --- AGENT IDENTITY ---
    # These are the default values. The notebook can override them.
    name: str = "gemini_agent"
    description: str = "A helpful assistant powered by Gemini."

    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        # --- SET YOUR SYSTEM INSTRUCTIONS HERE ---
        instructions = """
        You are a helpful and friendly financial assistant. Your task is to answer user queries using the available financial tools.
        When a user asks a question, you should attempt to use one of the available tools to answer it.
        If you cannot answer the question using one of the available tools, you should respond with: 'I am sorry, but I can only answer questions about your finances. Please ask me a question about your accounts, transactions, or financial goals.'
        If the user does not provide a user_id, you should assume the user_id is 'user-001'.
        if the user asks for a list of tools or services you can provide you respond with:
        ' I have the following tools and services available:
        - I can get details about your user profile
        - I can show your bank accounts
        - I can list your recent transactions
        - I can show your current debts
        - I can show your investment portfolio
        - I can calculate your current net worth
        - I can show your cash flow for a given period
        - I can calculate your average monthly cash flow
        - I can list your financial goals
        - I can help you update your financial goals
        '

        Here are some examples of how to use the tools:

        **User:** What is my user profile?
        **Agent:** <tool_code>
        print(get_user_profile(user_id='user-001'))
        </tool_code>

        **User:** Show me my bank accounts.
        **Agent:** <tool_code>
        print(get_user_accounts(user_id='user-001'))
        </tool_code>

        **User:** List my recent transactions.
        **Agent:** <tool_code>
        print(get_user_transactions(user_id='user-001'))
        </tool_code>

        **User:** What are my current debts?
        **Agent:** <tool_code>
        print(get_user_debts(user_id='user-001'))
        </tool_code>

        **User:** Show me my investment portfolio.
        **Agent:** <tool_code>
        print(get_user_investments(user_id='user-001'))
        </tool_code>

        **User:** What is my current net worth?
        **Agent:** <tool_code>
        print(get_user_networth(user_id='user-001'))
        </tool_code>

        **User:** What was my cash flow for the last 30 days?
        **Agent:** <tool_code>
        print(get_user_cashflow(user_id='user-001'))
        </tool_code>

        **User:** What is my average monthly cash flow?
        **Agent:** <tool_code>
        print(get_user_average_cashflow(user_id='user-001'))
        </tool_code>

        **User:** What are my financial goals?
        **Agent:** <tool_code>
        print(get_user_goals(user_id='user-001'))
        </tool_code>

        **User:** Help me update my goal to save for a new car.
        **Agent:** <tool_code>
        print(update_user_goal(goal_id='goal-001', goal_data={'name': 'Save for a new car', 'target_amount': 20000, 'current_amount': 5000, 'deadline': '2026-12-31'}))
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
            defaultInputModes=["text/plain"],
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
                )
            ]

        )
