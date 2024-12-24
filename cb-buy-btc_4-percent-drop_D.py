### This script uses the coinbase api to check bitcoins price each hour. If the price has droped by 4% in the last 24 hours, a market buy is triggered ###
### The idea behind the script is that there is a continuous buy order when the bitcoin price is dropping helping to "stack" only on price corrections ###

from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
import time
import json


def initialize_client():
    try:
        with open("cb-api.json", "r", encoding = "UTF-8") as handle:
            secrets = json.load(handle)
            client = EnhancedRESTClient(api_key=secrets["api_key"], api_secret=secrets["api_secret"])
    except FileNotFoundError:
        print("Error: secrets file not found.")
        return None, None
    except KeyError:
        print("Error: Invalid format in config.json. Ensure it contains 'api_key' and 'api_secret'.")
        return None, None


def get_product_info(client, product_id="BTC-USDC"):
    """Fetch product information including price percentage change."""
    try:
        client = initialize_client()
        product_info = client.get_product(product_id=product_id)
        return product_info
    except Exception as e:
        print(f"Error fetching product info: {e}")
        return None


def check_price_drop(product_info, threshold=4):
    """Check if the price has dropped by the given threshold percentage."""
    try:
        # Access attributes directly from the product_info object
        price_percentage_change = float(product_info.price_percentage_change_24h or 0)
        current_price = float(product_info.price or 0)

        if price_percentage_change <= -threshold:  # Negative value indicates a drop
            return True, current_price
        return False, current_price
    except Exception as e:
        print(f"Error checking price drop: {e}")
        return False, None


def place_buy_order(client, product_id="BTC-USDC", amount_in_usdc="10", client):
    """Place a market buy order."""
    try:
        client = initialize_client()
        order = client.place_order(
            product_id=product_id,
            side="buy",
            order_type="market",
            funds=amount_in_usdc  # Amount to spend in USDC
        )
        return order
    except Exception as e:
        print(f"Error placing buy order: {e}")
        return None


# Main loop to monitor and place a buy order
try:
    while True:
        client=initialize_client()
        product_info = get_product_info(client)
        if not product_info:
            print("Skipping due to missing product info.")
            time.sleep(300)  # Wait before retrying
            continue

        has_dropped, current_price = check_price_drop(product_info, threshold=4)

        if current_price:
            print(f"Price: ${current_price} | 24h Change: {product_info.price_percentage_change_24h}%")

        if has_dropped:
            print("Price has dropped by 4%! Placing a buy order...")
            order_response = place_buy_order(client)
            if order_response:
                print("Buy order response:", order_response)
                break  # Exit after successful purchase

        time.sleep(3600)  # Wait 1 hour before checking again
except Exception as e:
    print("An unexpected error occurred:", e)
