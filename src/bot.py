import os
import toml
import client
import webhook


def bot_config_retrieval():
    """retreives currency and parameters from bot.toml."""
    try:
        src_path = os.path.dirname(__file__)[:-3]
        with open(src_path + "config/bot_settings.toml", "r", encoding = "UTF-8") as handle:
        #secrets_path = os.path.abspath(os.sep) + "run/secrets/"
        #with open(secrets_path + "bot_settings.toml", "r", encoding = "UTF-8") as handle:
            bot_config = toml.load(handle)
            return bot_config
    except Exception as e:
        webhook.error_webhook(f"Error retrieving bot config.toml: {e}")
        return None
        

def get_product_info(product_id):
    """Fetch product information including price percentage change."""
    try:
        cdb_client = client.initialize_client()
        product_info = cdb_client.get_product(product_id)
        return product_info
    except Exception as e:
        webhook.error_webhook(f"Error fetching product info: {e}")
        return None


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
        return False, None


def place_buy_order(product_id, amount_in_usdc):
    """Place a market buy order."""
    try:
        cdb_client = client.initialize_client()
        order = cdb_client.place_order(
            product_id=product_id,
            side="buy",
            order_type="market",
            funds=amount_in_usdc  # Amount to spend in USDC
        )
        return order
    except Exception as e:
        webhook.error_webhook(f"Error placing buy order: {e}")
        return None