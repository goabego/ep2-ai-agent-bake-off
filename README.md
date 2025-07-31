# AI Financial Steward

This project is an AI-powered financial assistant designed to help users manage their finances, plan for the future, and achieve their financial goals.

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