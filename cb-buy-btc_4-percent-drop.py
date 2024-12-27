### This script uses the Coinbase API to check Bitcoin price each hour. If the price has droped by 4% in the last 24 hours, a market buy is triggered ###
### The idea behind the script is that there is a continuous buy order when the bitcoin price is dropping helping to "stack"                          ###

from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient
import time
import json
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the JSON file
json_path = os.path.join(script_dir, 'cb-api.json')

# Load API credentials from JSON file
try:
    with open(json_path, 'r') as f:
        credentials = json.load(f)
        api_key = credentials['api_key']
        api_secret = credentials['api_secret']
except Exception as e:
    print(f"Error loading API credentials: {e}")
    exit(1)

client = EnhancedRESTClient(api_key=api_key, api_secret=api_secret)

def get_product_info(product_id="BTC-USDC"):
    """Fetch product information including price percentage change."""
    try:
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

def place_buy_order(product_id="BTC-USDC", amount_in_usdc="25"):
    """Place a market buy order."""
    try:
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
        product_info = get_product_info()
        if not product_info:
            print("Skipping due to missing product info.")
            time.sleep(300)  # Wait before retrying
            continue

        has_dropped, current_price = check_price_drop(product_info, threshold=4)

        if current_price:
            print(f"Price: ${current_price} | 24h Change: {product_info.price_percentage_change_24h}%")

        if has_dropped:
            print("Price has dropped by 4%! Placing a buy order...")
            order_response = place_buy_order(amount_in_usdc="25")
            if order_response:
                print("Buy order response:", order_response)
                break  # Exit after successful purchase

        time.sleep(3600)  # Wait 1 hour before checking again
except Exception as e:
    print("An unexpected error occurred:", e)
