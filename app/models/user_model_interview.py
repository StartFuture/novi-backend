from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, EmailStr


class user_preferred_activities(BaseModel):
    relax_on_the_beach_or_by_the_pool: bool
    outdoor_trails_and_walks: bool
    explore_museums_and_historic_sites: bool
    practice_extreme_and_adventure_sports: bool
    try_the_gastronomy_and_go_on_gastronomic_tours: bool