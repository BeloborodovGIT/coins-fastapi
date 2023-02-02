from typing import List

from fastapi import APIRouter, Depends, status

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
    return coins_service.get_many(user)

@router.get('/{coin_id}', response_model=models.Coin)
def get_coin(
    coin_id: int,
    user: models.User = Depends(get_current_user),
    coins_service: CoinsService = Depends()
    ):
    return coins_service.get(user, coin_id)

@router.post('/', response_model=models.Coin)
def create_coin(
    coin_data: models.CreateCoin,
    user: models.User = Depends(get_current_user),
    coins_service: CoinsService = Depends()
    ):
    return coins_service.create(user, coin_data)

@router.put('/{coin_id}', response_model=models.Coin)
def update_coin(
    coin_id: int,
    coin_data: models.UpdateCoin,
    user: models.User = Depends(get_current_user),
    coins_service: CoinsService = Depends()
    ):
    return coins_service.update(user, coin_id, coin_data)

@router.delete('/{coin_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_coin(
    coin_id: int,
    user: models.User = Depends(get_current_user),
    coin_service: CoinsService = Depends()
    ):
    return coin_service.delete(user, coin_id)