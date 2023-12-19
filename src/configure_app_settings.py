from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import NameValuePair
from azure.identity import DefaultAzureCredential
import os

def set_app_settings(settings):
    """
    Set application settings for an Azure App Service.

    Parameters:
    settings (dict): A dictionary of settings to apply.

    Returns:
    None
    """
    # Get Azure credentials
    credential = DefaultAzureCredential()

    # Create a WebSiteManagementClient
    web_client = WebSiteManagementClient(
        credential, os.getenv('AZURE_SUBSCRIPTION_ID'))

    # Set the app settings
    app_settings = web_client.web_apps.list_application_settings(
        os.getenv('AZURE_RESOURCE_GROUP_NAME'), os.getenv('AZURE_WEB_APP_NAME'))
    new_settings = {**app_settings.properties, **settings}
    web_client.web_apps.update_application_settings(
        os.getenv('AZURE_RESOURCE_GROUP_NAME'), os.getenv('AZURE_WEB_APP_NAME'), NameValuePair(new_settings))


if __name__ == "__main__":
    # Example usage
    settings = {
        "SETTING1": "VALUE1",
        "SETTING2": "VALUE2"
    }
    set_app_settings(settings)