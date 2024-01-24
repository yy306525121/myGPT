from typing import Any, Self, List

from sqlalchemy.orm import DeclarativeBase, declared_attr, Session

from app.core import settings
from app.utils import StringUtils


class Base(DeclarativeBase):
    id: Any
    __name__: str

    def create(self, db):
        db.add(self)
        db.commit()
        return self

    @classmethod
    def get(cls, db: Session, id: int) -> Self:
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def list(cls, db: Session) -> List[Self]:
        result = db.query(cls).all()
        return list(result)

    @declared_attr
    def __tablename__(self) -> str:
        return settings.TABLE_PREFIX + StringUtils.camel_to_snake(self.__name__)
