from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    email = Column(String, primary_key=True, unique=True, nullable=False)
    password = Column(String)


def create_database(database_url: str):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
