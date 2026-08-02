import pandas as pd
import os

def export(jobs):
    if not jobs:
        return

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(jobs)
    df["skills"] = df["skills"].apply(lambda x: ", ".join(x))

    output_file = "output/report.csv"
    df.to_csv(output_file, index=False)

    print(f"CSV exported to {output_file}")
