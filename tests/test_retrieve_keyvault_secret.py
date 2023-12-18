import pytest
from unittest.mock import patch, Mock
from azure.core.exceptions import ResourceNotFoundError
from src.retrieve_keyvault_secret import retrieve_secret

@patch('src.retrieve_keyvault_secret.SecretClient')
def test_retrieve_secret(mock_secret_client):
    # Arrange
    mock_secret_client.return_value.get_secret.return_value.value = 'mock_secret'
    key_vault_name = 'dummy_key_vault_name'
    secret_name = 'dummy_secret_name'

    # Act
    result = retrieve_secret(key_vault_name, secret_name)

    # Assert
    mock_secret_client.return_value.get_secret.assert_called_once_with(secret_name)
    assert result == 'mock_secret'

@patch('src.retrieve_keyvault_secret.SecretClient')
def test_retrieve_secret_error(mock_secret_client):
    # Arrange
    mock_secret_client.return_value.get_secret.side_effect = ResourceNotFoundError('dummy_error')
    key_vault_name = 'dummy_key_vault_name'
    secret_name = 'dummy_secret_name'

    # Act & Assert
    with pytest.raises(ResourceNotFoundError):
        retrieve_secret(key_vault_name, secret_name)