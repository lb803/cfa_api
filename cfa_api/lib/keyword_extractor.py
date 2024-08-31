"""Keyword Extractor module to extract keywords from strings

I expect this module to change a lot over time (new AI models,
better libraries etc) so this module offers a KeywordExtractor
interface which we can use to add new extractors.
"""

from collections import Counter
from typing import Protocol


class KeywordExtractor(Protocol):
    def extract_keywords(self, text: str, limit: int) -> list[str]:
        """Extract keywords from text strings
        
        :param text: Text to analyse.
        :param limit: Max number of words to return.
        """
        ...


class BonkersKeywordExtractor:
    """This is just a stub! Likely to return ["the", "a", "of"] and
    to have hiccups with punctuation.
    
    To be used to demo.
    """
    def extract_keywords(self, text: str, limit: int) -> list[str]:
        """Extract keywords from text strings

        :param text: Text to analyse.
        :param limit: Max number of words to return.
        """
        words = text.split()
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(limit)
    
        return [keyword for keyword, _ in most_common_words]
