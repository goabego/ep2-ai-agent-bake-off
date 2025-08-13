# AI Financial Steward

This project is an AI-powered financial assistant designed to help users manage their finances, plan for the future, and achieve their financial goals. By integrating various financial accounts, life goals, and real-time market data, the Steward empowers users to make informed decisions and achieve their long-term aspirations.

This project is built on a modern, scalable architecture that leverages the power of AI to deliver personalized financial guidance. At its core is a council of specialized AI agents, each responsible for a different aspect of the user's financial well-being.

# Overview

**What you’re building**  
As a reminder, your core task is to: 

1) Build agents that help to reimagine the retail banking experience using ADK and Gemini (or imagen, veo, etc)  
2) Establishing connectivity to a pre-built retail bank agent (Cymbal Bank) that has access to the financial information of consumers your agents are trying to help with using A2A.    
3) In addition, to build a delightful consumer experience that would wow the consumers of today, you’re encouraged  to show the development process of designing the agents  that benefit from communicating to the Cymbal Banks Agent. 

**Focal points for hackathon**

* P1: At least two subagents that tackle financial use cases (we suggested three but feel free to consider your own)  
  * Suggested: Big Purchase planning agent, Travel Budget Agent, Subscriptions Audit Agent  
* P2: Showcase how these agents you’ve built communicate to the Cymbal Banks Agent via A2A    
* P3: Automation: Each sub-agent requires a form of automation. Automate at least one thing from a consumer experience and one from the bank’s operation perspective.


**Endpoint URLs**  
To help you focus on building, we've prepared useful assets that you can use during the bake-off:

| Endpoint Type | Notes | Pretty URL |
| :---- | :---- | :---- |
| Cymbal Bank Frontend | This is to help give you a sense of challenge. You’re not expected to build on top of this frontend.  | [https://frontend.ai-agent-bakeoff.com/](https://frontend.ai-agent-bakeoff.com/) |
| Cymbal Bank Frontend Dashboard | Same as above | [https://frontend.ai-agent-bakeoff.com/dashboard?userId=user-001](https://frontend.ai-agent-bakeoff.com/dashboard?userId=user-001) |
| Cymbal Bank Agent | Agent endpoint that you will communicate via A2A | [https://agent.ai-agent-bakeoff.com/](https://agent.ai-agent-bakeoff.com/) |
| Cymbal Bank Agent Card | Agent Card details. You need to establish protocol with your agents using A2A \- [docs here](https://a2a-protocol.org/latest/topics/agent-discovery/) | [https://agent.ai-agent-bakeoff.com/.well-known/agent-card.json](https://agent.ai-agent-bakeoff.com/.well-known/agent-card.json) |
| Cymbal Bank Backend Fast API | Fast API Backend with built in components, database, etc. Implementation Note: To accurately simulate a real-world environment, please ensure all communication protocol is directed through the agent interface. Direct calls to the backend APIs are prohibited in the final product, as this would bypass the intended security model where each agent's data is treated as a protected and separate entity. Direct API access is provided exclusively for troubleshooting and debugging purposes.  | [https://backend.ai-agent-bakeoff.com/](https://backend.ai-agent-bakeoff.com//docs) |
| A2A Inspector GUI | Useful A2A inspector GUI for communication and initializing Agent via A2A (can be used with your Agent and Cymbal Bank’s Agent). | [https://github.com/goabego/ep2-ai-agent-bake-off/tree/main/a2a\_example/a2a\_ui\_tool](https://github.com/goabego/ep2-ai-agent-bake-off/tree/main/a2a_example/a2a_ui_tool) |
| A2A Examples | We added example code for quicker development. Mock Cymbal Bank Agent, Your Agent, and Inspector GUI. | [https://github.com/goabego/ep2-ai-agent-bake-off/tree/main/a2a\_example](https://github.com/goabego/ep2-ai-agent-bake-off/tree/main/a2a_example) |


## Tech Stack

-   **Backend:** Python 3.10+ with FastAPI and Poetry
-   **Frontend:** React with Vite, TypeScript, and Tailwind CSS
-   **AI:** Google Agent Development Kit (ADK)
-   **Database:** Mock JSON files

## Getting Started

To get started with the AI Financial Steward, you'll need to have Python 3.10+, Poetry, and Node.js (which includes npm) installed.

### Backend Setup

1.  **Navigate to the `ep2-sandbox` directory:**
    ```bash
    cd ep2-sandbox
    ```
2.  **Install backend dependencies:**
    ```bash
    poetry install
    ```

### Frontend Setup

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd ep2-sandbox/frontend
    ```
2.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

## Running the Application

### Backend

1.  **Navigate to the `ep2-sandbox` directory:**
    ```bash
    cd ep2-sandbox
    ```
2.  **Run the backend server:**
    ```bash
    poetry run uvicorn backend.main:app --reload
    ```
    The FastAPI server will start, and you can access the interactive API documentation at `http://localhost:8000/docs`.

### Frontend

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd ep2-sandbox/frontend
    ```
2.  **Run the frontend development server:**
    ```bash
    npm run dev
    ```
    The frontend application will be available at `http://localhost:5173` (or another port if 5173 is in use).

## Running Tests

1.  **Navigate to the `ep2-sandbox` directory:**
    ```bash
    cd ep2-sandbox
    ```
2.  **Run the tests:**
    ```bash
    poetry run pytest
    ```

## Project Structure

This repository is organized into the following directories:

### `/.gemini`

This directory contains project-specific settings and context for the Gemini AI, including development standards and use case details.

### `/ep2-sandbox`

This is the main application directory, containing the source code for the AI Financial Steward.

-   **`agent/`**: Contains the core logic for the AI agents, including the main `FinancialStewardAgent` and its council of specialized agents (`PersonalBankerAgent`, `WealthPlannerAgent`, `TaxStrategistAgent`).
-   **`backend/`**: The FastAPI application that serves the financial data via a REST API. It includes API endpoints and data models.
-   **`frontend/`**: A React application built with Vite and styled with Tailwind CSS and Shadcn/UI. It provides the user interface for the mock bank.
-   **`db/`**: Holds the mock JSON data files that act as the application's database.
-   **`images/`**: Contains the profile pictures for the mock users.
-   **`tests/`**: Includes tests for the API and agent functionalities.

### `user_personas.json`

This file contains a set of mock user personas. Each persona includes a name, age, financial situation, and specific goals, providing realistic scenarios for testing and demonstration of the AI Financial Steward.

## API Endpoints

The backend API provides the following endpoints:

-   `GET /user/{user_id}`: Retrieves a user's profile.
-   `GET /user/{user_id}/accounts`: Fetches all accounts for a specific user.
-   `POST /user/{user_id}/transactions`: Adds a new transaction for a user.
-   `GET /goals/{user_id}`: Retrieves a user's financial goals.
-   `PUT /goals/{goal_id}`: Updates a specific financial goal.
-   `GET /events/next`: Fetches the next event for a midway challenge.

## Agent Council

The AI Financial Steward is powered by a council of specialized agents:

-   **Personal Banker Agent**: Manages daily budgets, analyzes spending, and provides insights on debt management.
-   **Wealth Planner Agent**: Manages long-term growth, models market scenarios, and aligns investments with life goals.
-   **Tax Strategist Agent**: Analyzes the tax implications of all financial activities and identifies opportunities for tax savings.

These agents collaborate to provide users with comprehensive and proactive financial advice.