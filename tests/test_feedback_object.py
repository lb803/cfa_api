"""Unit tests for the Feedback object schema"""
from datetime import datetime
from typing import Union

from pydantic import ValidationError
import pytest

from cfa_api.schemas.feedback import Feedback


def create_feedback(creation_date: Union[str, datetime],
                product_id:str, rating: int,
                comment: str) -> Feedback:
    """Helper function to create a Feedback instance"""
    feedback = Feedback(
        creation_date=creation_date,
        product_id=product_id,
        rating=rating,
        comment=comment
    )
    return feedback

@pytest.mark.parametrize("creation_date,product_id,rating,comment",
                         [("2024-01-01T00:00:00", "123abc", 1, "dummy comment"),
                          ("2024-01-01T00:00:00", "123abc", 1, None)])
def test_init_correct(creation_date, product_id, rating, comment) -> None:
    feedback = create_feedback(creation_date, product_id, rating, comment)

    assert feedback.creation_date == datetime.strptime(creation_date,
                                                       "%Y-%m-%dT%H:%M:%S")
    assert feedback.product_id == product_id
    assert feedback.rating == rating
    assert feedback.comment == comment


# Test creation_date
@pytest.mark.parametrize("allowed_creation_date_value",
                         ["2024-01-01T00:00:00", datetime.now()])
def test_allowed_creation_date_values(allowed_creation_date_value):
    feedback = create_feedback(allowed_creation_date_value, "123abc",
                               1, "dummy comment")

    if isinstance(allowed_creation_date_value, datetime):
        assert feedback.creation_date == allowed_creation_date_value
    else:
        assert feedback.creation_date == datetime. \
            strptime(allowed_creation_date_value, "%Y-%m-%dT%H:%M:%S")


@pytest.mark.parametrize("not_allowed_creation_date_value",
                         ["2024/01/01 at 00:00:00", "now", ["now"],
                          {"creation_date": "2024-01-01T00:00:00"}])
def test_creation_date_not_allowed_values(not_allowed_creation_date_value):
    with pytest.raises(ValidationError):
        _ = create_feedback(not_allowed_creation_date_value, "123abc",
                            1, "dummy comment")


# Test product_id
@pytest.mark.parametrize("allowed_product_id_value",
                         "dummy product id")
def test_product_id_allowed_values(allowed_product_id_value):
    feedback = create_feedback("2024-01-01T00:00:00", allowed_product_id_value,
                               1, comment="dummy comment")

    assert feedback.product_id == allowed_product_id_value


@pytest.mark.parametrize("not_allowed_product_id_value",
                         [["dummy product id"], {"id": "dummy product id"}])
def test_product_id_not_allowed_values(not_allowed_product_id_value):
    with pytest.raises(ValidationError):
        _ = create_feedback("2024-01-01T00:00:00", not_allowed_product_id_value,
                            1, comment="dummy comment")


# Test rating
@pytest.mark.parametrize("allowed_rating_value", [n for n in range(1, 6)])
def test_rating_allowed_values(allowed_rating_value):
    feedback = create_feedback("2024-01-01T00:00:00", "123abc",
                               allowed_rating_value, "dummy comment")

    assert feedback.rating == allowed_rating_value


@pytest.mark.parametrize("not_allowed_rating_value",
                         [n for n in range(-1, 7) if n not in range(1, 6)] + \
                         ["one", ["one"], {"rating": 1}])
def test_rating_not_allowed_values(not_allowed_rating_value):
    with pytest.raises(ValidationError):
        _ = create_feedback("2024-01-01T00:00:00", "123abc",
                            not_allowed_rating_value, "dummy comment")


# Test comment
@pytest.mark.parametrize("allowed_comment_value", "dummy comment")
def test_comment_allowed_values(allowed_comment_value):
    feedback = create_feedback("2024-01-01T00:00:00", "123abc",
                               1, allowed_comment_value)

    assert feedback.comment == allowed_comment_value


@pytest.mark.parametrize("not_allowed_comment_value",
                         [["dummy comment"], {"comment": "dummy comment"}])
def test_comment_not_allowed_values(not_allowed_comment_value):
    with pytest.raises(ValidationError):
        _ = create_feedback("2024-01-01T00:00:00", "123abc",
                            1, not_allowed_comment_value)
