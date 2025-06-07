"""
创建 FastAPI 应用
"""

from fastapi import FastAPI
from .db.database import metadata, engine
from .routers import comments
from .lifespan import lifespan

metadata.create_all(engine)

app = FastAPI(lifespan=lifespan)
app.include_router(comments.router)
