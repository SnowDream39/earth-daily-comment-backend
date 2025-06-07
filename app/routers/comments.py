from fastapi import APIRouter, Header, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ..crud import comments as crud_comments
from datetime import datetime

router = APIRouter()

class CommentIn(BaseModel):
    article_id: int
    content: str
    parent_id: Optional[int] = None

class CommentOut(BaseModel):
    id: int
    article_id: int
    user_id: str
    content: str
    created_at: datetime
    parent_id: Optional[int] = None

async def get_current_user(x_token: str = Header(...)):
    # 临时代替身份验证，x_token 直接视作 user_id
    return x_token

@router.post("/comments/", response_model=CommentOut)
async def create_comment(comment: CommentIn, user_id: str = Depends(get_current_user)):
    return await crud_comments.create_comment(comment.article_id, user_id, comment.content, comment.parent_id)

@router.get("/comments/", response_model=List[CommentOut])
async def list_comments(article_id: int):
    return await crud_comments.get_comments_by_article(article_id)
