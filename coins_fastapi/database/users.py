import sqlalchemy as sa
from enum import Enum
from . import Base

class RoleENUM(str, Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'

class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)

    login = sa.Column(sa.String, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)

    role = sa.Column(sa.Enum(RoleENUM, name='role'), nullable=False, default=RoleENUM.USER)
