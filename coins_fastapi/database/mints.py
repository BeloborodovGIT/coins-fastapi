import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class Mints(Base):
    __tablename__ = 'mints'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)

    