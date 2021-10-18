import datetime
from enum import Enum

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from db.database import Base


class AppBaseModelOrm:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, default=None, nullable=True)
    created_datetime = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_datetime = Column(DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)


class Book(AppBaseModelOrm, Base):
    __tablename__: str = 'book'
    name = Column(String, nullable=False)
    author_name = Column(String, nullable=False)
    isbn = Column(String(20))
    user = relationship("User", secondary="user_review")


class User(AppBaseModelOrm, Base):
    __tablename__: str = "user"
    first_name = Column(String(40))
    last_name = Column(String(40))


class UserReview(AppBaseModelOrm, Base):
    __tablename__: str = "user_review"
    review = Column(String(300), nullable=True)
    rating = Column(SmallInteger, nullable=True)
    user_id = Column(
        Integer,
        ForeignKey('user.id'), primary_key=True)

    book_id = Column(
        Integer,
        ForeignKey('book.id'), primary_key=True)
    user = relationship("User", backref="book_associations")
    book = relationship("Book", backref="user_associations")
