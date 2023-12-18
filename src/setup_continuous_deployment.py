"""
This script sets up continuous deployment for an Azure App Service Web App from a GitHub repository.

It uses the Azure SDK for Python to authenticate with Azure, and sets up continuous deployment for a web app within a resource group. The script uses environment variables for configuration, including the Azure subscription ID, resource group name, web app name, GitHub repository URL, and branch name.

The script logs its progress, logging the setup of the continuous deployment. If the script encounters an error during the setup, it logs the error and raises an exception.
"""

import os
import logging
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import SiteSourceControl

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get configuration from environment variables
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
RESOURCE_GROUP_NAME = os.getenv("AZURE_RESOURCE_GROUP_NAME")
WEB_APP_NAME = os.getenv("AZURE_WEB_APP_NAME")
REPO_URL = os.getenv("REPO_URL")
BRANCH = os.getenv("BRANCH")

def setup_continuous_deployment():
    """
    Set up continuous deployment for an Azure App Service Web App from a GitHub repository.
    """
    # Get a credential for authentication
    credential = DefaultAzureCredential()

    # Create a client for WebSiteManagement
    web_client = WebSiteManagementClient(credential, SUBSCRIPTION_ID)

    # Set up continuous deployment
    logging.info(f"Setting up continuous deployment for web app {WEB_APP_NAME}...")
    source_control = SiteSourceControl(repo_url=REPO_URL, branch=BRANCH, is_manual_integration=False, is_mercurial=False)
    web_client.web_apps.create_or_update_source_control(RESOURCE_GROUP_NAME, WEB_APP_NAME, source_control)

    logging.info("Continuous deployment set up successfully.")

if __name__ == "__main__":
    setup_continuous_deployment()