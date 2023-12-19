"""
Module to scale an Azure App Service.

This module contains functions to scale up or out an Azure App Service
using the azure.mgmt.web package.
"""

from azure.mgmt.web import WebSiteManagementClient
from azure.identity import DefaultAzureCredential
import os

def scale_app_service(resource_group_name, name, sku_name):
    """
    Scale an Azure App Service.

    Parameters:
    resource_group_name (str): The name of the resource group.
    name (str): The name of the App Service.
    sku_name (str): The SKU name to scale to.

    Returns:
    None
    """
    # Get Azure credentials
    credential = DefaultAzureCredential()

    # Create a WebSiteManagementClient
    web_client = WebSiteManagementClient(credential, os.getenv('AZURE_SUBSCRIPTION_ID'))

    # Get the current app service plan
    app_service_plan = web_client.app_service_plans.get(resource_group_name, name)

    # Update the SKU
    app_service_plan.sku.name = sku_name
    web_client.app_service_plans.create_or_update(resource_group_name, name, app_service_plan)

if __name__ == "__main__":
    # Example usage
    scale_app_service(os.getenv('AZURE_RESOURCE_GROUP_NAME'), os.getenv('AZURE_WEB_APP_NAME'), os.getenv('AZURE_SKU_NAME'))