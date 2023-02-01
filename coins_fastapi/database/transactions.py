import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base 

class Transactions(Base):
    __tablename__ = 'transactions'
    
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    from_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    to_user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    coin_id = sa.Column(sa.Integer, sa.ForeignKey('coins.id'))
    datetime = sa.Column(sa.DateTime)
    description = sa.Column(sa.String)

    from_user = relationship('Users', foreign_keys=from_user_id)
    to_user = relationship('Users', foreign_keys=to_user_id)
    coin = relationship('Coins', foreign_keys=coin_id)