from pathlib import Path as P

from pyperclip import copy

JP_PROMPT = (
    "Produce an explanation in Japanese of following Tweet from Twitter user @elonmusk."
)
ENG_PROMPT = "Produce an explanation of following Tweet from Twitter user @elonmusk."
REPORTS_DIR = P(__file__).parent.parent / "reports"

tweets = """First picture of SpaceX spacesuit. More in days to follow. Worth noting that this actually works…  https://t.co/5ZtqkKiTQX
When searching for parking, the car reads the signs to see if it is allowed to park there, which is why it skipped the disabled spot
Will post video of a Tesla navigating a complex urban environment shortly. That was what took the extra couple of days.
Designing a rocket part w hand gestures &amp; then 3D printing it in a metal superalloy ...  http://t.co/h3KoyAb0Lt
Still working on the Falcon fireball investigation. Turning out to be the most difficult and complex failure we have ever had in 14 years.
Also dig Mass Effect. It's all fun & games until the AI decides people suck. Maybe we can be their limbic system.
Dragon floating in the Pacific near California. Reentry scorch marks visible on the heat shield  http://t.co/grGShZUi
Glad to contribute to the Tesla museum and will do more in the future. He was a great man.  http://t.co/NR2QNiax
Paid respects to Masada earlier today. Live free or die.  https://t.co/RIfSVHRkDY
With my team after a profoundly interesting discussion of history, philosophy &amp; luck with Vice President Wang in 中南海紫光阁  https://t.co/pHd52YTZD2""".split(
    "\n"
)

for i, s in enumerate(tweets):
    with open(REPORTS_DIR / "tweets.txt", "a") as f:
        f.write(s + "\n")
    print(f"Tweet {i+1} written to file")
    copy(f"{JP_PROMPT}\n\n{s}")
    print("JP prompt copied")
    input("Press Enter to continue...")
    copy(f"{ENG_PROMPT}\n\n{s}")
    print("ENG prompt copied")
    input("Press Enter to continue...")
