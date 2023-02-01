from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from .. import models

from ..services.auth import get_current_user
from ..services.coins import CoinsService


router = APIRouter(
    prefix='/coins',
    tags=['coins'],
)

@router.get('/', response_model=List[models.Coin])
def get_coins(
    user: models.User = Depends(get_current_user),
    coins_service: CoinsService = Depends()
    ):
    return coins_service.get_many(user.id)