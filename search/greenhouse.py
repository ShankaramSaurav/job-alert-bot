
import requests

BASE = "https://boards-api.greenhouse.io/v1/boards/{}/jobs"


def search(company):

    jobs = []

    try:

        url = BASE.format(company)

        r = requests.get(url, timeout=20)

        if r.status_code != 200:

            return jobs

        data = r.json()

        for job in data["jobs"]:

            jobs.append({

                "company": company.title(),

                "title": job["title"],

                "location": job["location"]["name"],

                "url": job["absolute_url"],

                "platform": "Greenhouse"

            })

    except Exception:

        pass

    return jobs
