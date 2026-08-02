import os
import smtplib

from email.mime.text import MIMEText

from keyword_extractor import extract_keywords


def send_email(jobs):

    html = """
    <h2>Daily Data Engineer Jobs</h2>

    <table border="1" cellpadding="6">

    <tr>

    <th>Company</th>

    <th>Role</th>

    <th>Location</th>

    <th>Link</th>

    <th>Keywords</th>

    <th>Technical Skills</th>

    </tr>

    """

    for job in jobs:

        keywords, skills = extract_keywords(job["title"])

        html += f"""

        <tr>

        <td>{job['company']}</td>

        <td>{job['title']}</td>

        <td>{job['location']}</td>

        <td><a href="{job['url']}">Apply</a></td>

        <td>{', '.join(keywords)}</td>

        <td>{', '.join(skills)}</td>

        </tr>

        """

    html += "</table>"

    msg = MIMEText(html, "html")

    msg["Subject"] = "Daily Data Engineer Jobs"

    msg["From"] = os.environ["EMAIL_ADDRESS"]

    msg["To"] = os.environ["TO_EMAIL"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(
            os.environ["EMAIL_ADDRESS"],
            os.environ["EMAIL_PASSWORD"],
        )

        smtp.send_message(msg)
