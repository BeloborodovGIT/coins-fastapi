from pydantic import BaseModel

class BaseCoin(BaseModel):
    serial: str
    year_of_issue: str
    country_of_issue: str
    mint: str
    face_price: str
    currency: str
    type: str
    description: str
    owner_id: int

class CreateCoin(BaseCoin):
    pass

class UpdateCoin(BaseCoin):
    pass

class GetCoin(BaseCoin):
    pass

class Coin(BaseCoin):
    id: int

    class Config:
        orm_mode = True