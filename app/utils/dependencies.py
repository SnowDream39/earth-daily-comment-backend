from ..db.database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_current_user(x_token: str) -> str:
    return x_token
