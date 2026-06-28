from datetime import datetime
from google.cloud import storage
import os

BUCKET_NAME = "platform-reports-project-18ee516c-a108-431d-a73"


def upload_pdf_to_gcs(pdf_file):

    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    now = datetime.utcnow()

    blob_name = (
        f"{now:%Y/%m/%d}/"
        f"{os.path.basename(pdf_file)}"
    )

    blob = bucket.blob(blob_name)

    blob.upload_from_filename(pdf_file)

    print(f"Uploaded to gs://{BUCKET_NAME}/{blob_name}")

    return blob_name