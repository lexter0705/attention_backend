import os.path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import include_routers
from config import ConfigReader
from database.creator import create_database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = ConfigReader().read()
if not os.path.exists(config.database_path):
    create_database(config.database_path)

include_routers(app)
