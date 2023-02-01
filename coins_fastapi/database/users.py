import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class Users(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)

    login = sa.Column(sa.String, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)