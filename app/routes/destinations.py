from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_destination
from models.models_destinations import Destination, UpdateDestination
import utils

router = APIRouter()


# Criar linha de destino
@router.post('/create_destination', status_code=status.HTTP_201_CREATED)
async def write_data(destination: Destination):
    
    verify_data = await dao_destination.verify_duplicated_data(destination)

    print(verify_data)

    if verify_data:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Cannot create destination. Destination alredy exist")
    

    print(destination.continent)
    message = await dao_destination.write_data_destination(
        destination
    )

    return JSONResponse(content=message)


# Select da linha de destino criada
@router.get('/{id_destination}', status_code=status.HTTP_200_OK)
async def read_data(id_destination: int):
    
    query_destination, result = await dao_destination.select_data_destination(id_destination)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Destination not found")
    
    return JSONResponse(content=query_destination)


# Updata da linha de destino
@router.patch('/update_destination/{id_destination}', status_code=status.HTTP_200_OK)
async def update_data(id_destination: int, destination: UpdateDestination):
    
    verify_id = await dao_destination.verify_id_destination(id_destination)
    print(verify_id)

    if not verify_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Cannot Update Destination. Destination Not Found")


    update_destination, message = await dao_destination.update_data_destination(
        id_destination= id_destination,
        destination= destination
    )
    if not update_destination:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Nothing to change")

    return JSONResponse(content=message)



# Delete da linha de destino
@router.delete('/delete_destination', status_code=status.HTTP_200_OK)
async def delete_data(id_destination: int):

    verify_id = await dao_destination.verify_id_destination(id_destination)

    if not verify_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Cannot Delete Destination. Destination Not Found")

    message = await dao_destination.delete_data_destination(
        id_destination= id_destination
    )
    print(message)

    return JSONResponse(content=message)
