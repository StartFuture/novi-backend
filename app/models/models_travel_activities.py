from typing import Optional
from datetime import date

from pydantic import BaseModel


class travel_activities(BaseModel):
    water_preference: int
    walk_preference: int
    historic_preference: int
    sport_preference: int
    food_preference: int