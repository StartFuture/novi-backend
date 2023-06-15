from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

class Travel(BaseModel):
    id_accommodation: int
    id_transport_from: int
    id_transport_return: int
    date_from: str
    date_return: Optional[str] = Field(None)
    quantity_people: int
    price: float
    id_tour: int
from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

class Travel(BaseModel):
    id_accommodation: int
    id_transport_from: int
    id_transport_return: int
    date_from: str
    date_return: Optional[str] = Field(None)
    quantity_people: int
    price: float
    id_tour: int

