from asyncio import current_task

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine,async_scoped_session
from sqlalchemy.ext.declarative import declarative_base

from ..settings import config

engine = create_async_engine(config.db_connetion_string, future=True)
Base = declarative_base()

def session_factory():
    return async_scoped_session(
        sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            class_=AsyncSession,
            future=True
        ),
        scopefunc=current_task
    )

async def start_base():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


from .coins import *
from .users import *
from .transactions import *
from .countries import *
from .types_of_coins import *
from .mints import *
from .currencies import *