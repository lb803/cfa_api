from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

class Feedback(BaseModel):
    """Base model for the Feedback object schema"""
    creation_date: datetime

    product_id: str
    rating: PositiveInt = Field(le=5)  #: values from 1 to 5
    comment: Optional[str] = None