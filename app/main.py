"""
创建 FastAPI 应用
"""

from fastapi import FastAPI
from .api import comments, likes
from .db.database import engine
from .db.models import Base

app = FastAPI()
app.include_router(comments.router)
app.include_router(likes.router)

@app.on_event("startup")
async def on_startup():
    # 异步创建所有表结构（如果没有就创建）
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def on_shutdown():
    # 关闭异步引擎释放资源
    await engine.dispose()
