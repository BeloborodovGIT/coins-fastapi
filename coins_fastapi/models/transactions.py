from pydantic import BaseModel
from datetime import datetime

class BaseTransaction(BaseModel):
    to_user_id: int
    coin_id: int
    description: str

class TransactionCreate(BaseTransaction):
    pass

class TransactionGet(BaseTransaction):
    id: int
    from_user_id: int
    datetime: datetime

class Transaction(TransactionGet):
    pass

    class Config:
        orm_mode = True