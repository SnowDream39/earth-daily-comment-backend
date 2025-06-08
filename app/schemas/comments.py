from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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