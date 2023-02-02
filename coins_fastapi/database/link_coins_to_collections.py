import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class LinkCoinsToCollections(Base):
    __tablename__ = 'link_coins_to_collections'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    coin_id = sa.Column(sa.Integer, sa.ForeignKey('coins.id'))
    collection_id = sa.Column(sa.Integer, sa.ForeignKey('collections.id'))

    coin = relationship('Coins', foreign_keys=coin_id)
    collection = relationship('Collections', foreign_keys=collection_id)