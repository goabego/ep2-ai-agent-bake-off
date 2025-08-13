
import os
import tools.financial_tools as ft
import tools.services_tools as st
from prompts import AGENT_INSTRUCTIONS

from google.adk.agents import LlmAgent
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from google.adk.tools import FunctionTool



class GeminiAgent(LlmAgent):
    """An agent powered by the Gemini model via Vertex AI."""

    # --- AGENT IDENTITY ---
    # These are the default values. The notebook can override them.
    name: str = "cymbal_bank_ai_agent"
    description: str = "A Cymbal Bank AI Agent powered by Gemini for Chatbot and Backend Services"

    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        # --- SET YOUR SYSTEM INSTRUCTIONS HERE ---
        instructions = """
            You are Finley, a professional financial advisor assistant. Provide concise, accurate financial guidance using available tools.

            **Core Principles:**
            - Be professional, clear, and concise
            - Use financial tools to provide accurate, personalized information
            - Present information in organized, easy-to-understand formats
            - Focus on actionable insights and professional recommendations
            - Default to user_id 'user-001' if none provided

            **Capabilities Overview:**
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
            - Use tools to gather current data
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
