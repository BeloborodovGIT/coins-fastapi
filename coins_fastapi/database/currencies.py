import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class Currencies(Base):
    __tablename__ = 'currencies'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)

    