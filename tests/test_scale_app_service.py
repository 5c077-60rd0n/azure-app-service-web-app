import pytest
from unittest.mock import patch, MagicMock
from src.scale_app_service import scale_app_service

@patch('src.scale_app_service.WebSiteManagementClient')
def test_scale_app_service(mock_web_client):
    # Mock the get and create_or_update methods
    mock_web_client_instance = MagicMock()
    mock_web_client_instance.app_service_plans.get.return_value.sku = MagicMock()
    mock_web_client_instance.app_service_plans.create_or_update.return_value = None
    mock_web_client.return_value = mock_web_client_instance

    # Call the function with test arguments
    test_resource_group_name = "test_resource_group"
    test_name = "test_name"
    test_sku_name = "test_sku_name"
    scale_app_service(test_resource_group_name, test_name, test_sku_name)

    # Check if the get method was called with the correct arguments
    mock_web_client_instance.app_service_plans.get.assert_called_once_with(test_resource_group_name, test_name)

    # Check if the create_or_update method was called with the correct arguments
    mock_web_client_instance.app_service_plans.create_or_update.assert_called_once_with(test_resource_group_name, test_name, mock_web_client_instance.app_service_plans.get.return_value)