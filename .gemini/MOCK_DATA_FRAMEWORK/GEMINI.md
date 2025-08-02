# Framework and Criteria for Generating Mock Data

This document outlines the requirements for creating realistic mock datasets for the `transactions.json` and `bank_partners.json` files.

## I. Data Schemas

### a. `transactions.json`

The following is the schema for a single transaction object in the `transactions.json` array.

```json
{
  "transaction_id": "string",
  "account_id": "string",
  "merchant_id": "string",
  "date": "string",
  "description": "string",
  "amount": "number",
  "category": "string"
}
```

### b. `bank_partners.json`

The following is the schema for a single partner object in the `bank_partners.json` array.

```json
{
  "partner_id": "string",
  "merchant_id": "string",
  "name": "string",
  "category": "string",
  "benefit_type": "string",
  "benefit_value": "number",
  "eligibility_criteria": {
    "minimum_credit_score": "number"
  }
}
```

## II. Field Constraints and Criteria

### `transactions.json`

#### 1. `transaction_id`

*   **Type:** `string`
*   **Constraints:**
    *   Must be a unique identifier for each transaction.
    *   Should follow the format `txn_id_` followed by a zero-padded 3-digit number (e.g., `txn_id_001`).
*   **Criteria:**
    *   The numeric part of the ID should be sequential and continuous.

#### 2. `account_id`

*   **Type:** `string`
*   **Constraints:**
    *   Must correspond to an existing `account_id` in the `accounts.json` file.
*   **Criteria:**
    *   Transactions should be logically associated with the correct user and account type.

#### 3. `merchant_id`

*   **Type:** `string`
*   **Constraints:**
    *   Should correspond to a `merchant_id` in the `bank_partners.json` file for partner transactions.
*   **Criteria:**
    *   Use a specific `merchant_id` (e.g., `merch_101`) for transactions that should be associated with a partner.
    *   Use a generic identifier (e.g., `merch_999`) for non-partner transactions.

#### 4. `date`

*   **Type:** `string`
*   **Constraints:**
    *   Must be in ISO 8601 format (e.g., `YYYY-MM-DDTHH:MM:SSZ`).
*   **Criteria:**
    *   The dataset should span a 12-month period, from August 2024 to July 2025.
    *   Transactions should be distributed realistically throughout each month.

#### 5. `description`

*   **Type:** `string`
*   **Constraints:**
    *   Should be a human-readable description of the transaction.
*   **Criteria:**
    *   Descriptions should be varied and reflect the transaction's category.

#### 6. `amount`

*   **Type:** `number`
*   **Constraints:**
    *   Positive values represent income.
    *   Negative values represent expenses.
*   **Criteria:**
    *   The amount should be realistic for the transaction's category and the user's persona.

#### 7. `category`

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

### `bank_partners.json`

#### 1. `partner_id`

*   **Type:** `string`
*   **Constraints:**
    *   Unique identifier for the partner (e.g., `partner_001`).

#### 2. `merchant_id`

*   **Type:** `string`
*   **Constraints:**
    *   Unique identifier for the merchant (e.g., `merch_101`). This ID links the partner to transactions.

#### 3. `name`

*   **Type:** `string`
*   **Criteria:**
    *   Human-readable name of the partner company.

#### 4. `category`

*   **Type:** `string`
*   **Constraints:**
    *   Must be one of the following: "Dining", "Subscriptions", "Lender", "Automotive", "Home Purchases".

#### 5. `benefit_type`

*   **Type:** `string`
*   **Constraints:**
    *   Must be "percentage_discount" or "apr_reduction".

#### 6. `benefit_value`

*   **Type:** `number`
*   **Criteria:**
    *   For `percentage_discount`, this is a float (e.g., `0.10` for 10%).
    *   For `apr_reduction`, this is a float (e.g., `0.0025` for 0.25%).

#### 7. `eligibility_criteria`

*   **Type:** `object`
*   **Criteria:**
    *   For transactional partners, this should be `null`.
    *   For "Lender" partners, this must contain a `minimum_credit_score` key with an integer value.
