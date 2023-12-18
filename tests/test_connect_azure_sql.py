import pytest
from unittest.mock import patch, Mock
from pyodbc import Error
from src.connect_azure_sql import connect_to_database


@patch('pyodbc.connect')
def test_connect_to_database(mock_connect):
    # Arrange
    mock_connect.return_value.cursor.return_value = 'mock_cursor'
    connection_string = 'dummy_connection_string'

    # Act
    result = connect_to_database(connection_string)

    # Assert
    mock_connect.assert_called_once_with(connection_string)
    assert result == 'mock_cursor'


@patch('pyodbc.connect')
def test_connect_to_database_error(mock_connect):
    # Arrange
    mock_connect.side_effect = Error('dummy_error')
    connection_string = 'dummy_connection_string'

    # Act & Assert
    with pytest.raises(Error):
        connect_to_database(connection_string)
