from pydantic import BaseModel

class BaseTransaction(BaseModel):
    from_user_id: int
    to_user_id: int
    coin_id: int
    datetime: int
    description: int

class CreateTransaction(BaseTransaction):
    pass

class UpdateTransaction(BaseTransaction):
    pass

class GetTransaction(BaseTransaction):
    owner_id: int

class Transaction(GetTransaction):
    id: int

    class Config:
        orm_mode = True