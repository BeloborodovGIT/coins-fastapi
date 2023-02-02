from pydantic import BaseModel

class BaseCurrency(BaseModel):
    name: str

class CreateCurrency(BaseCurrency):
    pass

class UpdateCurrency(BaseCurrency):
    pass

class GetCurrency(BaseCurrency):
    id: int

class Currency(GetCurrency):

    class Config:
        orm_mode = True