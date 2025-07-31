# AI Agent Bake Off: Tech Stack & Environment

This document outlines the technical environment, stack, and mock data for the AI Agent Bake Off challenge. The goal is to provide a clear and well-documented foundation for teams to build their "AI Financial Steward."

## 1. Core Tech Stack

The environment is designed to be simple, robust, and easy to set up, allowing teams to focus on building their AI agent's logic and user experience.

*   **Backend Language:** **Python 3.10+**
    *   **Why:** Python's simplicity, extensive data science libraries, and strong support for AI/ML make it the ideal choice.
*   **Backend Framework:** **FastAPI**
    *   **Why:** FastAPI is a modern, high-performance web framework for building APIs. It offers automatic, interactive API documentation (via Swagger UI and ReDoc), data validation with Pydantic, and an intuitive structure. This allows teams to quickly create and test a robust backend to support their agent.
*   **AI Agent Framework:** **Google Agent Development Kit (ADK)**
    *   **Why:** The ADK provides the core building blocks for creating powerful, multi-agent systems with Gemini. It simplifies the process of defining agent roles, managing state, and orchestrating complex workflows.
*   **Database:** **JSON Files (Mock Database)**
    *   **Why:** To keep the focus on agent development rather than database management, we will use a set of local JSON files as our data store. The FastAPI backend will be responsible for reading from and writing to these files, simulating a real database.

## 2. Environment Setup

Participants should follow these steps to prepare their local development environment using **Poetry**.

1.  **Install Poetry:** If you don't have Poetry, install it by following the official instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

2.  **Initialize Project:** In your project directory, initialize a new Poetry project.

    ```bash
    poetry init --name "ai-financial-steward" --python "^3.10"
    ```
    This will create a `pyproject.toml` file.

3.  **Add Dependencies:** Add the necessary libraries to your project. Poetry will handle creating a virtual environment automatically.

    ```bash
    poetry add fastapi "uvicorn[standard]" pydantic google-generativeai google-cloud-aiplatform
    # ADK will be provided or installed via specific instructions
    ```

4.  **Activate Virtual Environment:** To work within the project's virtual environment, run:

    ```bash
    poetry shell
    ```

## 3. Proposed Code Structure

To keep the project organized, we recommend the following directory structure.

```
ai-financial-steward/
│
├── pyproject.toml      # Poetry configuration and dependencies
├── poetry.lock         # Poetry lock file
│
├── app/                # Main application source code
│   ├── __init__.py
│   ├── main.py         # FastAPI application entry point
│   │
│   ├── api/            # FastAPI backend logic
│   │   ├── __init__.py
│   │   ├── endpoints/  # API endpoint routers
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   ├── accounts.py
│   │   │   └── goals.py
│   │   └── models.py   # Pydantic models for request/response
│   │
│   ├── agent/          # ADK Agent logic
│   │   ├── __init__.py
│   │   ├── steward.py  # Main Financial Steward agent
│   │   ├── council/    # The multi-agent council
│   │   │   ├── __init__.py
│   │   │   ├── banker.py
│   │   │   ├── wealth_planner.py
│   │   │   └── tax_strategist.py
│   │   └── tools/      # Tools for agents to interact with the API
│   │       ├── __init__.py
│   ���       └── financial_tools.py
│   │
│   └── core/           # Core application logic/config
│       ├── __init__.py
│       └── config.py   # Configuration settings
│
├── data/               # Mock database JSON files
│   ├── users.json
│   ├── accounts.json
│   ├── transactions.json
│   ├── life_goals.json
│   ├── market_data.json
│   └── events.json
│
└── tests/              # Tests for the application
    ├── __init__.py
    ├── test_api.py
    └── test_agent.py
```

## 4. Mock Database Schema (JSON Files)

The following JSON files will serve as the mock database. The backend API will provide endpoints to interact with this data.

### a. `users.json`

Stores the profile information for the user.

*   **Structure:**
    ```json
    [
      {
        "user_id": "user-123",
        "name": "Alex Johnson",
        "age": 35,
        "risk_tolerance": "moderate",
        "life_goals": [
          "goal-001",
          "goal-002",
          "goal-003"
        ]
      }
    ]
    ```

### b. `accounts.json`

Stores all financial accounts linked to a user.

*   **Structure:**
    ```json
    [
      {
        "account_id": "acc-chk-001",
        "user_id": "user-123",
        "type": "checking",
        "balance": 5400.75,
        "institution": "Fidelity"
      },
      {
        "account_id": "acc-inv-002",
        "user_id": "user-123",
        "type": "investment",
        "balance": 150000.00,
        "holdings": [
          {"symbol": "VOO", "value": 100000.00},
          {"symbol": "QQQ", "value": 50000.00}
        ]
      },
      {
        "account_id": "acc-dbt-003",
        "user_id": "user-123",
        "type": "debt",
        "balance": -25000.00,
        "asset": "Car Loan",
        "interest_rate": 0.045
      }
    ]
    ```

### c. `transactions.json`

A log of all financial transactions.

*   **Structure:**
    ```json
    [
      {
        "transaction_id": "txn-001",
        "account_id": "acc-chk-001",
        "date": "2025-07-20T10:00:00Z",
        "description": "Paycheck",
        "amount": 2500.00,
        "category": "Income"
      },
      {
        "transaction_id": "txn-002",
        "account_id": "acc-chk-001",
        "date": "2025-07-21T12:30:00Z",
        "description": "Coffee Shop",
        "amount": -5.50,
        "category": "Discretionary"
      }
    ]
    ```

### d. `life_goals.json`

Defines the user's major life goals.

