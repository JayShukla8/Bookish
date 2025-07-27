import pandas as pd
import numpy as np

df = pd.read_csv("../datasets/books_with_emotion_scores_02.csv")
default_image = "http://books.google.com/books/content?id=pWsvtQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api&fife=w800"

df["large_thumbnail"] = np.where(
    df["thumbnail"].isna(),
    default_image,
    df["thumbnail"]+"&fife=w800"
)

df.to_csv("books_with_emotion_scores_02.csv", index=False)