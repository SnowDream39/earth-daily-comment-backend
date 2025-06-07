"""
生命周期控制。
如果要加载大模型、初始化第三方服务、连接 Redis、发送“服务已上线”通知……都应该写在这里。
"""


from contextlib import asynccontextmanager
from .db.database import database

@asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.disconnect()
