from pydantic import BaseModel
from datetime import datetime
from .coins import Coin

class BaseCollection(BaseModel):
    name: str
    description: str

class CollectionCreate(BaseCollection):
    pass

class CollectionAppend(BaseModel):
    coin_id: int

class CollectionGet(BaseCollection):
    id: int

class Collection(CollectionGet):
    coins: list[Coin]

    class Config:
        orm_mode = True