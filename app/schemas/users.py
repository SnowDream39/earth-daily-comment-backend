from pydantic import BaseModel
from datetime import datetime

class UserIn(BaseModel):
    nickname: str
    avatar: str

class UserOut(BaseModel):
    id: str
    nickname: str
    avatar: str
    created_at: datetime