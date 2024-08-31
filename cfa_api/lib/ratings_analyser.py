"""Ratings Analyser module for performing analysis operations on feedback ratings"""
from statistics import mean, StatisticsError
from typing import Optional

from schemas.feedback import Feedback


class RatingsAnalyser:
    def __init__(self, feedbacks: list[Feedback]) -> None:
        """Class to perform analysis operations on feedback ratings"""
        self.feedbacks = feedbacks

        self.ratings = self._extract_ratings()
    
    def _extract_ratings(self, feedback_samples: list[Feedback] = None) -> list[int]:
        """Helper function to extract rating values
        
        :param feedback_sample: Optional parameter to specify a (subset)
            sample of feedbacks. Defaults to self.feedbacks of the 
            object instance.
        :return: A list with the rating values.
        """
        if feedback_samples is None:
            feedback_samples = self.feedbacks

        return [feedback.rating for feedback in feedback_samples]

