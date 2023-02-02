from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from ..settings import config

engine = create_engine(config.db_connetion_string, future=True)
Base = declarative_base()

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

def start_base():
        Base.metadata.create_all(bind=engine)


from .coins import *
from .users import *
from .transactions import *
from .countries import *
from .types_of_coins import *
from .mints import *
from .currencies import *