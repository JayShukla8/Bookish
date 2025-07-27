import pandas as pd

df = pd.read_csv("../datasets/books_with_emotion_scores.csv")

df["Adventure"] = 0.4 * df["fear"] + 0.3 * df["surprise"] + 0.3 * df["joy"]
df["Comedy"] = 0.7 * df["joy"] + 0.3 * df["surprise"]
df["Horror"] = 0.5 * df["fear"] + 0.3 * df["disgust"] + 0.2 * df["anger"]
df["Romance"] = 0.6 * df["joy"] + 0.4 * df["sadness"]
df["Thriller"] = 0.5 * df["fear"] + 0.5 * df["surprise"]

df.to_csv("books_with_emotion_scores_02.csv", index=False)