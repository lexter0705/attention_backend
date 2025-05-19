from fastapi import APIRouter

from models import User

router = APIRouter(prefix="/users")


@router.post("/login")
async def login(user: User):
    pass


@router.post("/register")
async def register(user: User):
    pass
