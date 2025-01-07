import time
import bot
import webhook


try:
    while True:
        bot_config = bot.bot_config_retrieval()
        for currency, parameter in bot_config.items():
            product_info = bot.get_product_info(product_id=parameter["GLOBAL_PRODUCT_ID"])
            if not product_info:
                SKIP_REPORT = (f"{product_info.product_id} | Skipping due to missing product info.")
                webhook.price_webhook(SKIP_REPORT)
                continue


            has_dropped, current_price = bot.check_price_drop(product_info, threshold=parameter["GLOBAL_NEG_THRESHOLD"])


            if current_price:
                current_report = (f"{product_info.product_id} | Price: ${current_price} | 24h Change: {product_info.price_percentage_change_24h}%")
                webhook.price_webhook(current_report)


            if has_dropped:
                DROP_REPORT = (f"{product_info.product_id} | Price has dropped by 4%! Placing a buy order...")
                webhook.buy_webhook(DROP_REPORT)
                order_response = bot.place_buy_order(product_id=parameter["GLOBAL_PRODUCT_ID"], amount_in_usdc=parameter["GLOBAL_BUY_INCREMENT"])
                if order_response:
                    order_report = (f"{product_info.product_id} | Buy order response:, {order_response}")
                    webhook.buy_webhook(order_report)
                    break
        time.sleep(3600)


except Exception as e:
    exception_msg = f"An unexpected error occurred: {e}"
    webhook.error_webhook(exception_msg)
