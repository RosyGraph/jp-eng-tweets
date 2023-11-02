import json
from pathlib import Path as P

JSON_FILE = P(__file__).parent.parent / "reports" / "elonmusk_claude1-2.json"
OUTPUT_FILE = (
    P(__file__).parent.parent / "reports" / "elonmusk_claude1-2_responses.json"
)

with open(JSON_FILE, "r") as f:
    data = json.load(f)
player = input("Select a character: (1) JP (2) EN")
if player == "1":
    print("You selected JP")
    for row in data:
        print("TWEET:\n" + row["tweet"] + "\n")
        print("EXPLANATION:\n" + row["jp_explanation"] + "\n")
        row["jp_comprehensiveness"] = int(input("Comprehensiveness: 1-5"))
        row["jp_relevance"] = int(input("Relevance: 1-5"))
        row["jp_accuracy"] = int(input("Accuracy: 1-5"))
elif player == "2":
    print("You selected EN")
    for row in data:
        print("TWEET:\n" + row["tweet"] + "\n")
        print("EXPLANATION:\n" + row["en_explanation"] + "\n")
        row["en_comprehensiveness"] = int(input("Comprehensiveness: 1-5"))
        row["en_relevance"] = int(input("Relevance: 1-5"))
        row["en_accuracy"] = int(input("Accuracy: 1-5"))

with open(OUTPUT_FILE, "w") as f:
    json.dump(data, f, indent=2)
