from typing import Type

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine


class DatabaseWorker:
    def __init__(self, table: Type[DeclarativeBase], database_path: str):
        database_url = "sqlite:///" + database_path
        engine = create_engine(database_url)
        self.__table = table
        self.__connect = engine.connect()

    @property
    def table(self):
        return self.__table

    @property
    def connect(self):
        return self.__connect