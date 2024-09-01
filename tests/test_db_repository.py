"""Unit tests for the DBRepository class"""

from unittest.mock import MagicMock

from cfa_api.database.repository import DBRepository


def get_dummy_db():
    return MagicMock()


def test_db_repository_init_successful() -> None:
    dummy_db = get_dummy_db()

    repository = DBRepository(dummy_db)

    assert repository.db == dummy_db


def test_db_repository_add_feedback() -> None:
    dummy_db = get_dummy_db()
    dummy_fedback = "dummy_feedback"

    repository = DBRepository(dummy_db)
    repository.add_feedback(dummy_fedback)

    dummy_db.add_feedback.assert_called_once_with(dummy_fedback)


def test_db_repository_get_feedbacks() -> None:
    dummy_db = get_dummy_db()
    dummy_product_id = "dummy_product_id"

    repository = DBRepository(dummy_db)
    repository.get_feedbacks(dummy_product_id)

    dummy_db.get_feedbacks.assert_called_once_with(dummy_product_id)
