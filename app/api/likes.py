from fastapi import APIRouter, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..crud import likes as crud_likes
from ..schemas.likes  import LikeIn, LikeOut
from ..utils.dependencies import get_session, get_current_user

router = APIRouter()


@router.post("/likes/", response_model=LikeOut)
async def create_like(like: LikeIn, user_id: str = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await crud_likes.create_like(like.comment_id, user_id, session)
