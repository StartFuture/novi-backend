from typing import Optional
from datetime import date

from pydantic import BaseModel


class travel_options(BaseModel):
    travel_destination: int
    travel_style: int
    acommodation_style: int
    night_style: int
    can_leave_country: bool
    transport_style: int


class travel_activities(BaseModel):
    water_preference: int
    walk_preference: int
    historic_preference: int
    sport_preference: int
    food_preference: int


class travel_cultures(BaseModel):
    music_preference: int
    building_preference: int
    tradicion_preference: int
    party_preference: int
    no_preference: bool
    

class weather_option(BaseModel):
    warm: int
    mild: int
    cold: int
    no_preference: bool