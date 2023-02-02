from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import selectinload

from ...database import *

from ... import models


class CollectionsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self, user: models.User) -> List[Collections]:
        if user.role == RoleENUM.ADMIN:
            collections_link: List[Collections] = (
                self.session
                .query(LinkCoinsToCollections)
                .join(Collections)
                .join(Coins)
                .filter(Coins.owner_id == user.id)
            ).all()
        else:
            collections: List[Collections] = (
                self.session
                .query(Collections)
            )

        collections = [item.collection for item in collections_link]

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

        collection: Collections = (
            self.session
            .query(Collections)
            .filter(Collections.id == collection_id)
            .first()
        )

        return collection




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