import json
from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
import print_reports


def secrets_retreival():
    """retreives key and webhook url from secrets file."""
    try:
        with open("cb-api-key.json", "r", encoding = "UTF-8") as handle:
            key_file = json.load(handle)
            return key_file
    except Exception as e:
        print_reports.error_webhook(f"Error retrieving secrets: {e}")
        return None


def initialize_client():
    """Called upon by other modules to initialize the advanced trader cleint."""
    try:
        secrets = secrets_retreival()
        name, privateKey = secrets["name"], secrets["privateKey"]
        client = EnhancedRESTClient(api_key = name, api_secret = privateKey)
        return client
    except Exception as e:
        print_reports.error_webhook(f"Error initializing advanced trader client: {e}")
        return None