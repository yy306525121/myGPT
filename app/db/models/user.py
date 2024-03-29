from sqlalchemy import String, select, Boolean
from sqlalchemy.orm import Mapped, mapped_column, Session

from app.core.security import verify_password
from app.db.models import Base


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    roles: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, username={self.username!r}), role={self.roles}'

    @staticmethod
    def authenticate(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None
        if not verify_password(password, str(user.password)):
            return None
        return user

    @staticmethod
    def get_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
