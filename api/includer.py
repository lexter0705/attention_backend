from fastapi import FastAPI

from api.routers import websocket_router


def include_routers(api: FastAPI):
    api.include_router(websocket_router)
