from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    email = Column(String, primary_key=True, unique=True, nullable=False)
    password = Column(String)


def create_database(path: str):
    engine = create_engine("sqlite:///" + path)
    Base.metadata.create_all(engine)
