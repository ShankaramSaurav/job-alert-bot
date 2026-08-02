import os
import pandas as pd


def export(jobs):

    if not jobs:
        print("No jobs to export.")
        return None

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(jobs)
    df["skills"] = df["skills"].apply(lambda x: ", ".join(x))

    output_file = "output/report.csv"
    df.to_csv(output_file, index=False)

    print(f"CSV exported to {output_file}")

    return output_file
