import requests

GREENHOUSE_COMPANIES = {
    "Databricks": "databricks",
    "Snowflake": "snowflake",
    "Rubrik": "rubrik",
    "Confluent": "confluent",
    "Cockroach Labs": "cockroachlabs",
}

SEARCH_WORDS = [
    "Senior Data Engineer",
    "Lead Data Engineer",
    "Staff Data Engineer",
    "Principal Data Engineer",
]


def search_jobs():

    jobs = []

    for company, board in GREENHOUSE_COMPANIES.items():

        url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

        try:

            response = requests.get(url, timeout=20)

            if response.status_code != 200:
                continue

            data = response.json()

            for job in data["jobs"]:

                title = job["title"]

                if any(word.lower() in title.lower() for word in SEARCH_WORDS):

                    jobs.append(
                        {
                            "company": company,
                            "title": title,
                            "location": job["location"]["name"],
                            "url": job["absolute_url"],
                        }
                    )

        except Exception:
            pass

    return jobs
