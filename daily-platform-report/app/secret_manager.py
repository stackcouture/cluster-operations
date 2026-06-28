import os
from google.cloud import secretmanager

def get_secret(secret_name: str):

    webhook = os.getenv("SLACK_WEBHOOK")

    if webhook:
        return webhook

    client = secretmanager.SecretManagerServiceClient()

    project_id = "project-18ee516c-a108-431d-a73"

    name = (
        f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    )

    response = client.access_secret_version(
        request={"name": name}
    )

    return response.payload.data.decode()