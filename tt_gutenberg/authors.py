import pandas as pd
from .utils import load_authors, load_metadata



def list_authors(by_languages = True, alias = True):
    '''Function to list authors in order of translation count'''

    #Load Data
    meta = load_metadata()
    authors = load_authors()[['gutenberg_author_id' , 'author' , 'alias']]
   

    # Keep required columns
    req_cols = meta[['gutenberg_author_id' , 'language']].drop_duplicates()

    # Count languages per author
    author_count = (
        req_cols.groupby('gutenberg_author_id')
                    .size()
                    .reset_index(name = 'language_count')
                    )

    # Merge author and alias
    df = author_count.merge(authors, on = 'gutenberg_author_id' , how = 'left')
    df = df.sort_values('language_count' , ascending = False, kind = 'mergesort')

    # Return required columns
    name_col = 'alias' if alias else 'author'
    fin_col = df[name_col]
    name_col = 'alias' if alias else 'author'
    mask = df[name_col].notna() & (df[name_col].str.strip() != '') & (df[name_col].str.upper() != 'NA')
    
    return df.loc[mask, name_col].tolist()




