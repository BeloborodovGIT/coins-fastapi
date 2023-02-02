from typing import List, Optional
from fastapi import Depends, HTTPException, status

from ...database import *

from ... import models


class CoinsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self, user: models.User) -> List[Coins]:
        if user.role == RoleENUM.USER:
            coins: List[Coins] = (self.session.
                query(Coins)
                .filter(Coins.owner_id == user.id)
            ).all()
        else:
            coins: List[Coins] = (self.session.
                query(Coins)
            ).all()

        return coins

    def get(
        self,
        user: models.User,
        coin_id: int
    ) -> Coins:
        coin = self._get(user, coin_id)
        return coin

    async def create_many(
        self,
        user: models.User,
        coins_data: List[models.CreateCoin],
    ) -> List[Coins]:
        coins = [
            Coins(
                **coin_data.dict(),
                user_id=user.id,
            )
            for coin_data in coins_data
        ]
        self.session.add_all(coins)
        await self.session.commit()
        return coins

    def create(
        self,
        user: models.User,
        coin_data: models.CreateCoin,
    ) -> Coins:
        coin = Coins(
            **coin_data.dict(),
            owner_id=user.id,
        )
        self.session.add(coin)
        self.session.commit()
        return coin

    def update(
        self,
        user: models.User,
        coin_id: int,
        coin_data: models.UpdateCoin,
    ) -> Coins:
        coin = self._get(user, coin_id)
        for field, value in coin_data:
            setattr(coin, field, value)
        self.session.commit()
        return coin

    def delete(
        self,
        user: models.User,
        coin_id: int,
    ):
        coin = self._get(user, coin_id)
        self.session.delete(coin)
        self.session.commit()

    def _get(self, user: models.User, coin_id: int) -> Optional[Coins]:
        if user.role == RoleENUM.ADMIN:
            coin: Coins = (self.session
                .query(Coins)
                .filter(
                    Coins.id == coin_id
                )
                .first())
        else:
            coin: Coins = (self.session
                .query(Coins)
                .filter(
                    Coins.owner_id == user.id,
                    Coins.id == coin_id
                )
                .first())
        if not coin:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return coin