import uvicorn
from fastapi import FastAPI

from .settings import config
from . import api

app = FastAPI(
    title='Coins-FastAPI',
    description='Сервис учёта коллекций нумизамтами',
    version='0.1.1',
)

app.include_router(api.router)

def start():
    uvicorn.run(
        app, 
        host=config.server_host,
        port=config.server_port
    )
