"""Module for the database repository class

This module handles the data access layer to a data source, providing
a generic interface ``Repository`` and an implenentation for databases
``DBRepository``. 
"""

from typing import Protocol

from cfa_api.database.database import Database
from cfa_api.schemas.feedback import Feedback


class Repository(Protocol):
    def add_feedback(self, feedback: Feedback) -> Feedback:
        ...
    
    def get_feedbacks(self, product_id: str) -> list[Feedback]:
        ...


class DBRepository:
    """Data access layer for the database"""
    def __init__(self, db: Database) -> None:
        self.db = db
    
    def add_feedback(self, feedback: Feedback) -> Feedback:
        """Method to add a new feedback record to the database
        
        :param feedback: Feedback to add to the database
        :return: Echo back the added feedback
        """
        return self.db.add_feedback(feedback)
    
    def get_feedbacks(self, product_id: str) -> list[Feedback]:
        """Method to get a list of feedbacks relative to the supplied
        ``product_id``
        
        :param product_id: Product ID of of the feedbacks to get
        :return: A list of feedbacks related to the supplied ``product_id``
        """
        return self.db.get_feedbacks(product_id)
