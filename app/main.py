import multiprocessing
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware
from uvicorn import Config

from app.core import settings
from app.db.init import init_db


@asynccontextmanager
async def lifespan(App: FastAPI):
    startup()
    yield
    shutdown()


App = FastAPI(lifespan=lifespan)
App.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])

Server = uvicorn.Server(
    Config(app=App, host=settings.HOST, port=settings.PORT, reload=settings.DEV, workers=multiprocessing.cpu_count()))


def init_routers():
    """
    初始化路由
    """
    from app.api.api_v1 import api_router
    # API路由
    App.include_router(api_router, prefix=settings.API_V1_STR)


def startup():
    init_routers()


def shutdown():
    pass


if __name__ == '__main__':
    init_db()
    Server.run()
