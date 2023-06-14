from pydantic import BaseModel

class Accomodation(BaseModel):
    travel_destination: int
    travel_style: int
    accommodation_style: int
    is_country: bool
    warn: int
    mild: int
    cold: int
    price: float
    details: str
    local_name: str


class Transport(BaseModel):
    details: str
    price: float
    transport_style: int


class Tour(BaseModel):
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
    price: float
    details: str
