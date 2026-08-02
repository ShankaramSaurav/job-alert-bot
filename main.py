import json

#from search.greenhouse import search as greenhouse
#from search.lever import search as lever

from search.filters import ROLES, IGNORE

from utils.history import remove_duplicates
from utils.keyword_extractor import extract
from utils.scorer import score
from utils.csv_writer import export
from utils.email_sender import send_email
from search.manager import search_all

# -----------------------------
# Collect jobs from all sources
# -----------------------------

# all_jobs = []

# with open("data/companies.json") as f:
#     companies = json.load(f)

# for company in companies["greenhouse"]:
#     all_jobs.extend(greenhouse(company))

# for company in companies["lever"]:
#     all_jobs.extend(lever(company))


all_jobs = search_all()


# -----------------------------
# Filter relevant jobs
# -----------------------------

filtered = []

for job in all_jobs:

    title = job.get("title", "").lower()

    role_match = any(
        role.lower() in title
        for role in ROLES
    )

    ignored = any(
        word.lower() in title
        for word in IGNORE
    )

    if role_match and not ignored:
        filtered.append(job)


# -----------------------------
# Remove duplicates
# -----------------------------

filtered = remove_duplicates(filtered)


# -----------------------------
# Extract skills & calculate score
# -----------------------------

for job in filtered:

    description = job.get("description", "")

    skills = extract(description)

    job["skills"] = skills
    job["match"] = score(skills)


# Highest matching jobs first
filtered.sort(
    key=lambda x: x["match"],
    reverse=True
)


# -----------------------------
# Generate CSV & Email
# -----------------------------

if filtered:

    csv_file = export(filtered)

    if csv_file:
        send_email(csv_file)

    print(f"\nEmail sent with {len(filtered)} matching jobs.")

else:

    print("\nNo matching jobs found today.")


# -----------------------------
# Console Output
# -----------------------------

print()
print("=" * 90)
print(f"Found {len(filtered)} matching jobs")
print("=" * 90)

for job in filtered:

    print("=" * 90)

    print("Company :", job.get("company", "N/A"))
    print("Role    :", job.get("title", "N/A"))
    print("Location:", job.get("location", "N/A"))
    print("Platform:", job.get("platform", "N/A"))
    print("Match   :", f"{job.get('match', 0)}%")

    skills = job.get("skills", [])

    if skills:
        print("Skills  :", ", ".join(skills))
    else:
        print("Skills  : None detected")

    print("Apply   :", job.get("url", ""))

    print()
