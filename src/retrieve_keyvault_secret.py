"""
This module retrieves a secret from an Azure Key Vault.

It uses the DefaultAzureCredential from the Azure Identity library for authentication,
which is suitable for most scenarios where the application runs in the Azure Cloud.

The SecretClient class from the Azure Key Vault Secrets library is used to interact with the Key Vault,
and the secret is retrieved using the get_secret method.

The name of the Key Vault and the name of the secret are required as inputs.
"""

# Import the necessary modules
import os
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the Key Vault name and secret name from environment variables
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME")
SECRET_NAME = os.getenv("SECRET_NAME")


def retrieve_secret(key_vault_name, secret_name):
    """
    Retrieve a secret from an Azure Key Vault.

    Parameters:
    key_vault_name (str): The name of the Azure Key Vault.
    secret_name (str): The name of the secret stored in the Azure Key Vault.

    Returns:
    str: The value of the secret.
    """
    try:
        # Create a credential object
        credential = DefaultAzureCredential()

        # Create a secret client
        secret_client = SecretClient(
            vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=credential)

        # Retrieve a secret
        secret = secret_client.get_secret(secret_name)

        return secret.value

    except ResourceNotFoundError:
        logging.error(
            f"The secret {secret_name} was not found in the Key Vault {key_vault_name}.")
        return None

    except Exception as e:
        logging.error(f"An error occurred while retrieving the secret: {e}")
        return None


def main():
    """
    The main function that retrieves and prints the secret value.
    """
    # Retrieve the secret value
    secret_value = retrieve_secret(KEY_VAULT_NAME, SECRET_NAME)

    if secret_value is not None:
        # Print the secret value
        logging.info(f"Secret value: {secret_value}")


if __name__ == "__main__":
    main()
