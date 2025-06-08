"""
创建 FastAPI 应用
"""

from fastapi import FastAPI
from .api import comments, likes
from .db.database import engine
from .db.models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(comments.router)
app.include_router(likes.router)

allow_origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # 允许的前端来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法：GET, POST, PUT, DELETE 等
    allow_headers=["*"],  # 允许所有请求头
)

@app.on_event("startup")
async def on_startup():
    # 异步创建所有表结构（如果没有就创建）
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def on_shutdown():
    # 关闭异步引擎释放资源
    await engine.dispose()
