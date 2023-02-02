from typing import List

from fastapi import APIRouter, Depends, status

from .. import models

from ..services.auth import get_current_user
from ..services.collections import CollectionsService


router = APIRouter(
    prefix='/collections',
    tags=['collections'],
)

@router.get('/', response_model=List[models.Collection])
def get_collections(
        user: models.User = Depends(get_current_user),
        collections_service: CollectionsService = Depends()
    ):
    return collections_service.get_many(user)

@router.get('/{collection_id}', response_model=models.Collection)
def get_collections(
        collection_id: int,
        user: models.User = Depends(get_current_user),
        collections_service: CollectionsService = Depends()
    ):
    return collections_service.get(user, collection_id)

@router.post('/', response_model=models.Collection)
def create_collection(
    collection_data: models.CollectionCreate,
    user: models.User = Depends(get_current_user),
    collections_service: CollectionsService = Depends()
    ):
    return collections_service.create(user, collection_data)

@router.post(
    '/{collection_id}', 
    response_model=models.Collection, 
    status_code=status.HTTP_201_CREATED
    )
def append_to_collections(
    collection_id: int,
    coin_data: models.CollectionAppend,
    user: models.User = Depends(get_current_user),
    collection_service: CollectionsService = Depends()
    ):
    return collection_service.add(user, collection_id, coin_data.coin_id)

@router.get('/{collection_id}/import')
def import_collection(
    collection_id: int,
    user: models.User = Depends(get_current_user),
    collection_service: CollectionsService = Depends()
    ):
    return {'message': 'i`m teapot'}