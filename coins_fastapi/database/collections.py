import sqlalchemy as sa

from . import Base

class Collections(Base):
    __tablename__ = 'collections'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String)