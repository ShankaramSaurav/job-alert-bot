import json

from search.greenhouse import search as greenhouse

from search.lever import search as lever

from search.filters import ROLES, IGNORE

all_jobs=[]

with open("data/companies.json") as f:

    companies=json.load(f)

for company in companies["greenhouse"]:

    all_jobs.extend(greenhouse(company))

for company in companies["lever"]:

    all_jobs.extend(lever(company))

filtered=[]

for job in all_jobs:

    title=job["title"]

    if any(x.lower() in title.lower() for x in ROLES):

        if not any(x.lower() in title.lower() for x in IGNORE):

            filtered.append(job)

print()

print("="*80)

print(f"Found {len(filtered)} matching jobs")

print("="*80)

for job in filtered:

    print(job)
