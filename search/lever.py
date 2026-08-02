import requests

BASE="https://api.lever.co/v0/postings/{company}?mode=json"

def search(company):

    jobs=[]

    try:

        r=requests.get(BASE.format(company=company),timeout=20)

        if r.status_code!=200:

            return jobs

        for job in r.json():

            jobs.append({

                "company":company.title(),

                "title":job["text"],

                "location":job["categories"]["location"],

                "url":job["hostedUrl"],

                "platform":"Lever"

            })

    except:

        pass

    return jobs
