"""Unit Test cases for the Comments Analyzer module"""

import pytest

from cfa_api.lib.comments_analyser import CommentsAnalyser


class MockFeedback:
    def __init__(self, comment: int = "apple pear") -> None:
        self.comment = comment


class MockKeyworkExtractor:
    def extract_keywords(*args, **kwargs) -> list[str]:
        return ["all", "good"]


@pytest.mark.parametrize("feedbacks",
                         [[MockFeedback(), MockFeedback()], []])
def test_comments_analyser_init(feedbacks) -> None:
    analyser = CommentsAnalyser(feedbacks)

    assert analyser.feedbacks == feedbacks


def test_comments_analyser_extract_keywords() -> None:
    analyser = CommentsAnalyser([])
    words = analyser.extract_keywords(MockKeyworkExtractor(), 5)

    assert words == ["all", "good"]
