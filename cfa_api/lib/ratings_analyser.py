"""Ratings Analyser module for performing analysis operations on feedback ratings"""
from statistics import mean, StatisticsError
from typing import Optional

from cfa_api.schemas.feedback import Feedback


class RatingsAnalyser:
    """Class to perform analysis operations on feedback ratings"""
    def __init__(self, feedbacks: list[Feedback]) -> None:
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

    def get_mean(self) -> Optional[float]:
        """Get the mean value of the feedback ratings

        :return: The mean value of the feedback ratings. None if
            the list of feedbacks is empty.
        """
        try:
            mean_value = mean(self.ratings)
        except StatisticsError:
            return None

        return mean_value
