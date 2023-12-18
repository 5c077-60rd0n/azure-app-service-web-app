"""
This module uploads a file to an Azure Blob Storage container.

It uses the BlobServiceClient, ContainerClient, and BlobClient classes from the Azure Storage Blob library.

The connection string, container name, blob name, and file name should be replaced with your own values.
"""

# Import the necessary modules
import os
import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the connection string, container name, blob name, and file name from environment variables
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
BLOB_NAME = os.getenv("AZURE_STORAGE_BLOB_NAME")
FILE_NAME = os.getenv("AZURE_STORAGE_FILE_NAME")


def upload_file_to_blob(connection_string, container_name, blob_name, file_name):
    """
    Upload a file to an Azure Blob Storage container.

    Parameters:
    connection_string (str): The connection string for the Azure Storage account.
    container_name (str): The name of the container in the Azure Storage account.
    blob_name (str): The name of the blob in the container.
    file_name (str): The name of the file to upload.

    Returns:
    str: The URL of the uploaded blob.
    """
    try:
        # Create a blob service client
        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string)

        # Create a container client
        container_client = blob_service_client.get_container_client(
            container_name)

        # Create a blob client
        blob_client = container_client.get_blob_client(blob_name)

        # Upload a file
        with open(file_name, "rb") as data:
            blob_client.upload_blob(data)

        return blob_client.url

    except ResourceNotFoundError:
        logging.error(
            f"The container {container_name} or the blob {blob_name} was not found.")
        return None

    except Exception as e:
        logging.error(f"An error occurred while uploading the file: {e}")
        return None


def main():
    """
    The main function that uploads the file and prints the blob URL.
    """
    # Upload the file to the blob
    blob_url = upload_file_to_blob(
        CONNECTION_STRING, CONTAINER_NAME, BLOB_NAME, FILE_NAME)

    if blob_url is not None:
        # Print the blob URL
        logging.info(f"Blob URL: {blob_url}")


if __name__ == "__main__":
    main()
