import os
import pandas as pd


def export(jobs):

    if not jobs:
        return

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(jobs)
    df["skills"] = df["skills"].apply(lambda x: ", ".join(x))

    OUTPUT = "output/report.csv"

    df.to_csv(OUTPUT, index=False)

    return OUTPUT
