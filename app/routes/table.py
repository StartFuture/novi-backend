from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_table
from models.models_table import Accomodation, Transport, Tour

router = APIRouter()

@router.post("/accommodation", status_code=status.HTTP_201_CREATED)
def write_table_accommodation(accommodation: Accomodation):

    id_accommodation = dao_table.table_accommodation(
        accommodation= accommodation
    )

    id_accommodation = id_accommodation['LAST_INSERT_ID()']

    return JSONResponse(content={"id_accommodation": id_accommodation})

@router.post("/transport", status_code=status.HTTP_201_CREATED)
def write_table_transport(id_accommodation: int, transport: Transport):

    dao_table.table_transport(
        id_accommodation= id_accommodation,      
        transport= transport
    )
    
    return JSONResponse(content={"message": "Table transport created"})

@router.post("/tour", status_code=status.HTTP_201_CREATED)
def write_table_tour(id_accommodation: int, tour: Tour):

    dao_table.table_tour(
        id_accommodation= id_accommodation,
        tour= tour
    )

    return JSONResponse(content={"message": "Table tour created"})