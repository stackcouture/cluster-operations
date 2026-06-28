from kubernetes_client import get_cluster_summary
from report_generator import generate
from slack_client import send_report


def main():
    summary = get_cluster_summary()

    report = generate(summary)

    print(report)

    send_report(report)

    print("Slack notification sent successfully")


if __name__ == "__main__":
    main()