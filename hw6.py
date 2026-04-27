"""
Vince Duarte
Section Leader: Tingting Thompson
April 26, 2026
ISTA 131 Hw6
This module loads tweet text data from JSON files, performs sentiment
analysis using TextBlob, summarizes the results in a pandas DataFrame,
and creates a grouped bar chart with error bars.
"""
import json
import statistics
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_sentiment(filename):
    """
    Analyze tweet sentiment from a JSON file.
    Opens a JSON file containing a list of tweet text strings. Uses
    TextBlob sentiment analysis on each tweet. Tweets with both
    polarity and subjectivity equal to 0.0 are ignored.
    Parameters:
        filename (str): Name of JSON file containing tweet texts.
    Returns:
        list: [mean polarity, sample standard deviation polarity]
    """
    with open(filename, "r") as file:
        tweets = json.load(file)
    polarities = []
    for tweet in tweets:
        sentiment = TextBlob(tweet).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        if not (polarity == 0.0 and subjectivity == 0.0):
            polarities.append(polarity)
    mean_val = statistics.mean(polarities)
    std_val = statistics.stdev(polarities)
    return [mean_val, std_val]

def get_ct_sentiment_frame():
    files = {
        "Trump": ["data/trump_231005_730am.json", "data/trump_231006_330pm.json"],
        "Biden": ["data/biden_231005_730am.json", "data/biden_231006_330pm.json"]
    }
    data = {}
    for candidate in files:
        day1 = get_sentiment(files[candidate][0])
        day2 = get_sentiment(files[candidate][1])
        data[candidate] = [
            day1[0], day1[1],
            day2[0], day2[1]
        ]
    frame = pd.DataFrame(
        data,
        index=["10/5 mean", "10/5 std", "10/6 mean", "10/6 std"]
    ).T
    return frame

def make_fig(sentiment_frame):
    fig, ax = plt.subplots(figsize=(10, 7))
    candidates = sentiment_frame.index
    x = np.arange(len(candidates))
    width = 0.35

    day1_means = sentiment_frame["10/5 mean"]
    day1_sd = sentiment_frame["10/5 std"]
    day2_means = sentiment_frame["10/6 mean"]
    day2_sd = sentiment_frame["10/6 std"]

    ax.bar(
        x - width / 2,
        day1_means,
        width,
        yerr=day1_sd,
        capsize=6,
        color="royalblue",
        label="10/5"
    )
    ax.bar(
        x + width / 2,
        day2_means,
        width,
        yerr=day2_sd,
        capsize=6,
        color="firebrick",
        label="10/6"
    )
    ax.set_xticks(x)
    ax.set_xticklabels(candidates, fontsize=18, color="white")
    ax.tick_params(axis="y", labelsize=18, colors="white")
    ax.set_ylabel("Mean Polarity", fontsize=24, color="white")
    ax.set_facecolor("#2d2d2d")
    fig.patch.set_facecolor("black")
    for spine in ax.spines.values():
        spine.set_color("white")
    ax.legend()
    return fig
def main():
    """
    Run full program:
    print sentiment frame, make figure, display chart.
    """
    # DEBUG - check pickle index and columns
    correct = pd.read_pickle("test_data/sm.pkl")
    print("Expected index:", correct.index.tolist())
    print("Expected columns:", correct.columns.tolist())
    print(correct)

    frame = get_ct_sentiment_frame()
    print()
    print(frame)
    fig = make_fig(frame)
    plt.show()

if __name__ == "__main__":
    main()