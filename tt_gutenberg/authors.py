from .utils import get_alias_translation_counts

def list_authors(by_languages=True, alias=True):
    """
    Return author aliases ordered by number of translations.
    """
    if by_languages and alias:
        return get_alias_translation_counts()
    else:
        raise NotImplementedError("This exercise only covers alias by language count.")