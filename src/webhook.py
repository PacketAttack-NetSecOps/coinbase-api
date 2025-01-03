import requests
import json


def price_webhook(report):
    """Retrieves webhook url from secrets file and sends report."""
    print(report)
    with open("cb-api.json", "r", encoding = "UTF-8") as handle:
        secrets = json.load(handle)
        url = secrets["price-bot_url"]
        content = {"content": report}
        requests.post(url, json=content)


def buy_webhook(report):
    """Retrieves webhook url from secrets file and sends report."""
    print(report)
    with open("cb-api.json", "r", encoding = "UTF-8") as handle:
        secrets = json.load(handle)
        url = secrets["buy-bot_url"]
        content = {"content": report}
        requests.post(url, json=content)


def error_webhook(report):
    """Retrieves webhook url from secrets file and sends report."""
    print(report)
    with open("cb-api.json", "r", encoding = "UTF-8") as handle:
        secrets = json.load(handle)
        url = secrets["bot-errors_url"]
        content = {"content": report}
        requests.post(url, json=content)