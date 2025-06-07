from ..db.models import comments
from ..db.database import database
from datetime import datetime

async def create_comment(article_id: int, user_id: str, content: str, parent_id: int | None = None):
    query = comments.insert().values(
        article_id=article_id,
        user_id=user_id,
        content=content,
        created_at=datetime.utcnow(),
        parent_id=parent_id,
    )
    comment_id = await database.execute(query)
    return {
        "id": comment_id,
        "article_id": article_id,
        "user_id": user_id,
        "content": content,
        "created_at": datetime.utcnow(),
        "parent_id": parent_id,
    }

async def get_comments_by_article(article_id: int):
    query = comments.select().where(comments.c.article_id == article_id).order_by(comments.c.created_at.asc())
    return await database.fetch_all(query)
