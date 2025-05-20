from sqlalchemy import insert, select

from database.creator import UsersTable
from database.workers.base import DatabaseWorker
from models import User


class UsersWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(UsersTable, database_path)

    def add_user(self, user: User):
        request = insert(UsersTable).values(**user.model_dump())
        self.connect.execute(request)
        self.connect.commit()

    def is_user(self, user: User) -> bool:
        request = select(UsersTable).where(UsersTable.email == user.email)
        return len(self.connect.execute(request).fetchall()) != 0
