# HashiCorp Vault Management

This repository provides a set of Python functions to manage HashiCorp Vault instances using the HashiCorp Cloud Platform (HCP) API. The provided functions allow for creating vault applications, creating and retrieving secrets, and deleting vault applications and secrets.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- HashiCorp Cloud Platform account with necessary API credentials

## Environment Variables

Ensure the following environment variables are set before running the scripts:

- `ORGANIZATION_ID`
- `PROJECT_ID`
- `HCP_CLIENT_ID`
- `HCP_CLIENT_SECRET`

You can set these environment variables in your operating system or in a `.env` file.

## Functions

### 1. `get_hcp_token()`

Fetches an HCP API token using client credentials.

### 2. `app_vault_creation(key_valut_name)`

Creates a new app vault in HCP.

**Parameters:**
- `key_valut_name` (str): The name of the key vault to be created.

**Returns:**
- Success or error message.

### 3. `secret_creation(key_valut_name, secret_name, secret_value)`

Creates a new secret in the specified app vault.

**Parameters:**
- `key_valut_name` (str): The name of the key vault.
- `secret_name` (str): The name of the secret.
- `secret_value` (str): The value of the secret.

**Returns:**
- Success or error message.

### 4. `get_secret_value(key_vault_name, secret_name)`

Retrieves the value of a specified secret.

**Parameters:**
- `key_vault_name` (str): The name of the key vault.
- `secret_name` (str): The name of the secret.

**Returns:**
- The value of the secret.

### 5. `delete_keyvalut_app(key_vault_name)`

Deletes a specified key vault and all its secrets.

**Parameters:**
- `key_vault_name` (str): The name of the key vault to be deleted.

### 6. `delete_keyvalut_secret(key_vault_name, secret_name)`

Deletes a specified secret from a key vault.

**Parameters:**
- `key_vault_name` (str): The name of the key vault.
- `secret_name` (str): The name of the secret to be deleted.
