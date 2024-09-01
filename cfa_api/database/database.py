"""Module for the database class

This module also might be subject to change. I am creating
the interface Database for the new classes to be added in
the future.
"""

from typing import Protocol

from cfa_api.schemas.feedback import Feedback


class Database(Protocol):
    def add_feedback(self, feedback: Feedback) -> Feedback:
        """Method to add a new feedback to the database
        
        :param feedback: feedback to be added
        :return: echo back the added feedback
        """
        ...

    def get_feedbacks(self, product_id: str) -> list[Feedback]:
        """Get a list of feedbacks relative to the specified
        ``product_id``
        
        :param product_id: ``product_id`` of the feedbacks to get
        :return: A list of the requested feedbacks
        """
        ...


class FakeDB():
    """This is a stub database which tries to behave like a real one"""
    def __init__(self) -> None:
        self.feedbacks: list[Feedback] = []
    
    def add_feedback(self, feedback: Feedback) -> Feedback:
        """Method to add a new feedback to the database
        
        :raise TypeError: Error raised if an invalid feedback type is
            supplied
        :param feedback: feedback to be added
        :return: echo back the added feedback
        """
        if not isinstance(feedback, Feedback):
            raise TypeError("Expected feedback to be an instance of Feedback")
        
        self.feedbacks.append(feedback)

        return feedback
    
    def get_feedbacks(self, product_id: str) -> list[Feedback]:
        """Get a list of feedbacks relative to the specified
        ``product_id``
        
        :param product_id: ``product_id`` of the feedbacks to get
        :return: A list of the requested feedbacks
        """
        return [feedback for feedback in self.feedbacks \
                if feedback.product_id == product_id]