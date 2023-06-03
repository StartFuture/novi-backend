from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_table
from models.models_table import Accomodation, Transport, Tour

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def write_table_data(accommodation: Accomodation, transport: Transport, tour: Tour):

    id_accommodation = dao_table.table_accommodation(
        accommodation= accommodation
    )

    dao_table.table_transport(
        transport= transport,
        id_accommodation= id_accommodation
    )

    dao_table.table_tour(
        tour= tour,
        id_accommodation= id_accommodation
    )

    return JSONResponse(content={"message": "Tables accommodation, trasnport, tour created"})
