import time
import json
import cb_bot
import print_reports


try:
    while True:
        with open("parameters.json", "r", encoding = "UTF-8") as handle:
            parameters = json.load(handle)
        for currency, parameter in parameters.items():
            product_info = cb_bot.get_product_info(product_id=parameter["GLOBAL_PRODUCT_ID"])
            if not product_info:
                SKIP_REPORT = (f"{product_info.product_id} | Skipping due to missing product info.")
                print_reports.price_webhook(SKIP_REPORT)
                #time.sleep(300)  # Wait before retrying
                continue

            has_dropped, current_price = cb_bot.check_price_drop(product_info, threshold=parameter["GLOBAL_NEG_THRESHOLD"])

            if current_price:
                current_report = (f"{product_info.product_id} | Price: ${current_price} | 24h Change: {product_info.price_percentage_change_24h}%")
                print_reports.price_webhook(current_report)


            if has_dropped:
                DROP_REPORT = (f"{product_info.product_id} | Price has dropped by 4%! Placing a buy order...")
                print_reports.buy_webhook(DROP_REPORT)
                order_response = cb_bot.place_buy_order(product_id=parameter["GLOBAL_PRODUCT_ID"], amount_in_usdc=currency["GLOBAL_BUY_INCREMENT"])
                if order_response:
                    order_report = (f"{product_info.product_id} | Buy order response:, {order_response}")
                    print_reports.buy_webhook(order_report)
                    break  # Exit after successful purchase
        time.sleep(3600)  # Wait 1 hour before checking again


except Exception as e:
    exception_msg = f"An unexpected error occurred: {e}"
    print_reports.error_webhook(exception_msg)
