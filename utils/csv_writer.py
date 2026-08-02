import pandas as pd


def export(jobs):

    if not jobs:
        return

    df = pd.DataFrame(jobs)

    df["skills"] = df["skills"].apply(lambda x: ", ".join(x))

    df.to_csv("report.csv", index=False)
