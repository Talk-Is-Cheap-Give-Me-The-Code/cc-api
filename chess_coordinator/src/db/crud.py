from sqlalchemy.orm import Session
import hashlib

from . import models, manager


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, username: str, password: str):
    pwd_hash = hashlib.sha256(password.encode("ascii")).hexdigest()
    new_user = models.User(username=username, pwd_hash=pwd_hash)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_tournaments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tournament).offset(skip).limit(limit).all()


def create_user_tournament(
    db: Session, name: str, date: str, location: str, members: list
):
    pass
