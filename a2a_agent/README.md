# Financial Agent

This document provides an overview of the financial agent and its capabilities. The agent is designed to help users manage their personal finances by providing access to their financial data and helping them set and track their financial goals.

## Agent Capabilities

The financial agent can perform the following tasks:

*   **Get User Profile:** Retrieve a user's profile information, including their name, age, address, credit score, net worth, and risk tolerance.
*   **Get User Accounts:** Fetch all of a user's financial accounts, including checking, savings, 401k, student loans, and credit cards.
*   **Get User Transactions:** Retrieve a list of a user's recent transactions.
*   **Get User Debts:** Get a summary of a user's current debts, including student loans and credit card balances.
*   **Get User Investments:** Retrieve a user's investment portfolio, including their 401k and other investment accounts.
*   **Get User Net Worth:** Calculate a user's current net worth.
*   **Get User Cash Flow:** Calculate a user's cash flow for the last 30 days.
*   **Get User Average Cash Flow:** Calculate a user's average monthly cash flow over the last 3 months.
*   **Get User Goals:** Retrieve a user's financial goals.
*   **Update User Goal:** Update a user's financial goal, such as saving for a new car or paying off a debt.

## Interacting with the Agent

The financial agent can be accessed through a backend API. To interact with the agent, you will need to send requests to the API with the desired tool and any necessary parameters. The agent will then process the request and return a response with the requested information.

For example, to get a user's profile, you would send a request to the API with the `get_user_profile` tool and the user's ID. The agent would then return a response with the user's profile information.

## End-to-End Story

This end-to-end story demonstrates how a user might interact with the financial agent to manage their finances.

1.  **The user asks the agent for their user profile.** The agent retrieves the user's profile information and displays it to the user.
2.  **The user asks the agent for their bank accounts.** The agent fetches the user's bank accounts and displays them to the user.
3.  **The user asks the agent for their recent transactions.** The agent retrieves the user's recent transactions and displays them to the user.
4.  **The user asks the agent for their current debts.** The agent gets a summary of the user's current debts and displays it to the user.
5.  **The user asks the agent for their investment portfolio.** The agent retrieves the user's investment portfolio and displays it to the user.
6.  **The user asks the agent for their current net worth.** The agent calculates the user's current net worth and displays it to the user.
7.  **The user asks the agent for their cash flow for the last 30 days.** The agent calculates the user's cash flow for the last 30 days and displays it to the user.
8.  **The user asks the agent for their average monthly cash flow.** The agent calculates the user's average monthly cash flow over the last 3 months and displays it to the user.
9.  **The user asks the agent for their financial goals.** The agent retrieves the user's financial goals and displays them to the user. In this case, the user does not have any financial goals, so the agent asks the user if they would like to add some.
10. **The user asks the agent to help them update their goal to save for a new car.** The agent asks the user for more information about their goal, such as the target amount and deadline.
