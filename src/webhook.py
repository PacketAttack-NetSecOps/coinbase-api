import os
import toml
import requests


def webhook_url_retrieval():
    #src_path = os.path.dirname(__file__)[:-3]
    #with open(src_path + "config/webhooks.toml", "r", encoding = "UTF-8") as handle:
    secrets_path = os.path.abspath(os.sep) + "run/secrets/"
    with open(secrets_path + "webhooks.toml", "r", encoding = "UTF-8") as handle:
        webhooks = toml.load(handle)
        return webhooks

def price_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    webhooks = webhook_url_retrieval()
    #import pdb; pdb.set_trace()
    url = webhooks["webhook_urls"]["price-bot_url"]
    content = {"content": report}
    requests.post(url, json=content, timeout=10)


def buy_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    webhooks = webhook_url_retrieval()
    url = webhooks["webhook_urls"]["buy-bot_url"]
    content = {"content": report}
    requests.post(url, json=content, timeout=10)


def error_webhook(report):
    """Retrieves webhook url from webhooks file and sends report."""
    print(report)
    webhooks = webhook_url_retrieval()
    url = webhooks["webhook_urls"]["bot-errors_url"]
    content = {"content": report}
    requests.post(url, json=content, timeout=10)
