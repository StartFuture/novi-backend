from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_table
from models.models_table import Table
from utils import get_user_id

router = APIRouter()