# Mock Database Schema Documentation

This document outlines the structure and relationships of the JSON files used in the mock database.

## File Overview

-   **`user_personas.json`**: Contains the qualitative data about each user, including their financial background, goals, and risk tolerance. This file is the source of truth for the user archetypes.
-   **`users.json`**: The structured user data used by the application. It is derived from `user_personas.json` and includes a `user_id` to link to other files.
-   **`accounts.json`**: Contains a list of all financial accounts for all users. Each account is linked to a user via the `user_id`.
-   **`transactions.json`**: A log of all financial transactions. Each transaction is linked to a specific account via the `account_id`.

## Relationships

The files are linked in a hierarchical structure:

```
user_personas.json  ->  users.json  ->  accounts.json  ->  transactions.json
(1 to 1)            (1 to many)      (1 to many)
```

1.  **User Personas to Users**: Each user profile in `users.json` is based on a corresponding persona in `user_personas.json`. The `name` field can be used to map between these files.

2.  **Users to Accounts**: The `users.json` and `accounts.json` files are linked by the `user_id` field. Each user in `users.json` can have multiple accounts listed in `accounts.json`.

3.  **Accounts to Transactions**: The `accounts.json` and `transactions.json` files are linked by the `account_id` field. Each account in `accounts.json` can have multiple transactions associated with it in `transactions.json`.

This structure allows for a clear and organized representation of the mock financial data, ensuring that all transactions are tied to a specific account, which in turn is owned by a user with a defined persona.

## Key Value Criteria & Mock Data Instructions

### `users.json`

| Key               | Type   | Description                                                                 |
| ----------------- | ------ | --------------------------------------------------------------------------- |
| `user_id`         | String | Unique identifier for the user (e.g., "user-001").                          |
| `name`            | String | The user's full name.                                                       |
| `age`             | Number | The user's age in years.                                                    |
| `risk_tolerance`  | String | The user's tolerance for financial risk (e.g., "low-moderate").             |
| `profile_picture` | String | The filename of the user's profile picture.                                 |
| `credit_score`    | Number | The user's credit score.                                                    |
| `financial_blurb` | String | A brief description of the user's financial situation.                      |
| `goals`           | Array  | A list of the user's financial goals.                                       |

**Instructions:**

-   When creating a new user, ensure the `user_id` is unique.
-   The `financial_blurb` and `goals` should be directly informed by the corresponding user persona in `user_personas.json`.

### `accounts.json`

| Key             | Type   | Description                                                                 |
| --------------- | ------ | --------------------------------------------------------------------------- |
| `account_id`    | String | Unique identifier for the account (e.g., "acc-mw-c-001").                   |
| `user_id`       | String | The `user_id` of the account owner.                                         |
| `category`      | String | The category of the account (e.g., "asset", "liability").                   |
| `type`          | String | The type of account (e.g., "cash", "investment", "loan").                   |
| `sub_type`      | String | The sub-type of the account (e.g., "checking", "savings", "401k").          |
| `description`   | String | A brief description of the account.                                         |
| `balance`       | Number | The current balance of the account.                                         |
| `institution`   | String | The name of the financial institution.                                      |
| `interest_rate` | Number | The interest rate of the account (if applicable).                           |
| `holdings`      | Array  | A list of investment holdings within the account (if applicable).           |

**Instructions:**

-   Each `account_id` must be unique.
-   The number and types of accounts for each user should be consistent with their persona. For example, a recent graduate is unlikely to have a large investment portfolio, while a retiree may have multiple income-generating accounts.
-   The `balance` should be a realistic starting point for each account.

### `transactions.json`

| Key              | Type   | Description                                                                 |
| ---------------- | ------ | --------------------------------------------------------------------------- |
| `transaction_id` | String | Unique identifier for the transaction (e.g., "txn_id_001").                 |
| `account_id`     | String | The `account_id` to which the transaction belongs.                          |
| `date`           | String | The date and time of the transaction in ISO 8601 format.                    |
| `description`    | String | A brief description of the transaction.                                     |
| `amount`         | Number | The amount of the transaction. Positive for income, negative for expenses.  |
| `category`       | String | The category of the transaction (e.g., "Income", "Housing", "Debt").        |

**Instructions:**

-   Each `transaction_id` must be unique.
-   The `account_id` for each transaction must correspond to an existing account in `accounts.json`.
-   Transactions should be created in a way that reflects the user's persona and goals. For example, a user focused on paying off debt should have regular loan payments, while a retiree may have regular income from a pension or investments.
-   The `amount` and `category` of each transaction should be realistic and consistent with the `description`.
-   Include recurring transactions to simulate subscriptions and regular bills (e.g., streaming services, utilities).