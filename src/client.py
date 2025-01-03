import os
import json
from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
import webhook


def cdp_api_key_retrieval():
    """retreives key and webhook url from secrets file."""
    try:
        #src_path = os.path.dirname(__file__)[:-3]
        #with open(src_path + "config/cdp_api_key.json", "r", encoding = "UTF-8") as handle:
        secrets_path = os.path.abspath(os.sep) + "run/secrets/"
        with open(secrets_path + "cdp_api_key.json", "r", encoding = "UTF-8") as handle:
            key_file = json.load(handle)
            return key_file
    except Exception as e:
        webhook.error_webhook(f"Error retrieving secrets: {e}")
        return None


def initialize_client():
    """Called upon by other modules to initialize the advanced trader cleint."""
    try:
        secrets = cdp_api_key_retrieval()
        name, privateKey = secrets["name"], secrets["privateKey"]
        client = EnhancedRESTClient(api_key = name, api_secret = privateKey)
        return client
    except Exception as e:
        webhook.error_webhook(f"Error initializing advanced trader client: {e}")
        return None