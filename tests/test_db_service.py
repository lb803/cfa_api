"""Unit tests for the DBService class"""

from unittest.mock import MagicMock

from cfa_api.database.service import FeedbackService


def get_dummy_repository():
    return MagicMock()


def test_db_service_init_successful() -> None:
    dummy_repository = get_dummy_repository()

    service = FeedbackService(dummy_repository)

    assert service.repository == dummy_repository


def test_db_service_add_feedback() -> None:
    dummy_repository = get_dummy_repository()
    dummy_fedback = "dummy_feedback"

    service = FeedbackService(dummy_repository)
    service.add_feedback(dummy_fedback)

    dummy_repository.add_feedback.assert_called_once_with(dummy_fedback)


def test_db_service_get_feedbacks() -> None:
    dummy_repository = get_dummy_repository()
    dummy_product_id = "dummy_product_id"

    service = FeedbackService(dummy_repository)
    service.get_feedbacks(dummy_product_id)

    dummy_repository.get_feedbacks.assert_called_once_with(dummy_product_id)
