from search_jobs import search_jobs
from email_report import send_email

jobs = search_jobs()

print(f"Found {len(jobs)} jobs")

if jobs:
    send_email(jobs)
