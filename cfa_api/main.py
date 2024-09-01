"""Customer Feedback Analysis API endpoints"""

from fastapi import FastAPI, HTTPException

from cfa_api.database.database import FakeDB
from cfa_api.database.repository import DBRepository
from cfa_api.database.service import FeedbackService
from cfa_api.lib.comments_analyser import CommentsAnalyser
from cfa_api.lib.keyword_extractor import BonkersKeywordExtractor
from cfa_api.lib.ratings_analyser import RatingsAnalyser
from cfa_api.schemas.feedback import Feedback


app = FastAPI()

# Data handling
db = FakeDB()
repository = DBRepository(db)
feedback_service = FeedbackService(repository)

# Keywords extractor processor
keyword_extractor = BonkersKeywordExtractor()


@app.post("/v1/feedbacks")
def add_new_feedback(feedback: Feedback) -> Feedback:
    try:
        returned_feedback = feedback_service.add_feedback(feedback)
    except(TypeError):
        error_message = f"Expected feedback to be an instance of " + \
                        f"Feedback: {feedback}"
        raise HTTPException(status_code=400, detail=error_message)
    
    return returned_feedback


@app.get("/v1/feedbacks/ratings/average/{product_id}")
def get_rating_average(product_id: str) -> float:
    feedbacks = feedback_service.get_feedbacks(product_id)

    ratings_analyser = RatingsAnalyser(feedbacks)
    mean = ratings_analyser.get_mean()

    if mean is None:
        error_message = f"No feedback found with the product_id: {product_id}"
        raise HTTPException(status_code=404, detail=error_message)
    
    return mean


@app.get("/v1/feedbacks/comments/keywords/{product_id}")
def get_comments_keywords(product_id: str) -> list[str]:
    feedbacks = feedback_service.get_feedbacks(product_id)

    comments_analyser = CommentsAnalyser(feedbacks)
    keywords = comments_analyser.extract_keywords(extractor=keyword_extractor)

    if keywords is None:
        error_message = f"No feedback comments found with the " + \
                        f"product_id: {product_id}"
        raise HTTPException(status_code=404, detail=error_message)
    
    return keywords