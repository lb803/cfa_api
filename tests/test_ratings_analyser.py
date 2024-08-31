"""Unit test cases for the Ratings Analyser module"""
import pytest

from cfa_api.lib.ratings_analyser import RatingsAnalyser


class MockFeedback:
    def __init__(self, rating: int = 5):
        self.rating = rating


@pytest.mark.parametrize("feedbacks", 
                         [[MockFeedback(), MockFeedback()], []])
def test_ratings_analyser_init_successful(feedbacks) -> None:
    analyser = RatingsAnalyser(feedbacks)

    assert analyser.feedbacks == feedbacks
