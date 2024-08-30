"""Unit tests for the Feedback object schema"""
from datetime import datetime
from typing import Union

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
