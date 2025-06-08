from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from ..crud import users as crud_users
from ..schemas.users import UserIn, UserOut
from ..utils.dependencies import get_session, get_current_user

router = APIRouter()

@router.post("/user/", response_model=UserOut)
async def create_user(user: UserIn, session: AsyncSession = Depends(get_session)):
    return await crud_users.create_user(user.nickname, user.avatar, session)

@router.get("/user/{id}", response_model=UserOut)
async def get_user_by_id(id: str, session: AsyncSession = Depends(get_session)):
    return await crud_users.get_user_by_id(id, session)