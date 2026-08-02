import json

from search.greenhouse import search as greenhouse
from search.lever import search as lever
from search.workday import search as workday
from search.google_jobs import search as google_jobs

def search_all():

    all_jobs = []

    with open("data/companies.json") as f:
        companies = json.load(f)

    # Search Greenhouse companies
    for company in companies["greenhouse"]:
        all_jobs.extend(greenhouse(company))

    # Search Lever companies
    for company in companies["lever"]:
        all_jobs.extend(lever(company))
    
    # Search workday companies
    for company in companies["workday"]:
        all_jobs.extend(workday(company))

    all_jobs.extend(google_jobs())

    return all_jobs
