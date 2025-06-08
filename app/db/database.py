"""
连接数据库，建立异步会话
"""


import databases
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./comments.db"

# databases库用于异步操作数据库
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# 创建异步引擎
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 使用 async_sessionmaker（推荐写法）
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)