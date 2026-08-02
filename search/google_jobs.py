import os
import requests

SERPER_URL = "https://google.serper.dev/search"

QUERIES = [
    '"Senior Data Engineer" Snowflake India',
    '"Lead Data Engineer" Snowflake India',
    '"Staff Data Engineer" Snowflake India',
    '"Principal Data Engineer" Snowflake India',
    '"Data Platform Engineer" Snowflake India',
    '"Snowflake Data Engineer" India',
]

def search():

    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        print("SERPER_API_KEY not configured.")
        return []

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    jobs = []

    for query in QUERIES:

        print(f"Searching Google: {query}")

        payload = {
            "q": query,
            "num": 20
        }

        response = requests.post(
            SERPER_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            print(f"Failed for query: {query}")
            continue

        data = response.json()

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
