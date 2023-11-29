from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent.parent / "reports" / "tweets_report.json"


def load_df():
    df = pd.read_json(DATA_PATH)
    df["tweet_index"] = df.index
    return df
