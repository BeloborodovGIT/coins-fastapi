import uvicorn
import asyncio
from fastapi import FastAPI

from .database import start_base
from .settings import config
from . import api

app = FastAPI(
    title='Coins-FastAPI',
    description='Сервис учёта коллекций нумизамтами',
    version='0.0.1',
)

app.include_router(api.router)

def start():
    asyncio.run(start_base())
    uvicorn.run(
        app, 
        host=config.server_host,
        port=config.server_port
    )


