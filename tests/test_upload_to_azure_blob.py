import os
import pytest
from unittest.mock import patch
from importlib import reload

# Import the module under test
import src.upload_to_azure_blob


def test_environment_variables():
    with patch.dict(os.environ, {
        "AZURE_STORAGE_CONNECTION_STRING": "test_connection_string",
        "AZURE_STORAGE_ACCOUNT_NAME": "test_account_name",
        "AZURE_STORAGE_BLOB_NAME": "test_blob_name",
        "AZURE_STORAGE_FILE_NAME": "test_file_name"
    }):
        reload(src.upload_to_azure_blob)
        assert src.upload_to_azure_blob.CONNECTION_STRING == "test_connection_string"
        assert src.upload_to_azure_blob.CONTAINER_NAME == "test_account_name"
        assert src.upload_to_azure_blob.BLOB_NAME == "test_blob_name"
        assert src.upload_to_azure_blob.FILE_NAME == "test_file_name"
