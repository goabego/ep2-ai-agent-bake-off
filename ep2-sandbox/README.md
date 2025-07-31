# AI Financial Steward

The AI Financial Steward is a sophisticated financial assistant designed to provide users with a holistic view of their financial landscape. By integrating various financial accounts, life goals, and real-time market data, the Steward empowers users to make informed decisions and achieve their long-term aspirations.

This project is built on a modern, scalable architecture that leverages the power of AI to deliver personalized financial guidance. At its core is a council of specialized AI agents, each responsible for a different aspect of the user's financial well-being.

## Tech Stack

- **Backend:** Python 3.10+ with FastAPI
- **AI:** Google Agent Development Kit (ADK)
- **Database:** Mock JSON files

## Project Structure

The project is organized into the following directories:

- **`backend/`**: The main application code, including the FastAPI backend.
  - **`api/`**: Handles the backend API, with endpoints for managing users, accounts, and goals.
  - **`core/`**: Core application logic and configuration.
- **`db/`**: Mock JSON files that serve as the database.
- **`agent/`**: Contains the AI agent logic, including the main Steward and the specialized agent council.
- **`tests/`**: Unit and integration tests for the application.

## Getting Started

To get started with the AI Financial Steward, you'll need to have Python 3.10+ and Poetry installed.

1. **Install dependencies:**
   ```bash
   poetry install
   ```
2. **Run the application:**
   ```bash
   poetry run uvicorn backend.main:app --reload
   ```
This will start the FastAPI server, and you can access the interactive API documentation at `http://localhost:8000/docs`.

## API Endpoints

The backend API provides the following endpoints:

- `GET /user/{user_id}`: Retrieves a user's profile.
- `GET /user/{user_id}/accounts`: Fetches all accounts for a specific user.
- `POST /user/{user_id}/transactions`: Adds a new transaction for a user.
- `GET /goals/{user_id}`: Retrieves a user's financial goals.
- `PUT /goals/{goal_id}`: Updates a specific financial goal.
- `GET /events/next`: Fetches the next event for a midway challenge.

## Mock Data

The `db/` directory contains the following mock JSON files:

- **`users.json`**: User profile information.
- **`accounts.json`**: Financial accounts linked to users.
- **`transactions.json`**: A log of all financial transactions.
- **`life_goals.json`**: Users' major life goals.
- **`market_data.json`**: Simulated market data for challenges.
- **`events.json`**: Events to trigger midway challenges.

## Agent Council

The AI Financial Steward is powered by a council of specialized agents:

- **Personal Banker Agent**: Manages daily budgets, analyzes spending, and provides insights on debt management.
- **Wealth Planner Agent**: Manages long-term growth, models market scenarios, and aligns investments with life goals.
- **Tax Strategist Agent**: Analyzes the tax implications of all financial activities and identifies opportunities for tax savings.

These agents collaborate to provide users with comprehensive and proactive financial advice.
