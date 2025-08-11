import os
import asyncio
from dotenv import load_dotenv
from a2a.server.apps.jsonrpc.starlette_app import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from gemini_agent import GeminiAgent
from agent_executor import AdkAgentToA2AExecutor
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

load_dotenv()

# The URL of your deployed Cloud Function.
# It's best to set this as an environment variable in your deployment.
# For example: "https://us-central1-my-project.cloudfunctions.net/my-function-name"
#AGENT_URL = "https://a2aagenttest-906194901769.us-central1.run.app"
AGENT_URL = os.environ.get("AGENT_URL", "http://127.0.0.1:8000")

# 1. Create the AgentCard, RequestHandler, and App at the global scope.
#    This is more efficient as it's done only once when the function instance starts.
agent = GeminiAgent()
agent_card = agent.create_agent_card(AGENT_URL)

request_handler = DefaultRequestHandler(
    agent_executor=AdkAgentToA2AExecutor(),
    task_store=InMemoryTaskStore(),
)

# 2. The Functions Framework will automatically look for this 'app' variable.
# Use the middleware parameter for proper exception handling as recommended by Starlette docs
base_app = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler,
)

# Build the base app
app = base_app.build()

# Apply CORS middleware to the entire application for global enforcement
# This ensures CORS headers are applied even to error responses
app = CORSMiddleware(
    app=app,
    allow_origins=[
        "https://frontend-ep2-426194555180.us-west1.run.app",  # Production frontend
        "https://frontend-ep2-879168005744.us-west1.run.app",
        "http://localhost:8080",  # Development frontend
        "http://localhost:3000",  # Alternative development port
        "http://127.0.0.1:8080",  # Alternative localhost
        "http://127.0.0.1:3000",  # Alternative localhost
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Explicit methods
    allow_headers=["*"],  # Allows all headers
    expose_headers=["*"],  # Expose all headers in response
    max_age=600,  # Cache CORS preflight for 10 minutes
)
