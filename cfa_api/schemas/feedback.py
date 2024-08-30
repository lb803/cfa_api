from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

class Feedback(BaseModel):
    """Base model for the Feedback object schema
    
    :todo: Whenever this info would be available, we could
        be more precise when defining types for: `product_id`
        and `comment`.

        I.e.: is `product_id` an hex number? How many digits
        long? Or is it an UUID? Pydantic can help validate that.
    """
    creation_date: datetime

    product_id: str
    rating: PositiveInt = Field(le=5)  #: values from 1 to 5
    comment: Optional[str] = None