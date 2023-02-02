from pydantic import BaseModel

class BaseMint(BaseModel):
    name: str

class CreateMint(BaseMint):
    pass

class UpdateMint(BaseMint):
    pass

class GetMint(BaseMint):
    id: int

class Mint(GetMint):

    class Config:
        orm_mode = True