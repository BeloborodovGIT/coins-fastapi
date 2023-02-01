from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from ...database import *
from .. import DatabaseService

from ... import models


class CoinsService(DatabaseService):
    def __init__(self, session: Session = Depends(session_factory)):
        self.session = session

    async def get_many(self, user_id: int) -> List[Coins]:
        coins = (await self.session
            .query(Coins)
            .filter(Coins.owner_id == user_id)
            .order_by(
                Coins.id.desc()
            )).all()
        return coins

    async def get(
        self,
        user_id: int,
        coin_id: int
    ) -> Coins:
        coin = self._get(user_id, coin_id)
        return coin

    async def create_many(
        self,
        user_id: int,
        coins_data: List[models.CreateCoin],
    ) -> List[Coins]:
        coins = [
            Coins(
                **coin_data.dict(),
                user_id=user_id,
            )
            for coin_data in coins_data
        ]
        await self.session.add_all(coins)
        await self.session.commit()
        return coins

    async def create(
        self,
        user_id: int,
        coin_data: models.CreateCoin,
    ) -> Coins:
        coin = Coins(
            **coin_data.dict(),
            user_id=user_id,
        )
        await self.session.add(coin)
        await self.session.commit()
        return coin

    async def update(
        self,
        user_id: int,
        coin_id: int,
        coin_data: models.UpdateCoin,
    ) -> Coins:
        coin = await self._get(user_id, coin_id)
        for field, value in coin_data:
            setattr(coin, field, value)
        await self.session.commit()
        return coin

    async def delete(
        self,
        user_id: int,
        coin_id: int,
    ):
        coin = self._get(user_id, coin_id)
        await self.session.delete(coin)
        await self.session.commit()

    async def _get(self, user_id: int, coin_id: int) -> Optional[Coins]:
        coin: Coins = (
            await self.session
            .query(Coins)
            .filter(
                Coins.owner_id == user_id,
                Coins.id == coin_id
            )
            .first()
        ).c
        if not coin:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        else:
            coin = (
                await self.session
                .query(Coins)
                .filter(
                    Coins.id == coin_id
                )
                .first()
            )
        return coin