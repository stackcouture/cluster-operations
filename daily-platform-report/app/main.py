from kubernetes_client import get_cluster_summary
from report_generator import generate
from pdf_generator import create_pdf
from gcs_client import upload_pdf_to_gcs
from slack_client import send_summary
from slack_client import upload_pdf_to_slack


def main():

    summary = get_cluster_summary()

    report = generate(summary)

    pdf_file = create_pdf(summary)

    # Upload to GCS
    gcs_path = upload_pdf_to_gcs(pdf_file)

    # Send Slack summary
    send_summary(summary)

    # Optional: Upload PDF to Slack
    upload_pdf_to_slack(pdf_file)


if __name__ == "__main__":
    main()