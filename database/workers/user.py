from database.creator import Users
from database.workers.base import DatabaseWorker


class UsersWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(Users, database_path)

    def add_user(self, user: Users):
        self.session.add(user)
        self.session.commit()

    def is_user(self, user: Users) -> bool:
        return len(self.session.query(Users).filter(Users.email == user.email).all()) != 0
