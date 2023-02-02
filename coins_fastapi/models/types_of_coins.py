from pydantic import BaseModel

class BaseTypeOfCoin(BaseModel):
    name: str

class CreateTypeOfCoin(BaseTypeOfCoin):
    pass

class UpdateTypeOfCoin(BaseTypeOfCoin):
    pass

class GetTypeOfCoin(BaseTypeOfCoin):
    id: int

class TypeOfCoin(GetTypeOfCoin):

    class Config:
        orm_mode = True