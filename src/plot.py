from pathlib import Path as P

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

DATA_PATH = P(__file__).parent.parent / "reports" / "tweets_report.json"


def load_df():
    df = pd.read_json(DATA_PATH)
    df["tweet_index"] = df.index
    return df


def show_full_barchart():
    df = load_df()

    _, ax = plt.subplots(figsize=(8, 4))

    ax = df.set_index("tweet_index").plot(kind="bar", rot=0, ax=ax)
    ax.set_xlabel("Tweet Index")
    ax.set_ylabel("Score")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()


def show_avg_by_metric():
    df = load_df()
    df[
        [
            "EN Comprehensiveness",
            "EN Relevance",
            "EN Accuracy",
            "JP Comprehensiveness",
            "JP Relevance",
            "JP Accuracy",
        ]
    ] = df[
        [
            "en_comprehensiveness",
            "en_relevance",
            "en_accuracy",
            "jp_comprehensiveness",
            "jp_relevance",
            "jp_accuracy",
        ]
    ].mean()

    df = df[
        [
            "EN Comprehensiveness",
            "EN Relevance",
            "EN Accuracy",
            "JP Comprehensiveness",
            "JP Relevance",
            "JP Accuracy",
        ]
    ].reset_index()

    df = df.melt(id_vars=["index"], var_name="metric", value_name="value")
    df["language"] = np.where(df["metric"].str.contains("EN"), "English", "Japanese")

    df["metric"] = df["metric"].str.replace("EN ", "").str.replace("JP ", "")

    ax = sns.catplot(
        data=df,
        kind="bar",
        x="metric",
        y="value",
        hue="language",
        ci="sd",
        palette="Paired",
        alpha=0.8,
        height=4,
        aspect=1.5,
    )

    ax.set_axis_labels("", "Score")
    ax.set_xticklabels(rotation=45)

    ax.savefig("reports/figures/avg_by_metric.png", dpi=1000)


def ecdf(data):
    sorted_data = np.sort(data)
    ecdf_values = np.linspace(0, 1, len(sorted_data), endpoint=True)
    return sorted_data, ecdf_values


def show_ecdf():
    df = load_df()

    df["en_average"] = df[["en_comprehensiveness", "en_relevance", "en_accuracy"]].mean(
        axis=1
    )
    df["jp_average"] = df[["jp_comprehensiveness", "jp_relevance", "jp_accuracy"]].mean(
        axis=1
    )

    sns.set_style("whitegrid")
    sns.set_palette("Paired")

    en_series, en_ecdf = ecdf(df["en_average"])
    jp_series, jp_ecdf = ecdf(df["jp_average"])

    fig = plt.figure(figsize=(8, 6))
    plt.step(en_series, en_ecdf, label="English", where="post")
    plt.step(jp_series, jp_ecdf, label="Japanese", where="post")

    plt.xlabel("Average Score")
    plt.ylabel("ECDF")
    plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

    plt.tight_layout()
    fig.savefig("reports/figures/ecdf.png", dpi=1000)


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


show_ecdf()
