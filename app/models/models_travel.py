from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

class Travel(BaseModel):
    date_from: str
    date_return: Optional[str] = Field(None)
    quantity_people: int
    price: float
