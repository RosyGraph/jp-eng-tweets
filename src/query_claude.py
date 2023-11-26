from pathlib import Path as P
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import pandas as pd

SEED = 42
NUM_TWEETS = 50

JP_PROMPT = "Produce an explanation in Japanese of following Tweet from Twitter user @{author}.\n\n{content}"
ENG_PROMPT = "Produce an explanation of following Tweet from Twitter user @{author}.\n\n{content}"
REPORTS_DIR = P(__file__).parent.parent / "reports"

tweets_df = pd.read_csv("data/tweets.csv")
sample_tweets = tweets_df.sample(n=NUM_TWEETS, random_state=SEED)[["author", "content"]]

anthropic = Anthropic()


def query_claude(tweet_row, prompt):
    author = tweet_row["author"]
    content = tweet_row["content"]

    return anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}".format(author=author, content=content),
    ).completion


output_df = pd.DataFrame(columns=["author", "content", "jp_explanation", "en_explanation"])
output_list = []

for _, row in sample_tweets.iterrows():
    jp_explanation = query_claude(row, JP_PROMPT)
    eng_explanation = query_claude(row, ENG_PROMPT)
    output_list.append(
        {
            "author": row["author"],
            "content": row["content"],
            "jp_explanation": jp_explanation,
            "en_explanation": eng_explanation,
        }
    )

print(output_list)
output_df = pd.DataFrame(output_list)
output_df.to_json(REPORTS_DIR / "tweets_report.json", ensure_ascii=False, indent=2)
