import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class TypesOfCoins(Base):
    __tablename__ = 'types_of_coins'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    value = sa.Column(sa.String)

    