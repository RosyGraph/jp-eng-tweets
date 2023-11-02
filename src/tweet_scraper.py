import csv
import random
from pathlib import Path as P

DATA_DIR = P(__file__).parent.parent / "data" / "elonmusk"
TWEET_IDX = 7

tweets = []

for file in DATA_DIR.glob("*.csv"):
    with open(file, "r") as f:
        reader = csv.reader(f)
        tweets.extend(
            row[TWEET_IDX].replace("&apm;", "&")
            for row in reader
            if len(row[TWEET_IDX].split(" ")) > 10 and "@" not in row[TWEET_IDX]
        )

print("\n".join(random.sample(tweets, 10)))
