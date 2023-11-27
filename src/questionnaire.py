import json
from pathlib import Path as P

JSON_FILE = P(__file__).parent.parent / "reports" / "tweets_report.json"


def get_response():
    response = [None, None, None]
    while not all(response):
        try:
            response = [
                int(input("Comprehensiveness: 1-5: ")),
                int(input("Relevance: 1-5: ")),
                int(input("Accuracy: 1-5: ")),
            ]
            if not all(1 <= r <= 5 for r in response):
                print("Please enter a number between 1 and 5")
                response = [None, None, None]
        except ValueError:
            print("Please enter a number between 1 and 5")
    return response


with open(JSON_FILE, "r") as f:
    data = json.load(f)
player = input("Select a character: (1) JP (2) EN: ")
if player == "1":
    print("You selected JP")
    for row in data:
        print("AUTHOR: " + row["author"])
        print("TWEET:\n" + row["content"] + "\n")
        print("EXPLANATION:\n" + row["jp_explanation"] + "\n")
        (
            row["jp_comprehensiveness"],
            row["jp_relevance"],
            row["jp_accuracy"],
        ) = get_response()
elif player == "2":
    print("You selected EN")
    for row in data:
        print("AUTHOR: " + row["author"])
        print("TWEET:\n" + row["content"] + "\n")
        print("EXPLANATION:\n" + row["en_explanation"] + "\n")
        (
            row["en_comprehensiveness"],
            row["en_relevance"],
            row["en_accuracy"],
        ) = get_response()

with open(JSON_FILE, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
