"""
This script creates an Azure App Service Web App.

It uses the Azure SDK for Python to authenticate with Azure, create a resource group, and create a web app within that resource group. The script uses environment variables for configuration, including the Azure subscription ID, resource group name, web app name, and server farm ID.

The script logs its progress, logging both the creation of the resource group and the web app. If the script encounters an error during the creation of the resource group or the web app, it logs the error and raises an exception.
"""

import logging
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get configuration from environment variables
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
RESOURCE_GROUP_NAME = os.getenv("AZURE_RESOURCE_GROUP_NAME")
WEB_APP_NAME = os.getenv("AZURE_WEB_APP_NAME")
SERVER_FARM_ID = os.getenv("AZURE_SERVER_FARM_ID")


def authenticate_client(subscription_id):
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)
    web_client = WebSiteManagementClient(credential, subscription_id)

    return resource_client, web_client


def create_resource_group(resource_client):
    try:
        resource_group = resource_client.resource_groups.create_or_update(
            RESOURCE_GROUP_NAME,
            {
                "location": "eastus"
            }
        )
        logging.info(f"Created resource group {RESOURCE_GROUP_NAME}")
        return resource_group
    except Exception as e:
        logging.error(f"Failed to create resource group: {e}")
        raise


def create_web_app(web_client):
    # Use the web_client parameter instead of creating a new WebSiteManagementClient instance
    web_client.web_apps.create_or_update(
        os.getenv("AZURE_RESOURCE_GROUP_NAME"),
        os.getenv("AZURE_WEB_APP_NAME"),
        {
            "location": "eastus",
            "server_farm_id": os.getenv("AZURE_APP_SERVICE_PLAN_ID")
        }
    )


def main():
    resource_client, web_client = authenticate_client(SUBSCRIPTION_ID)
    resource_group = create_resource_group(resource_client)
    web_app = create_web_app(web_client)

    logging.info(f"Web app name: {web_app}")
    logging.info(f"Web app URL: {web_app.default_host_name}")


if __name__ == "__main__":
    main()
