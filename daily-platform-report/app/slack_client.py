import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from secret_manager import get_secret
import os

def send_summary(summary):

    webhook = get_secret("slack-webhook")

    payload = {
        "text": f"""
*Daily Platform Report*

Cluster : {summary.cluster_name}

Nodes Ready : {summary.ready_nodes}/{summary.total_nodes}

Running Pods : {summary.running_pods}

Pending Pods : {summary.pending_pods}

Deployments : {summary.ready_deployments}/{summary.total_deployments}

Status : {"Healthy" if summary.cluster_healthy else "Unhealthy"}
"""
    }

    response = requests.post(
        webhook,
        json=payload,
        timeout=10
    )

    response.raise_for_status()


def upload_pdf_to_slack(pdf_file):

    token = get_secret("slack-bot-token")

    client = WebClient(token=token)

    try:

        import os

        response = client.files_upload_v2(
            channel="C0BEJ4JUE2C",
            file=pdf_file,
            filename=os.path.basename(pdf_file),
            title="Daily Platform Report",
            initial_comment="📄 Daily Platform Report"
        )

        print("PDF uploaded successfully")

    except SlackApiError as e:

        print(e.response["error"])