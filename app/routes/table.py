from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_table
from models.models_table import Accomodation, Transport, Tour

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def table_