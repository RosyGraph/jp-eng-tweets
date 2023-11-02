from pathlib import Path as P

from pyperclip import paste

REPORTS_PATH = P(__file__).parent.parent / "reports"

raw_response = paste()

with open(REPORTS_PATH / "tweets.txt", "a") as f:
    f.write(raw_response.replace("\n", r"\n") + "\n")
