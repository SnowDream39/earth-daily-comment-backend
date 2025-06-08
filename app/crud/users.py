from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..db.models import User
from datetime import datetime, timezone

async def create_user(nickname: str, avatar: str, session: AsyncSession) -> User:
    user = User(
        avatar=avatar,
        created_at=datetime.now(timezone.utc),
        nickname=nickname
    )
    session.add(user)
    await  session.commit()
    await session.refresh(user)
    return user

async def get_user_by_id(id: str, session: AsyncSession) -> User | None:
    stmt = select(User).where(User.id == id)
    result = await session.execute(stmt)
    return result.scalars().first()