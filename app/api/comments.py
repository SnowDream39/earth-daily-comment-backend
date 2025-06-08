from fastapi import APIRouter, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..crud import comments as crud_comments
from ..schemas.comments import CommentIn, CommentOut
from ..utils.dependencies import get_session

router = APIRouter()


async def get_current_user(x_token: str = Header(...)):
    # 临时代替身份验证，x_token 直接视作 user_id
    return x_token

@router.post("/comment/", response_model=CommentOut)
async def create_comment(comment: CommentIn, user_id: str = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await crud_comments.create_comment(comment.article_id, user_id, comment.content, comment.parent_id, session)

@router.get("/comment/", response_model=list[CommentOut])
async def list_comments(article_id: int, session: AsyncSession = Depends(get_session)):
    return await crud_comments.get_comments_by_article(article_id, session)
