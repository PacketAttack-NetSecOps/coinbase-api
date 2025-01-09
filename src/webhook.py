import os
import toml
import requests


def webhook_url_retrieval():
    try:
        secrets_path = os.path.abspath(os.sep) + "run/secrets/"
        with open(secrets_path + "webhooks.toml", "r", encoding = "UTF-8") as handle:
            webhooks = toml.load(handle)
            return webhooks
    except Exception as e:
        print(f"Error fetching product info: {e}")


def price_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    try:
        webhooks = webhook_url_retrieval()
        #import pdb; pdb.set_trace()
        url = webhooks["webhook_urls"]["price-bot_url"]
        content = {"content": report}
        requests.post(url, json=content, timeout=10)
    except Exception as e:
        print(f"Error POSTing price report: {e}")


def buy_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    try:
        webhooks = webhook_url_retrieval()
        url = webhooks["webhook_urls"]["buy-bot_url"]
        content = {"content": report}
        requests.post(url, json=content, timeout=10)
    except Exception as e:
        print(f"Error POSTing buy report: {e}")


def error_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    try:
        webhooks = webhook_url_retrieval()
        url = webhooks["webhook_urls"]["bot-errors_url"]
        content = {"content": report}
        requests.post(url, json=content, timeout=10)
    except Exception as e:
        print(f"Error POSTing error report: {e}")
