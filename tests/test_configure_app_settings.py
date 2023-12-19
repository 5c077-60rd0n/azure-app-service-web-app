import pytest
import os
from unittest.mock import patch, MagicMock
from src.configure_app_settings import set_app_settings

@patch('src.configure_app_settings.WebSiteManagementClient')
@patch('src.configure_app_settings.NameValuePair')
def test_set_app_settings(mock_name_value_pair, mock_web_client):
    # Mock the list_application_settings and update_application_settings methods
    mock_web_client_instance = MagicMock()
    mock_web_client_instance.web_apps.list_application_settings.return_value.properties = {}
    mock_web_client_instance.web_apps.update_application_settings.return_value = None
    mock_web_client.return_value = mock_web_client_instance

    # Mock the NameValuePair class
    mock_name_value_pair.return_value = {}

    # Call the function with a test settings dictionary
    test_settings = {"SETTING1": "VALUE1", "SETTING2": "VALUE2"}
    set_app_settings(test_settings)

    # Check if the list_application_settings method was called with the correct arguments
    mock_web_client_instance.web_apps.list_application_settings.assert_called_once_with(
        os.getenv('AZURE_RESOURCE_GROUP_NAME'), os.getenv('AZURE_WEB_APP_NAME'))

    # Check if the update_application_settings method was called with the correct arguments
    mock_web_client_instance.web_apps.update_application_settings.assert_called_once_with(
        os.getenv('AZURE_RESOURCE_GROUP_NAME'), os.getenv('AZURE_WEB_APP_NAME'), mock_name_value_pair.return_value)