from pydantic import BaseModel
from datetime import datetime

class LikeIn(BaseModel):
    comment_id: int

class LikeOut(BaseModel):
    comment_id: int
    created_at: datetime
    id: int
    user_id: str
