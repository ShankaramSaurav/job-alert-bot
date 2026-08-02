def extract_keywords(title):

    mapping = {

        "Senior Data Engineer": (
            [
                "Data Engineering",
                "ETL",
                "Data Warehouse",
                "Cloud",
                "Data Pipelines",
            ],
            [
                "Snowflake",
                "Python",
                "SQL",
                "Airflow",
                "AWS",
            ],
        ),

        "Lead Data Engineer": (
            [
                "Architecture",
                "Mentoring",
                "ETL",
                "Scalable Systems",
                "Optimization",
            ],
            [
                "Snowflake",
                "Spark",
                "Python",
                "Kafka",
                "AWS",
            ],
        ),
    }

    for role in mapping:

        if role.lower() in title.lower():

            return mapping[role]

    return (
        ["Data Engineering"] * 5,
        ["Python", "SQL", "Snowflake", "AWS", "Airflow"],
    )
