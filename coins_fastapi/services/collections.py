from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import selectinload

from ..database import *

from .. import models


class CollectionsService:

    @staticmethod
    def append_dict(dict_: dict, key: str, value) -> dict:
        if not (key in dict_):
            dict_[key] = value
        return dict_
    
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self, user: models.User) -> List[Collections]:
        collections: List[Collections] = (
            self.session
            .query(Collections)
            .all()
        )

        return collections

    def get(
        self,
        user: models.User,
        collection_id: int
    ) -> Collections:
        collection = self._get(user, collection_id)
        return collection

    def add(
        self, 
        user: models.User,
        collection_id: int,
        coin_id: int
        ) -> Collections:
        
        link: LinkCoinsToCollections = LinkCoinsToCollections(
            collection_id=collection_id,
            coin_id=coin_id
            )

        self.session.add(link)
        self.session.commit()

        collection_link = (
            self.session
            .query(LinkCoinsToCollections)
            .join(Collections)
            .join(Coins)
            .filter(Collections.id == collection_id)
            .all()
        )

        coins_dict = {}

        for i in collection_link:
            coin_info = {c.name: str(getattr(i, c.name)) for c in i.__table__.columns}
            del coin_info['id']
            self.append_dict(coins_dict, i.coin.id, coin_info)

        collection = (
            self.session
            .query(Collections)
            .filter(Collections.id == collection_id)
            .first()
        )
        
        return models.Collection(**collection.__dict__, coins_list=coins_dict)

    def create(
        self,
        user: models.User,
        collection_data: models.CollectionCreate,
    ) -> Collections:
        collection = Collections(
            **collection_data.dict()
        )
        self.session.add(collection)
        self.session.commit()
        return collection

    def update(
        self,
        user: models.User,
        collection_id: int,
        coin_data: models.UpdateCoin,
    ) -> Collections:
        coin = self._get(user, collection_id)
        for field, value in coin_data:
            setattr(coin, field, value)
        self.session.commit()
        return coin

    def delete(
        self,
        user: models.User,
        collection_id: int,
    ):
        coin = self._get(user, collection_id)
        self.session.delete(coin)
        self.session.commit()

    def _get(self, user: models.User, collection_id: int) -> Optional[Collections]:
        collection: LinkCoinsToCollections = (self.session
            .query(LinkCoinsToCollections)
            .join(Coins)
            .join(Collections)
            .filter(
                Collections.id == collection_id
            )
            .first())
        if not collection:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return collection.collection