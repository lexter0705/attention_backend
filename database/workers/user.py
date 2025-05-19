from sqlalchemy import insert

from database.creator import UsersTable
from database.workers.base import DatabaseWorker
from models import User


class UsersWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(UsersTable, database_path)

    def add_user(self, user: User):
        request = insert(self.table).values()


    def find_user(self):
        pass
