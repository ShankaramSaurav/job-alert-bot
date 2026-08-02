MY_SKILLS = {

"Snowflake",

"SQL",

"Python",

"AWS",

"DBT",

"Airflow",

"Spark",

"Data Warehouse",

"ETL"

}


def score(skills):

    if not skills:
        return 0

    matches = len(MY_SKILLS.intersection(set(skills)))

    return round(matches / len(MY_SKILLS) * 100)
