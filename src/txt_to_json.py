import json
from pathlib import Path as P

REPORTS_PATH = P(__file__).parent.parent / "reports"
JSON_PATH = REPORTS_PATH / "elonmusk_claude1-2.json"
TXT_PATH = REPORTS_PATH / "elonmusk_claude1-2.txt"

TWEET_IDX = 0
JP_IDX = 1
EN_IDX = 2

tweets = []
obj = {}
for i, line in enumerate(TXT_PATH.open(encoding="utf-8")):
    i = i % 3
    if i == 0:
        obj["tweet"] = line
    elif i == 1:
        obj["jp_explanation"] = line
    elif i == 2:
        obj["en_explanation"] = line
        tweets.append(obj)
        obj = {}

JSON_PATH.write_text(json.dumps(tweets, ensure_ascii=False, indent=2))
