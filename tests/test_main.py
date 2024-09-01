"""Test Cases for the ``main.py`` file"""

from typing import Union

from fastapi.testclient import TestClient
import pytest

from cfa_api.main import app
from cfa_api.database.service import FeedbackService

client = TestClient(app)


def get_dummy_feedback() -> dict[str, Union[str, int]]:
    return {
        "creation_date": "2024-01-01T00:00:00",
        "product_id": "123abc",
        "rating": 1,
        "comment": "dummy comment"
        }


def test_add_new_feedback_successful(mocker) -> None:
    mock_feedback = get_dummy_feedback()
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.add_feedback')
    mock_add_feedback.return_value = mock_feedback

    response = client.post("/v1/feedbacks", json=mock_feedback)

    assert response.status_code == 200
    assert response.json() == mock_feedback


def test_add_new_feedback_no_request_body() -> None:
    response = client.post("/v1/feedbacks")

    assert response.status_code == 422


@pytest.mark.parametrize("mock_feedback", ["", "bad_type",
                                           {"product_id": "123abc",
                                            "rating": 1,
                                            "comment": "dummy comment"}])
def test_add_new_feedback_bad_request_body(mock_feedback) -> None:
    response = client.post("/v1/feedbacks", json=mock_feedback)

    assert response.status_code == 422


def test_add_new_feedback_bad_db_response(mocker) -> None:
    mock_feedback = get_dummy_feedback()
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.add_feedback')
    mock_add_feedback.side_effect = TypeError("Dummy error")

    response = client.post("/v1/feedbacks", json=mock_feedback)

    assert response.status_code == 400


def test_get_rating_average_successful(mocker) -> None:
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.get_feedbacks')
    mock_add_feedback.return_value = [get_dummy_feedback()]
    mock_extract_ratings = mocker.patch('cfa_api.main.RatingsAnalyser._extract_ratings')
    mock_extract_ratings.return_value = [1, 2, 3]
    mock_mean = 1.5
    mock_get_mean = mocker.patch('cfa_api.main.RatingsAnalyser.get_mean')
    mock_get_mean.return_value = mock_mean

    response = client.get(f"/v1/feedbacks/ratings/average/{'mock-id'}")

    assert response.status_code == 200
    assert response.json() == mock_mean


def test_get_rating_average_no_product_id_match(mocker) -> None:
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.get_feedbacks')
    mock_add_feedback.return_value = [get_dummy_feedback()]
    mock_extract_ratings = mocker.patch('cfa_api.main.RatingsAnalyser._extract_ratings')
    mock_extract_ratings.return_value = [1, 2, 3]
    mock_get_mean = mocker.patch('cfa_api.main.RatingsAnalyser.get_mean')
    mock_get_mean.return_value = None

    response = client.get(f"/v1/feedbacks/ratings/average/{'mock-id'}")

    assert response.status_code == 404


def test_get_rating_average_no_product_id(mocker) -> None:
    response = client.get(f"/v1/feedbacks/ratings/average/")

    assert response.status_code == 404


def test_get_comments_keywords_successful(mocker) -> None:
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.get_feedbacks')
    mock_add_feedback.return_value = [get_dummy_feedback()]
    mock_extract_ratings = mocker.patch('cfa_api.main.CommentsAnalyser.extract_keywords')
    mock_keywords = ["apple", "plum"]
    mock_extract_ratings.return_value = mock_keywords

    response = client.get(f"/v1/feedbacks/comments/keywords/{'mock-id'}")

    assert response.status_code == 200
    assert response.json() == mock_keywords


def test_get_comments_keywords_no_product_id_match(mocker) -> None:
    mock_add_feedback = mocker.patch('cfa_api.main.FeedbackService.get_feedbacks')
    mock_add_feedback.return_value = [get_dummy_feedback()]
    mock_extract_ratings = mocker.patch('cfa_api.main.CommentsAnalyser.extract_keywords')
    mock_extract_ratings.return_value = None

    response = client.get(f"/v1/feedbacks/comments/keywords/{'mock-id'}")

    assert response.status_code == 404


def test_get_comments_keywords_no_product_id() -> None:
    response = client.get("/v1/feedbacks/comments/keywords/")

    assert response.status_code == 404
