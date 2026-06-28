import requests
from secret_manager import get_secret


def send_report(report: str):

    webhook = get_secret("slack-webhook")

    response = requests.post(
        webhook,
        json={"text": report},
        timeout=10
    )

    response.raise_for_status()