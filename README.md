# AI Financial Steward

This project is an AI-powered financial assistant designed to help users manage their finances, plan for the future, and achieve their financial goals. By integrating various financial accounts, life goals, and real-time market data, the Steward empowers users to make informed decisions and achieve their long-term aspirations.

This project is built on a modern, scalable architecture that leverages the power of AI to deliver personalized financial guidance. At its core is a council of specialized AI agents, each responsible for a different aspect of the user's financial well-being.

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