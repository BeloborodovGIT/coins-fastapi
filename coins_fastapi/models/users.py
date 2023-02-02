from pydantic import BaseModel
from ..database.users import RoleENUM


class BaseUser(BaseModel):
    login: str
    name: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int
    role: RoleENUM

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'