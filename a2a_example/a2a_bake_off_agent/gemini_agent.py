import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.tools.example_tool import ExampleTool
from google.genai import types
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from dotenv import load_dotenv


load_dotenv("../.env")

AGENT_URL = os.environ.get("AGENT_URL", "http://127.0.0.1:8000")
AGENT_URL = "http://127.0.0.1:8000"

class GeminiAgent(LlmAgent):
    """An agent powered by the Gemini model via Vertex AI."""

    # --- AGENT IDENTITY ---
    # These are the default values. The notebook can override them.
    name: str = "gemini_agent"
    description: str = "A helpful assistant powered by Gemini."

    
    def __init__(self, **kwargs):
        print("Initializing GeminiAgent...")
        financial_agent = RemoteA2aAgent(
            name="financial_agent",
            description="Agent that has access to financial data",
            agent_card=(
                f"https://a2a-ep2-33wwy4ha3a-uw.a.run.app/.well-known/agent-card.json"
            ),
        )

        super().__init__(
            model="gemini-2.5-flash",
            instruction="""
              You are a helpful assistant that helps users with their requets.
              If there are questinos of financial nature, you can work with the financial_agent who can answer questions of financial topics.
            """,
            global_instruction=(
                "You are assistant Bot, an assistant agent."
            ),
            sub_agents=[financial_agent],
            tools=[],
            generate_content_config=types.GenerateContentConfig(
                safety_settings=[
                    types.SafetySetting(  # avoid false alarm about rolling dice.
                        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                        threshold=types.HarmBlockThreshold.OFF,
                    ),
                ]
            ),
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