*   **Structure:**
    ```json
    [
      {
        "goal_id": "goal-001",
        "user_id": "user-123",
        "description": "Buy a house",
        "target_amount": 750000.00,
        "target_date": "2030-01-01",
        "current_amount_saved": 120000.00
      },
      {
        "goal_id": "goal-002",
        "user_id": "user-123",
        "description": "Retire",
        "target_amount": 2000000.00,
        "target_date": "2055-01-01",
        "current_amount_saved": 150000.00
      }
    ]
    ```

### e. `market_data.json`

Simulated market data for the "Market Tremor" challenge.

*   **Structure:**
    ```json
    {
      "timestamp": "2025-07-25T14:00:00Z",
      "indices": {
        "S&P_500": {"change_percent": -15.0},
        "NASDAQ": {"change_percent": -18.5}
      },
      "news_headline": "Stock market enters correction territory amidst inflation fears."
    }
    ```

### f. `events.json`

For triggering the midway challenges.

*   **Structure:**
    ```json
    [
        {
            "event_id": "event-bonus-001",
            "type": "windfall",
            "description": "Received a one-time work bonus.",
            "amount": 25000.00,
            "triggered": false
        },
        {
            "event_id": "event-market-002",
            "type": "market_downturn",
            "description": "Market correction: indices down 15%.",
            "triggered": false
        }
    ]
    ```

## 4. Backend API (FastAPI)

The FastAPI server will expose endpoints to manage the mock data. This creates a clear separation between the data and the agent logic.

**Example Endpoints:**

*   `GET /user/{user_id}`: Get user profile.
*   `GET /user/{user_id}/accounts`: Get all accounts for a user.
*   `POST /user/{user_id}/transactions`: Add a new transaction.
*   `GET /goals/{user_id}`: Get user's financial goals.
*   `PUT /goals/{goal_id}`: Update a financial goal.
*   `GET /events/next`: Get the next event for a midway challenge.

## 5. Role of Gemini: Core Logic and Creative Content

While the primary use of Gemini in this challenge is for its powerful reasoning and text generation capabilities, there is significant opportunity to creatively use its multimodal features to generate other content, making the "AI Financial Steward" more engaging and visually appealing.

*   **Essential (Text Generation):**
    *   **Conversational AI:** Understanding user queries in natural language.
    *   **Analysis & Summarization:** Processing financial data from the API to generate the "Living Briefing" and "Directive."
    *   **Proactive Alerts:** Crafting the text for proactive notifications (e.g., "The Silent Drift" challenge).
    *   **Multi-Agent Collaboration:** Generating dialogue and synthesized recommendations from the AI Council.

*   **Optional (Creative Content Generation):**
    *   **Image Generation:** Teams can use Gemini to generate images to enhance the user experience. For example:
        *   Creating a personalized avatar for the user's profile.
        *   Generating icons or illustrative images for life goals (e.g., a picture of a dream house, a new car, a travel destination).
        *   Creating charts or infographics that are more visually rich than standard library outputs.
    *   **Video Generation (Stretch Goal):** For teams looking to push the boundaries, Gemini could be used to create short, personalized video summaries of financial progress, though this is not a core requirement.

The core task is to build a functional financial agent, but the creative use of generated content could be a key differentiator during judging, especially in fulfilling the "make it visually appealing for TV" aspect of the brief.

## 6. Recommended MCP Servers for the Sandbox Environment

To build a scalable and production-ready solution, we recommend leveraging the following Managed Cloud Platform (MCP) servers and services.

*   ### **Cloud Run MCP Server**
    *   **What it is:** A fully managed, serverless platform for deploying and scaling containerized applications. Cloud Run will serve as the core for the backend.
    *   **Why it's useful:** Instead of running the FastAPI server locally, teams can containerize their application and deploy it to Cloud Run. This provides a public HTTPS endpoint, automatic scaling, and integrated logging, making it perfect for hosting the agent's backend API.
    *   **Integrated Services:**
        *   **Secret Manager:** For securely storing the Gemini API key instead of using `.env` files.
        *   **Cloud Logging & Monitoring:** For centralized logging and performance monitoring of the deployed application.

*   ### **Firebase MCP Server**
    *   **What it is:** A comprehensive application development platform that includes a suite of tools for building and managing apps.
    *   **Why it's useful:** Firebase provides the data persistence layer for the application, replacing the local JSON files with a scalable, cloud-native solution.
    *   **Integrated Services:**
        *   **Firestore:** A flexible, scalable NoSQL document database that is the ideal replacement for the mock JSON files. The data structures map directly to Firestore's document-collection model, and it offers real-time data synchronization.
        *   **Cloud Storage for Firebase:** The perfect place to store any generated image assets (e.g., user avatars, goal icons) from Gemini.

*   ### **Core AI Service: Vertex AI**
    *   **What it is:** Google's unified AI platform.
    *   **Why it's useful:** This is the recommended way to interact with the Gemini API for the challenge. It provides access to the latest models, robust SDKs, and tools for monitoring and management, ensuring a production-oriented approach.

## 7. ADK Agent Integration

The ADK agent will be the "brain" of the operation.

*   **Interaction:** The agent will not access the JSON files directly. Instead, it will use **tools** that make HTTP requests to the FastAPI backend.
*   **Example Workflow:**
    1.  A user asks the agent, "How close am I to buying a house?"
    2.  The agent uses its `get_financial_goals` tool, which calls the `GET /goals/{user_id}` endpoint.
    3.  The FastAPI server reads `life_goals.json` and returns the relevant data.
    4.  The agent receives the data and formulates a response for the user.
*   **Multi-Agent Council:** The ADK will be used to define the `Personal Banker`, `Wealth Planner`, and `Tax Strategist` agents. Each agent will have its own set of tools to interact with the backend, allowing them to collaborate on complex queries.
