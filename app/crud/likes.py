from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..db.models import Like
from ..db.database import database
from datetime import datetime


async def create_like(comment_id: int, user_id: str, session: AsyncSession):
    like = Like(
        comment_id=comment_id,
        user_id=user_id,
        created_at=datetime.utcnow(),
    )
    session.add(like)
    await session.commit()
    await session.refresh(like)
    return like
