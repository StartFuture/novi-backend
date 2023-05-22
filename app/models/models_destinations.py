from typing import Optional

from pydantic import BaseModel, Field

#Modelo de entrada de destinos
class Destination(BaseModel):
    continent: str
    country: str
    state_destination: str = Field(regex=r'^[A-Z]{2}$')
    city: str
    journey: str

class UpdateDestination(BaseModel):
    continent: Optional[str] = None
    country: Optional[str] = None
    state_destination: Optional[str] = Field(None, regex=r'^[A-Z]{2}$')
    city: Optional[str] =  None
    journey: Optional[str] = None
