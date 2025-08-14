
import os
from .tools import financial_tools as ft
from .tools import services_tools as st
from .prompts import AGENT_INSTRUCTIONS

from google.adk.agents import LlmAgent
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from google.adk.tools import FunctionTool

# Import specialized agents
from .agents.big_purchases import root_agent as big_purchases_agent
from .agents.daily_spending import root_agent as daily_spending_agent
from .agents.travel import root_agent as travel_agent



class Agent(LlmAgent):
    """An agent powered by the Gemini model via Vertex AI."""

    # --- AGENT IDENTITY ---
    # These are the default values. The notebook can override them.
    name: str = "cymbal_bank_ai_agent"
    description: str = "A Cymbal Bank AI Agent powered by Gemini for Chatbot and Backend Services"

    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        # --- SET YOUR SYSTEM INSTRUCTIONS HERE ---
        instructions = """
            You are Finley, a professional financial advisor assistant coordinating a team of specialized agents. 
            Provide concise, accurate financial guidance using available tools and delegate to specialists when appropriate.

            **Core Principles:**
            - Be professional, clear, and concise
            - Use financial tools to provide accurate, personalized information
            - Present information in organized, easy-to-understand formats
            - Focus on actionable insights and professional recommendations
            - Default to user_id 'user-001' if none provided

            **Specialized Sub-Agents:**
            You have access to these specialized agents for delegation:
            1. 'big_purchases_agent': Handles queries about large purchases (cars, appliances, home upgrades, tuition).
               Delegate when users ask about: buying cars, major appliances, financing big purchases, budgeting for large expenses.
            2. 'daily_spending_agent': Analyzes daily spending patterns and provides coaching.
               Delegate when users ask about: spending habits, daily expenses, budgeting tips, transaction analysis.
            3. 'travel_agent': Helps with travel planning and cost optimization.
               Delegate when users ask about: trip planning, travel budgets, vacation savings, travel cost optimization.

            **Delegation Strategy:**
            When you receive a user query, FIRST determine if it should be delegated to a specialist:
            
            - Travel-related requests (itinerary, vacation planning, trip budgets, travel savings): 
              Use the transfer_to_agent function to delegate to 'travel_agent'
            - Big purchase questions (cars, appliances, home upgrades, financing large expenses):
              Use the transfer_to_agent function to delegate to 'big_purchases_agent'  
            - Daily spending analysis or coaching (spending habits, budgeting tips, transaction categorization):
              Use the transfer_to_agent function to delegate to 'daily_spending_agent'
            - For account management, transactions, goals, or backend services: handle yourself using available tools
            
            IMPORTANT: If a query matches a specialist domain, you MUST use transfer_to_agent('agent_name') to delegate.
            Do NOT try to answer travel, big purchase, or daily spending coaching questions yourself.

            **Direct Capabilities:**
            I can assist with:
            • Get your user profile details
            • Get your recent transactions
            • Create a new financial goal
            • Delete a financial goal
            • Get a list of bank partners
            • Get a list of partners a specific user can benefit from
            • Create a new schedule

            **Response Style:**
            - Provide direct, professional answers
            - Use tools to gather current data when handling queries directly
            - Present information clearly and concisely
            - Offer brief, actionable insights when appropriate

            **Skill Selection:**
             - Use the "chat" skill for general financial advice and user interactions
             - Use the "serice_backend" skill when accessing backend API endpoints
    
            **When to use each skill:**
            - Chat skill: User questions, financial guidance, goal management
            - backend_services: API calls, data retrieval, system operations

            **When to use Json format:**
            - When the user asks for details about the tools or backend services or backend_services skill,
            - When the user asks for the data schemas,
            - When the user asks for the API endpoints,
        """

        instructions = instructions + ft.get_tool_prompt() + st.get_tool_prompt()

        # --- REGISTER YOUR TOOLS HERE ---
        tools = [
            ft.get_user_profile,
            ft.get_user_accounts,
            ft.get_user_transactions,
            ft.get_user_debts,
            ft.get_user_investments,
            ft.get_user_networth,
            ft.get_user_cashflow,
            ft.get_user_average_cashflow,
            ft.get_user_goals,
            ft.update_user_goal,
            ft.create_user_account,
            ft.get_user_transactions_with_history,
            ft.create_user_goal,
            ft.delete_user_goal,
            ft.get_bank_partners,
            ft.get_user_eligible_partners,
            ft.create_user_schedule,
            ft.get_user_schedules,
            ft.update_user_schedule,
            ft.delete_user_schedule,
            ft.get_all_advisors,
            ft.get_advisors_by_type,
            ft.schedule_meeting,
            ft.get_user_meetings,
            ft.cancel_meeting,
            st.get_all_endpoints,
            st.get_all_data_schemas,
        ]

        super().__init__(
            model=os.environ.get("MODEL", "gemini-2.5-flash"),
            instruction=instructions,
            tools=tools,
            sub_agents=[big_purchases_agent, daily_spending_agent, travel_agent],
            **kwargs,
        )


    def create_agent_card(self, agent_url: str) -> "AgentCard":
        return AgentCard(
            
            name=self.name,
            description=self.description,
            url=agent_url,
            version="1.0.0",
            defaultInputModes=["application/json", "text/plain"],
            defaultOutputModes=["application/json", "text/plain"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[
                AgentSkill(
                    id="chat",
                    name="Cymbal Bank AI Agent",
                    description="Cymbal Bank AI Agent is a helpful assistant powered by Gemini.",
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
                    id="backend_services",
                    name="Cymbal Bank Backend Services",
                    description="This skill is used to interact with the Cymbal Bank backend services.",
                    tags=["fast_api","backend_services","backend"],
                    defaultOutputModes=["application/json"],
                    examples=[
                        "What are the available endpoints?",
                        "What are the data schemas?",
                    ]
                )
            ]

        )

root_agent = Agent()
