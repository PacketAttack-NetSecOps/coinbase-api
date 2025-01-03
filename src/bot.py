import cb_client
import print_reports


def get_product_info(product_id):
    """Fetch product information including price percentage change."""
    try:
        client = cb_client.initialize_client()
        product_info = client.get_product(product_id)
        return product_info
    except Exception as e:
        print_reports.error_webhook(f"Error fetching product info: {e}")
        return None


def check_price_drop(product_info, threshold):
    """Check if the price has dropped by the given threshold percentage."""
    try:
        # Access attributes directly from the product_info object
        price_percentage_change = float(product_info.price_percentage_change_24h or 0)
        current_price = float(product_info.price or 0)

        if price_percentage_change <= threshold:  # Negative value indicates a drop
            return True, current_price
        return False, current_price
    except Exception as e:
        print_reports.error_webhook(f"Error checking price drop: {e}")
        return False, None


def place_buy_order(product_id, amount_in_usdc):
    """Place a market buy order."""
    try:
        client = cb_client.initialize_client()
        order = client.place_order(
            product_id=product_id,
            side="buy",
            order_type="market",
            funds=amount_in_usdc  # Amount to spend in USDC
        )
        return order
    except Exception as e:
        print_reports.error_webhook(f"Error placing buy order: {e}")
        return None