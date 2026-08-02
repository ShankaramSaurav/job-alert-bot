
import re

KEYWORDS = [

"Snowflake",
"SQL",
"Python",
"AWS",
"Azure",
"GCP",
"Spark",
"Kafka",
"Airflow",
"DBT",
"Databricks",
"ETL",
"ELT",
"Data Warehouse",
"Power BI",
"Tableau",
"Docker",
"Kubernetes",
"Git",
"CI/CD"

]


def extract(text):

    found = []

    lower = text.lower()

    for word in KEYWORDS:

        if re.search(rf"\b{re.escape(word.lower())}\b", lower):

            found.append(word)

    return found
