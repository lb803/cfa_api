"""Database service module

This module implements the business logic to perform data
operation on the repository.
"""

from cfa_api.database.repository import Repository
from cfa_api.schemas.feedback import Feedback


class FeedbackService:
    """Class to perform data operations on the repository"""
    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    def add_feedback(self, feedback: Feedback) -> Feedback:
        """Method to add a new feedback record to the database
        
        :param feedback: Feedback to add to the database
        :return: Echo back the added feedback
        """
        return self.repository.add_feedback(feedback)
    
    def get_feedbacks(self, product_id: str) -> list[Feedback]:
        """Method to get a list of feedbacks relative to the supplied
        ``product_id``
        
        :param product_id: Product ID of of the feedbacks to get
        :return: A list of feedbacks related to the supplied ``product_id``
        """
        return self.repository.get_feedbacks(product_id)