"""Unit Test cases for the Comments Analyzer module"""

import pytest

from cfa_api.lib.comments_analyser import CommentsAnalyser


class MockFeedback:
    def __init__(self, comment: int = "apple pear"):
        self.comment = comment


@pytest.mark.parametrize("feedbacks",
                         [[MockFeedback(), MockFeedback()], []])
def test_comments_analyser_init(feedbacks) -> None:
    analyser = CommentsAnalyser(feedbacks)

    assert analyser.feedbacks == feedbacks