from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData, ForeignKey
from .database import metadata

comments = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("article_id", Integer, index=True),
    Column("user_id", String, index=True),
    Column("content", Text),
    Column("created_at", DateTime),
    Column("parent_id", Integer, nullable=True),
)
