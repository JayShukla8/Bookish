import pandas as pd


def display_books(
        df: pd.DataFrame
) -> list:
    results = []
    for index, row in df.iterrows():
        # get the description
        description = row["description"]
        # desc_split = description.split()
        # description = " ".join(desc_split[:30]) + '...'
        # get the author names
        authors_split = row["authors"].split(';')
        if len(authors_split) == 2:
            authors_list = f"{authors_split[0] and authors_split[1]}"
        elif len(authors_split) > 2:
            authors_list = f"{', '.join(authors_split[:-1])} and {authors_split[-1]}"
        else:
            authors_list = row["authors"]
        caption = f"<b>{row['title']}</b><br> by {authors_list}"
        results.append((row["large_thumbnail"], caption, description))
    return results