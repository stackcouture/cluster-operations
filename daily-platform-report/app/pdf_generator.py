from datetime import datetime
import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from report_generator import generate


def create_pdf(summary):

    os.makedirs("reports", exist_ok=True)

    report = generate(summary)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    pdf_file = f"reports/platform-report-{timestamp}.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(pdf_file)

    story = []

    story.append(
        Paragraph(
            "<b>Daily Platform Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    for line in report.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["BodyText"])
            )

    doc.build(story)

    print(f"PDF generated: {pdf_file}")

    return pdf_file