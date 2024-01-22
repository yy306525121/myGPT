import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core import settings

# 数据库引擎
engine = create_engine(f'mysql+pymysql://{settings.MYSQL_USERNAME}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:'
                       f'{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}',
                       echo=True)

# 数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    获取数据库会话
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()


class DBOper:
    _db: Session = None

    def __init__(self, db: Session = None):
        self._db = db
