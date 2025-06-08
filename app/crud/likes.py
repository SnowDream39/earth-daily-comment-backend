from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..db.models import Like
from ..db.database import database
from datetime import datetime


async def create_like(comment_id: int, user_id: str, session: AsyncSession):
    query = Like.insert().values(
        comment_id=comment_id,
        user_id=user_id,
        created_at=datetime.utcnow(),
    )
    like_id = await database.execute(query=query)
    return {
        "id": like_id,
        "user_id": user_id,
        "created_at": datetime.utcnow(),
        "comment_id": comment_id,
    }

