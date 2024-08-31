"""Comments Analyser module for performing analysis operations on feedback comments"""
from typing import Optional

from lib.keyword_extractor import KeywordExtractor
from schemas.feedback import Feedback


class CommentsAnalyser:
    """Class to perform analysis operations on feedback comments"""
    def __init__(self, feedbacks: list[Feedback]) -> None:
        self.feedbacks = feedbacks
    
    def extract_keywords(self, extractor: KeywordExtractor,
                         limit: int = 5) -> Optional[list[str]]:
        """Method to extract keywords from comments
        
        :param extractor: KeywordExtractor (sub)class to use to perform the
            keyword extraction.
        :param limit: Max number of words to extract
        """
        comments = ' '.join(feedback.comment for feedback in self.feedbacks \
                            if feedback.comment is not None)
        return extractor.extract_keywords(comments, limit)
