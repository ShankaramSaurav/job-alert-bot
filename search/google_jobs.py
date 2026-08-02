import os
import requests

SERPER_URL = "https://google.serper.dev/search"


def search():

    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        print("SERPER_API_KEY not configured.")
        return []

    query = (
        '("Senior Data Engineer" OR "Lead Data Engineer" '
        'OR "Staff Data Engineer") '
        'Snowflake India'
    )

    payload = {
        "q": query,
        "num": 20
    }

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(
        SERPER_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        print("Google search failed")
        return []

    data = response.json()

    jobs = []

    for item in data.get("organic", []):

        jobs.append({
            "company": item.get("title", "").split("-")[0].strip(),
            "title": item.get("title", ""),
            "location": "Unknown",
            "platform": "Google",
            "description": item.get("snippet", ""),
            "url": item.get("link", "")
        })

    return jobs
