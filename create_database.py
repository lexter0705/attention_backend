from sqlalchemy import create_engine

from config import ConfigReader
from database import Base

reader = ConfigReader()


def create_database():
    url = reader.read().database_url
    engine = create_engine(url)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_database()
