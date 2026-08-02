import json

from search.greenhouse import search as greenhouse
from search.lever import search as lever

from search.filters import ROLES, IGNORE, PREFERRED_LOCATIONS

from utils.history import remove_duplicates
from utils.keyword_extractor import extract
from utils.scorer import score
from utils.csv_writer import export
from utils.email_sender import send_email

# Collect all jobs
all_jobs = []

with open("data/companies.json") as f:
    companies = json.load(f)

for company in companies["greenhouse"]:
    all_jobs.extend(greenhouse(company))

for company in companies["lever"]:
    all_jobs.extend(lever(company))

# Filter jobs
filtered = []

for job in all_jobs:

    title = job["title"]
    description = job["description"].lower()
    location = job["location"].lower()

    # Role check
    role_match = any(
        role.lower() in title.lower()
        for role in ROLES
    )

    # Ignore unwanted roles
    ignored = any(
        word.lower() in title.lower()
        for word in IGNORE
    )

    # Snowflake must be mentioned
    snowflake_match = "snowflake" in description

    # Preferred location
    location_match = any(
        loc in location
        for loc in PREFERRED_LOCATIONS
    )

    if role_match and not ignored and snowflake_match and location_match:
        filtered.append(job)
        
# Remove duplicate jobs
filtered = remove_duplicates(filtered)

# Extract skills and calculate score
for job in filtered:
    skills = extract(job["description"])
    job["skills"] = skills
    job["match"] = score(skills)

# Export to CSV
csv_file = export(filtered)
send_email(csv_file)

# Print results
print()
print("=" * 80)
print(f"Found {len(filtered)} matching jobs")
print("=" * 80)

for job in filtered:
    print("=" * 80)
    print("Company :", job["company"])
    print("Role    :", job["title"])
    print("Location:", job["location"])
    print("Platform:", job["platform"])
    print("Match   :", f'{job["match"]}%')
    print("Skills  :", ", ".join(job["skills"]))
    print("Apply   :", job["url"])
    print()
