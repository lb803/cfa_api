"""Unit test cases for the FakeDB class"""
from unittest.mock import MagicMock
import pytest

from cfa_api.database.database import FakeDB
from cfa_api.schemas.feedback import Feedback


def test_fakedb_init() -> None:
    db = FakeDB()

    assert db.feedbacks == []


def test_fakedb_add_feedback_valid() -> None:
    db = FakeDB()
    feedback = MagicMock(spec=Feedback)
    return_value = db.add_feedback(feedback)

    assert db.feedbacks == [feedback]
    assert return_value == feedback


def test_fakedb_add_feedback_bad_feedback_type() -> None:
    db = FakeDB()
    with pytest.raises(TypeError):
        _ = db.add_feedback("bad_feedback_type")


def test_fakedb_get_feedbacks() -> None:
    feedback = MagicMock(spec=Feedback)
    feedback.product_id = "dummy_id"

    db = FakeDB()
    db.feedbacks = [feedback]
    result = db.get_feedbacks("dummy_id")

    assert result == [feedback]


def test_fakedb_get_feedbacks_no_results() -> None:
    feedback = MagicMock(spec=Feedback)
    feedback.product_id = "dummy_id"

    db = FakeDB()
    db.feedbacks = [feedback]
    result = db.get_feedbacks("bad_dummy_id")

    assert result == []
