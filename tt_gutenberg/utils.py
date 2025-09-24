# Import the data from gutenberg project

import pandas as pd
def load_authors():
    '''Load authors data as data frame'''
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(url)



def load_languages():
    '''Load languages data as data frame'''
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_languages.csv"
    return pd.read_csv(url)


def load_metadata():
    '''Load metadata data as data frame'''
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    return pd.read_csv(url)
