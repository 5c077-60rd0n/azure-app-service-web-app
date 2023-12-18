import os
import pytest
from unittest.mock import patch, MagicMock
from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models import SiteSourceControl
import sys

sys.path.append('../src')

import src.setup_continuous_deployment

@patch.object(DefaultAzureCredential, '__init__', return_value=None)
@patch.object(WebSiteManagementClient, '__init__', return_value=None)
@patch('src.setup_continuous_deployment.SiteSourceControl')
def test_setup_continuous_deployment(mock_source_control_init, mock_web_client_init, mock_credential_init):
    # Mock the create_or_update_source_control method
    mock_web_client = MagicMock()
    mock_web_client.web_apps.create_or_update_source_control = MagicMock()

    # Replace the WebSiteManagementClient instance with our mock
    with patch('src.setup_continuous_deployment.WebSiteManagementClient', return_value=mock_web_client):
        src.setup_continuous_deployment.setup_continuous_deployment()

    # Check if the create_or_update_source_control method was called with the correct arguments
    mock_web_client.web_apps.create_or_update_source_control.assert_called_once_with(
        os.getenv("AZURE_RESOURCE_GROUP_NAME"), os.getenv("AZURE_WEB_APP_NAME"), mock_source_control_init.return_value)