# Azure App Service Web App Creator

This project contains a Python script to automate the creation of an Azure App Service Web App.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10
- Azure SDK for Python
- An active Azure subscription

### Installing

1. Clone the repository:

   ```bash
   git clone https://github.com/5c077-60rd0n/azure-app-service-web-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd azure-app-service-web-app
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Before running the script, you need to set the following environment variables:

- `AZURE_SUBSCRIPTION_ID`: Your Azure Subscription ID
- `AZURE_RESOURCE_GROUP_NAME`: The name of the Azure Resource Group
- `AZURE_WEB_APP_NAME`: The name of the Azure Web App
- `AZURE_SERVER_FARM_ID`: The ID of the Azure Server Farm
- `KEY_VAULT_NAME`: The name of your Azure Key Vault
- `SECRET_NAME`: The name of the secret in your Azure Key Vault

Then, run the script:

## Running the tests

You can run the tests using pytest:

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](https://github.com/5c077-60rd0n/azure-app-service-web-app/blob/main/CONTRIBUTING.md) for details on how to contribute and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/5c077-60rd0n/azure-app-service-web-app/blob/main/LICENSE.md) file for details.
