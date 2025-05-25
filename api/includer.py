from fastapi import FastAPI

from api.routers.users import router as user_router
from api.routers.neural import router as neural_router


def include_routers(api: FastAPI):
    api.include_router(user_router)
    api.include_router(neural_router)