import os
import pytest
from dotenv import load_dotenv
from unittest.mock import Mock, patch
from src.create_app_service_webapp import create_resource_group
from src.create_app_service_webapp import create_web_app


@patch('src.create_app_service_webapp.ResourceManagementClient')
def test_create_resource_group(MockResourceManagementClient):
    # Arrange
    mock_resource_client = MockResourceManagementClient()
    mock_resource_client.resource_groups.create_or_update.return_value = "dummy_resource_group"

    # Act
    result = create_resource_group(mock_resource_client)

    # Assert
    mock_resource_client.resource_groups.create_or_update.assert_called_once_with(
        os.getenv("AZURE_RESOURCE_GROUP_NAME"),
        {
            "location": "eastus"
        }
    )


@patch('src.create_app_service_webapp.WebSiteManagementClient')
def test_create_web_app(MockWebSiteManagementClient):
    # Arrange
    mock_web_client = MockWebSiteManagementClient()
    mock_web_client.web_apps.create_or_update.return_value = "dummy_web_app"

    # Act
    result = create_web_app(mock_web_client)

    # Assert
    mock_web_client.web_apps.create_or_update.assert_called_once_with(
        os.getenv("AZURE_RESOURCE_GROUP_NAME"),
        os.getenv("AZURE_WEB_APP_NAME"),
        {
            "location": "eastus",
            "server_farm_id": os.getenv("AZURE_APP_SERVICE_PLAN_ID")
        }
    )
    
    
