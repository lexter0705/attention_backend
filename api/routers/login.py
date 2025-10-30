from fastapi import APIRouter, HTTPException

from api.cryptor import Cryptor
from api.models import User
from config import ConfigReader
from database import Users
from database.workers.user import UsersWorker

router = APIRouter(prefix="/users")

config = ConfigReader().read()

worker = UsersWorker(config.database_path)


@router.post("/login")
async def login(user: User):
    user_for_db = Users(email=user.email, password=user.password)

    if not worker.is_user(user_for_db):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    if not Cryptor.verify_password(user.password, worker.get_user_hashed_password(user_for_db)):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    return 201


@router.post("/register")
async def register(user: User):
    if worker.is_user(Users(email=user.email, password=user.password)):
        raise HTTPException(status_code=409, detail="User is already registered")

    user_in_db = Users(email=user.email, password=Cryptor.hash_password(user.password))
    worker.add_user(user_in_db)
