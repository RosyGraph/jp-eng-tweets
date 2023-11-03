import matplotlib.pyplot as plt

from process_reports import load_df


def show_full_barchart():
    df = load_df()

    _, ax = plt.subplots(figsize=(8, 4))

    ax = df.set_index("tweet_index").plot(kind="bar", rot=0, ax=ax)
    ax.set_xlabel("Tweet Index")
    ax.set_ylabel("Score")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()


def show_en_jp_average_scores():
    df = load_df()

    _, ax = plt.subplots(figsize=(8, 4))

    df["en_average"] = df[["en_comprehensiveness", "en_relevance", "en_accuracy"]].mean(
        axis=1
    )
    df["jp_average"] = df[["jp_comprehensiveness", "jp_relevance", "jp_accuracy"]].mean(
        axis=1
    )
    ax = df[["en_average", "jp_average"]].plot(kind="bar", rot=0, ax=ax)
    ax.set_xlabel("Tweet Index")
    ax.set_ylabel("Average Score")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()


show_en_jp_average_scores()
