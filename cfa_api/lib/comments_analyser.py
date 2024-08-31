"""Comments Analyser module for performing analysis operations on feedback comments"""
from typing import Optional

from lib.keyword_extractor import KeywordExtractor
from schemas.feedback import Feedback


class CommentsAnalyser:
    """Class to perform analysis operations on feedback comments"""
    def __init__(self, feedbacks: list[Feedback]) -> None:
        self.feedbacks = feedbacks

