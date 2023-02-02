from pydantic import BaseModel

class BaseCountry(BaseModel):
    name: str

class CreateCountry(BaseCountry):
    pass

class UpdateCountry(BaseCountry):
    pass

class GetCountry(BaseCountry):
    id: int

class Country(GetCountry):

    class Config:
        orm_mode = True