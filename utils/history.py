
import json
import os

HISTORY_FILE = "data/history.json"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return set()

    with open(HISTORY_FILE, "r") as f:
        return set(json.load(f))


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(list(history), f, indent=4)


def remove_duplicates(jobs):

    history = load_history()

    new_jobs = []

    for job in jobs:

        uid = f"{job['company']}|{job['title']}|{job['url']}"

        if uid not in history:
            new_jobs.append(job)
            history.add(uid)

    save_history(history)

    return new_jobs
