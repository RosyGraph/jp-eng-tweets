from pathlib import Path as P

import pandas as pd

REPORTS_DIR = P(__file__).parent.parent / "reports"


def load_df():
    df = pd.read_json(REPORTS_DIR / "elonmusk_claude1-2.json")
    df["tweet_index"] = df.index
    df = df[
        [
            "tweet_index",
            "jp_comprehensiveness",
            "en_comprehensiveness",
            "jp_relevance",
            "en_relevance",
            "jp_accuracy",
            "en_accuracy",
        ]
    ]
    return df
