from database.database import User
from database.workers.base import DatabaseWorker


class UsersWorker(DatabaseWorker):
    def __init__(self, database_path: str):
        super().__init__(User, database_path)

    def add_user(self, user: User):
        if not isinstance(user, User):
            raise TypeError("user must be a User")

        self.session.add(user)
        self.session.commit()

    def is_user(self, user: User) -> bool:
        if not isinstance(user, User):
            raise TypeError("user must be a User")

        return len(self.session.query(User).filter(User.email == user.email).all()) != 0

    def get_user_hashed_password(self, user: User) -> str:
        if not isinstance(user, User):
            raise TypeError("user must be a User")

        return self.session.query(User).filter(User.email == user.email).first().password
