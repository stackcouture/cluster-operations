from google.cloud import secretmanager


def get_secret(secret):

    client = secretmanager.SecretManagerServiceClient()

    project = "project-18ee516c-a108-431d-a73"

    name = f"projects/{project}/secrets/{secret}/versions/latest"

    response = client.access_secret_version(
        request={"name": name}
    )

    return response.payload.data.decode()