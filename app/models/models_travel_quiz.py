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


class travel_information(BaseModel):
    travel_destination: int
    travel_style: int
    accommodation_style: int
    is_country: bool
    warm: int
    mild: int
    cold: int
    price: int
    details: str
    local_name: str


class tours_information(BaseModel):
    night_style: int
    music_preference: int
    building_preference: int
    tradicion_preference: int
    party_preference: int
    water_preference: int
    walk_preference: int
    historic_preference: int
    sport_preference: int
    food_preference: int
    price: int
    details: str


class transport_information(BaseModel):
    details: str
    price: str
    transport_style: int