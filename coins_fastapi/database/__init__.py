from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from ..settings import config

engine = create_engine(config.db_connetion_string, future=True)
Base = declarative_base()

session_item: Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = session_item()
    try:
        yield session
    finally:
        session.close()



from .coins import *
from .users import *
from .transactions import *
from .countries import *
from .types_of_coins import *
from .mints import *
from .currencies import *
from .collections import *
from .link_coins_to_collections import *