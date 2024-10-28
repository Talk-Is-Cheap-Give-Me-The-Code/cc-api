from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .manager import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    pwd_hash = Column(String)

    tournaments = relationship("Tournament", back_populates="owner")


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    date = Column(DateTime, index=True)
    location = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populate="tournaments")
    members = relationship("Member", back_populate="tournaments")


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    rating = Column(Integer, default=0)

    tournaments = relationship("Tournament", back_populate="members")
