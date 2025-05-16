from fastapi import APIRouter

from api.models.user import User

router = APIRouter(prefix="/users")


@router.post("/login")
async def login(user: User):
    pass


@router.post("/register")
async def register(user: User):
    pass
