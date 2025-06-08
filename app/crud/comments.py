from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..db.models import Comment
from datetime import datetime

async def create_comment(article_id: int, user_id: str, content: str, parent_id: int | None, session: AsyncSession):
    comment = Comment(
        article_id=article_id,
        user_id=user_id,
        content=content,
        created_at=datetime.utcnow(),
        parent_id=parent_id,
    )
    session.add(comment)              # 加入到session
    await session.commit()            # 提交保存到数据库
    await session.refresh(comment)   # 刷新，拿到自增id等字段
    return comment                   # 返回ORM对象

async def get_comments_by_article(article_id: int, session: AsyncSession):
    stmt = select(Comment).where(Comment.article_id == article_id).order_by(Comment.created_at.asc())  # 创建查询语句
    result = await session.execute(stmt)
    comments = result.scalars().all()  # 返回 ORM 对象列表
    return comments
