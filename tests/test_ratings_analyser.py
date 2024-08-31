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


@pytest.mark.parametrize("feedbacks,expected_mean_value",
                         [([MockFeedback(1), MockFeedback(3)], 2),
                          ([MockFeedback(3), MockFeedback(3)], 3),
                          ([MockFeedback(1), MockFeedback(4)], 2.5)])
def test_get_mean_valid_ratings(feedbacks, expected_mean_value) -> None:
    analyser = RatingsAnalyser(feedbacks)

    assert analyser.get_mean() == expected_mean_value


def test_get_mean_no_ratings() -> None:
    analyser = RatingsAnalyser([])

    assert analyser.get_mean() == None
