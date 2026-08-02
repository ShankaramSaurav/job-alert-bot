
import smtplib
import os

from email.message import EmailMessage


def send_email(csv_file):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("TO_EMAIL")

    if not sender or not password or not receiver:
        print("Email credentials not configured.")
        return

    msg = EmailMessage()

    msg["Subject"] = "Daily Data Engineering Jobs"

    msg["From"] = sender

    msg["To"] = receiver

    msg.set_content(
        "Hi,\n\nAttached is today's job report.\n\nGood luck!"
    )

    with open(csv_file, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="jobs.csv",
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

    print("Email sent successfully.")
