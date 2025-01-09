import json
import os
import time
import toml
import uuid
import client
import webhook


def bot_config_retrieval():
    """retreives currency and parameters from bot_settings.toml."""
    try:
        settings_path = os.path.abspath(os.sep) + "app/settings/"
        with open(settings_path + "bot_settings.toml", "r", encoding = "UTF-8") as handle:
            bot_config = toml.load(handle)
            return bot_config
    except Exception as e:
        webhook.error_webhook(f"Error retrieving bot_settings.toml: {e}")
        

def get_product_info(product_id):
    """Fetch product information including price percentage change."""
    try:
        cdb_client = client.initialize_client()
        product_info = cdb_client.get_product(product_id)
        return product_info
    except Exception as e:
        webhook.error_webhook(f"Error fetching product info: {e}")


def check_price_drop(product_info, threshold):
    """Check if the price has dropped by the given threshold percentage."""
    try:
        price_percentage_change = float(product_info.price_percentage_change_24h or 0)
        current_price = float(product_info.price or 0)

        if price_percentage_change <= threshold:  # Negative value indicates a drop
            return True, current_price
        return False, current_price
    except Exception as e:
        webhook.error_webhook(f"Error checking price drop: {e}")
        return False 


def place_buy_order(product_id, amount_in_usdc):
    """Place a market buy order."""
    try:
        cdb_client = client.initialize_client()
        order_id = uuid.uuid4()
        order = cdb_client.market_order_buy(
            client_order_id=str(order_id),
            product_id=product_id,
            quote_size=amount_in_usdc
        )

        if order['success']:
            time.sleep(10)
            order_id = order['success_response']['order_id']
            fills = cdb_client.get_fills(order_id=order_id)
            return (json.dumps(fills.to_dict(), indent=2))
            
            
        else:
            error_response = order['error_response']
            return(error_response)
    except Exception as e:
        webhook.error_webhook(f"Error placing buy order: {e}")
