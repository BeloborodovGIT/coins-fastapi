import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Base

class Coins(Base):
    __tablename__ = 'coins'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    serial = sa.Column(sa.String, unique=True)
    year_of_issue = sa.Column(sa.String)
    country_of_issue_id = sa.Column(sa.Integer, sa.ForeignKey('countries.id'))
    mint_id = sa.Column(sa.Integer, sa.ForeignKey('mints.id'))
    face_price = sa.Column(sa.String)
    currency_id = sa.Column(sa.Integer, sa.ForeignKey('currencies.id'))
    type_id = sa.Column(sa.Integer, sa.ForeignKey('types_of_coins.id'))
    description = sa.Column(sa.String)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    country_of_issue = relationship('Countries', foreign_keys=country_of_issue_id)
    mint = relationship('Mints', foreign_keys=mint_id)
    currency = relationship('Currencies', foreign_keys=currency_id)
    type = relationship('TypesOfCoins', foreign_keys=type_id)
