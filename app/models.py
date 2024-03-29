from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import false, text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, TIMESTAMP, String
from .database import Base
from sqlalchemy import Column, Integer, NVARCHAR, Boolean

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(254), nullable=False)
    content = Column(String(4000), nullable=False)
    published = Column(Boolean,nullable=False, server_default='TRUE')
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String(20))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(254), nullable=False)
    create_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)

