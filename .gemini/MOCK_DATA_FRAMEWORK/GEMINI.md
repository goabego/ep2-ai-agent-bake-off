# Framework and Criteria for Generating Mock Transaction Data

This document outlines the requirements for creating a realistic 12-month mock dataset for the `transactions.json` file.

## I. Data Schema

The following is the schema for a single transaction object in the `transactions.json` array.

```json
{
  "transaction_id": "string",
  "account_id": "string",
  "date": "string",
  "description": "string",
  "amount": "number",
  "category": "string"
}
```

## II. Field Constraints and Criteria

### 1. `transaction_id`

*   **Type:** `string`
*   **Constraints:**
    *   Must be a unique identifier for each transaction.
    *   Should follow the format `txn_id_` followed by a zero-padded 3-digit number (e.g., `txn_id_001`).
*   **Criteria:**
    *   The numeric part of the ID should be sequential and continuous.

### 2. `account_id`

*   **Type:** `string`
*   **Constraints:**
    *   Must correspond to an existing `account_id` in the `accounts.json` file.
*   **Criteria:**
    *   Transactions should be logically associated with the correct user and account type. For example, a "Paycheck" transaction should be associated with a checking account, not a mortgage account.

### 3. `date`

*   **Type:** `string`
*   **Constraints:**
    *   Must be in ISO 8601 format (e.g., `YYYY-MM-DDTHH:MM:SSZ`).
*   **Criteria:**
    *   The dataset should span a 12-month period, from August 2024 to July 2025.
    *   Transactions should be distributed realistically throughout each month.

### 4. `description`

*   **Type:** `string`
*   **Constraints:**
    *   Should be a human-readable description of the transaction.
*   **Criteria:**
    *   Descriptions should be varied and reflect the transaction's category. For example, a "Dining" transaction could have descriptions like "Lunch - ACME Salads" or "Dinner - The Cymbal Room".

### 5. `amount`

*   **Type:** `number`
*   **Constraints:**
    *   Positive values represent income.
    *   Negative values represent expenses.
*   **Criteria:**
    *   The amount should be realistic for the transaction's category and the user's persona. For example, a "Paycheck" for a high-income user should be larger than for a low-income user.

### 6. `category`

*   **Type:** `string`
*   **Constraints:**
    *   Must be one of the following predefined categories:
        *   Income
        *   Housing
        *   Debt
        *   Transfers
        *   Groceries
        *   Dining
        *   Transportation
        *   Shopping
        *   Utilities
        *   Kids
        *   Entertainment
        *   Taxes
        *   Charity
        *   Health & Wellness
        *   Fees
        *   Pets
        *   Services
        *   Gifts & Donations
        *   Travel
*   **Criteria:**
    *   The category should accurately reflect the nature of the transaction.
