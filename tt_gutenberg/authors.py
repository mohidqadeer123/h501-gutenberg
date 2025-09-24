import pandas as pd
from .utils import load_authors, load_metadata



def list_authors(by_languages = True, alias - True):
    '''Function to list authors in order of translation count'''

    #Load Data
    authors = load_authors()[['gutenber_author_id' , 'author' , 'alias']]
    meta = load_metadata

    # Keep required columns
    req_cols = meta[['gutenber_author_id' , 'language']].drop_duplicates()

    # Count languages per author
    author_count = (req_cols.groupby('gutenberg_author_id').size().reset_index(name = 'lang_count'))

    # Merge author and alias
    df = req_cols.merge(authors, on = 'guteneberg_author_id' , how = 'left')
    df = df.sort_values('language_count' , ascending = False, kind = 'mergesoft')

    # Return required columns
    name_col = 'alias' if alias else 'author'
    fin_col = df[name_col]
    mask = name_col.notna() & (name_col.str.strip() != '') & (name_col.str.upper() != 'NA')
    return fin_col[mask].tolist()
    




