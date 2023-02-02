import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class Countries(Base):
    __tablename__ = 'countries'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)