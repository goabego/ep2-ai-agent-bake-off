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

- `GET /api/users/{user_id}`: Retrieves a user's profile.
- `GET /api/users/{user_id}/accounts`: Fetches all accounts for a specific user.
- `GET /api/users/{user_id}/transactions`: Retrieves all transactions for a user.
- `GET /api/users/{user_id}/debts`: Retrieves all debt accounts for a user.
- `GET /api/users/{user_id}/investments`: Retrieves all investment accounts for a user.
- `GET /api/users/{user_id}/networth`: Calculates the net worth of a user.
- `GET /api/users/{user_id}/cashflow`: Calculates the cash flow for a user over the last 30 days.
- `GET /api/users/{user_id}/average_cashflow`: Calculates the average monthly cash flow for a user over the last 3 months.
- `GET /api/goals/{user_id}`: Retrieves a user's financial goals.
- `PUT /api/goals/{goal_id}`: Updates a specific financial goal.

## Mock Data

The `db/` directory contains the following mock JSON files:

- **`users.json`**: User profile information.
- **`accounts.json`**: Financial accounts linked to users. Each account has a `category` (`asset` or `liability`), `type` (e.g., `cash`, `investment`, `loan`), and `sub_type` (e.g., `checking`, `brokerage`, `student_loan`).
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
