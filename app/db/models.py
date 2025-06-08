from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()  # ORM 必须有 Base 类，所有模型都继承它


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, index=True)
    user_id = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=func.now())
    parent_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    # 关系
    replies = relationship("Comment", backref="parent", remote_side=[id])
    likes = relationship("Like", back_populates="comment")


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True)
    comment_id = Column(Integer, ForeignKey("comments.id"))
    created_at = Column(DateTime, default=func.now())

    comment = relationship("Comment", back_populates="likes")
