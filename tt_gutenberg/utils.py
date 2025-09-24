import pandas as pd

def load_gutenberg_data():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(url)

def get_alias_translation_counts():
    df = load_gutenberg_data()

    # Keep rows with non-null alias
    df = df.dropna(subset=["alias"])

    # Count how many translations per alias
    counts = (df.groupby("alias")["language"]
                .nunique()
                .sort_values(ascending=False))
    return counts.index.tolist()   # list of aliases ordered by count