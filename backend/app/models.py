from typing import Optional, List
from .database import Base
from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship


followers = Table(
    'followers',
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id')),
    Column('followed_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(200))
    login: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    photo_profile: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    posts: Mapped[List["Post"]] = relationship(back_populates="user")
    liked_posts: Mapped[List["LikePost"]] = relationship(back_populates="user")
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")
    liked_comments: Mapped[List["LikeComment"]] = relationship(back_populates="user")

    following: Mapped[List["User"]] = relationship(
        "User",
        secondary=followers,
        primaryjoin=id == followers.c.follower_id,
        secondaryjoin=id == followers.c.followed_id,
        back_populates="followers"
    )
    followers: Mapped[List["User"]] = relationship(
        "User",
        secondary=followers,
        primaryjoin=id == followers.c.followed_id,
        secondaryjoin=id == followers.c.follower_id,
        back_populates="following"
    )

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String(4000))
    media: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
    likes: Mapped[List["LikePost"]] = relationship(back_populates="post")

class LikePost(Base):
    __tablename__ = "like_post"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

    user: Mapped["User"] = relationship(back_populates="liked_posts")
    post: Mapped["Post"] = relationship(back_populates="likes")

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String)
    media: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

    user: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")
    likes: Mapped[List["LikeComment"]] = relationship(back_populates="comment")

class LikeComment(Base):
    __tablename__ = "like_comment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    comment_id: Mapped[int] = mapped_column(ForeignKey("comments.id"))

    user: Mapped["User"] = relationship(back_populates="liked_comments")
    comment: Mapped["Comment"] = relationship(back_populates="likes")