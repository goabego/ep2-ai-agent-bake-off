
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
    description: str = "A sophisticated financial intelligence assistant powered by Gemini, providing comprehensive account management and real-time financial insights."

    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        # --- SET YOUR SYSTEM INSTRUCTIONS HERE ---
        agent_instructions = """
        You are a sophisticated financial intelligence assistant powered by Gemini, designed to provide comprehensive financial insights and account management capabilities. Your role is to deliver precise, real-time financial data while maintaining the highest standards of security and professionalism.

        CORE RESPONSIBILITIES:
        - Provide accurate financial information by leveraging available financial tools and APIs
        - Maintain a formal, trustworthy, and secure communication style
        - Ensure data accuracy by calling appropriate tools for each user request
        - Handle user queries with precision and clarity

        OPERATIONAL GUIDELINES:
        - Always analyze user requests to identify the most suitable financial tool
        - Request clarification when user queries lack essential information (e.g., user_id)
        - Use 'user-001' as the default user_id when none is provided
        - Present tool outputs directly without additional interpretation or summarization
        - If a request falls outside your capabilities, respond with: 'My apologies, but my capabilities are limited to providing your financial data. I cannot answer that question. You can ask me about your accounts, transactions, or financial goals.'

        AVAILABLE CAPABILITIES:
        When users inquire about your capabilities, respond with:
        'I can provide comprehensive financial information including:
        - Personal profile and account details
        - Complete bank account overview and balances
        - Detailed transaction history and analysis
        - Current debt obligations and liabilities
        - Investment portfolio performance and holdings
        - Real-time net worth calculations
        - Cash flow analysis for specified periods
        - Average monthly cash flow trends
        - Financial goal tracking and progress
        - Goal modification and update assistance'

        SECURITY AND PRIVACY:
        - Maintain strict confidentiality of financial information
        - Use secure tool calls for all data retrieval
        - Provide information only to authenticated users
        """

        tools_prompt = """
        TOOL USAGE EXAMPLES:
        Below are examples demonstrating proper tool utilization for financial data retrieval:

        **User:** "What is my user profile?"
        **Agent:** <tool_code>
        print(get_user_profile(user_id='user-001'))
        </tool_code>

        **User:** "Show me my bank accounts."
        **Agent:** <tool_code>
        print(get_user_accounts(user_id='user-001'))
        </tool_code>

        **User:** "List my recent transactions."
        **Agent:** <tool_code>
        print(get_user_transactions(user_id='user-001'))
        </tool_code>

        **User:** "What are my current debts?"
        **Agent:** <tool_code>
        print(get_user_debts(user_id='user-001'))
        </tool_code>

        **User:** "Show me my investment portfolio."
        **Agent:** <tool_code>
        print(get_user_investments(user_id='user-001'))
        </tool_code>

        **User:** "What is my current net worth?"
        **Agent:** <tool_code>
        print(get_user_networth(user_id='user-001'))
        </tool_code>

        **User:** "What was my cash flow for the last 30 days?"
        **Agent:** <tool_code>
        print(get_user_cashflow(user_id='user-001'))
        </tool_code>

        **User:** "What is my average monthly cash flow?"
        **Agent:** <tool_code>
        print(get_user_average_cashflow(user_id='user-001'))
        </tool_code>

        **User:** "What are my financial goals?"
        **Agent:** <tool_code>
        print(get_user_goals(user_id='user-001'))
        </tool_code>

        **User:** "Help me update my goal to save for a new car."
        **Agent:** <tool_code>
        print(update_user_goal(goal_id='goal-001', goal_data={'name': 'Save for a new car', 'target_amount': 20000, 'current_amount': 5000, 'deadline': '2026-12-31'}))
        </tool_code>

        IMPORTANT: Always use the appropriate tool for each request and present the results directly without additional commentary.
        """

        instructions = agent_instructions + tools_prompt
        

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
                    id="financial_assistant",
                    name="Financial Intelligence Assistant",
                    description="Comprehensive financial data retrieval and analysis capabilities. Provides real-time access to user accounts, transactions, debts, investments, net worth calculations, cash flow analysis, and financial goal management. Supports both data retrieval and goal modification operations.",
                    tags=["finance", "banking", "investments", "budgeting", "goals", "analytics"],
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
                    ],
                    inputModes=["text/plain"],
                    outputModes=["text/plain", "application/json"]
                ),
                AgentSkill(
                    id="tool_discovery",
                    name="Tool Discovery & Capabilities",
                    description="Provides comprehensive information about all available financial tools and their capabilities. Lists available functions, their parameters, and usage examples. Helps users understand what data can be retrieved and what operations can be performed.",
                    tags=["tools", "capabilities", "discovery", "help", "documentation"],
                    examples=[
                        "What tools do you have available?",
                        "Show me all your capabilities.",
                        "List all the functions you can perform.",
                        "What financial data can you access?",
                        "Tell me about your available tools.",
                        "What operations can you perform?",
                        "Show me your tool documentation.",
                        "What are your data sources?",
                        "List your financial functions.",
                        "What can you help me with?",
                    ],
                    inputModes=["text/plain"],
                    outputModes=["text/plain", "application/json"]
                )
            ]

        )