import requests


def search(workday_company):

    jobs = []

    company = workday_company["company"]
    base_url = workday_company["url"]

    print(f"Searching Workday: {company}")

    # TODO:
    # Fetch jobs from the Workday endpoint

    return jobs
