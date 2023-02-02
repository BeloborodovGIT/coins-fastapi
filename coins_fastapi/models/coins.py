from pydantic import BaseModel

class BaseCoin(BaseModel):
    serial: int
    year_of_issue: str
    country_of_issue_id: int
    mint_id: int
    face_price: str
    currency_id: int
    type_id: int
    description: str

class CreateCoin(BaseCoin):
    pass

class UpdateCoin(BaseCoin):
    pass

class GetCoin(BaseCoin):
    owner_id: int

class Coin(GetCoin):
    id: int

    class Config:
        orm_mode = True