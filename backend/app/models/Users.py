from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from backend.app.db.database import Base

class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column()
    weight: Mapped[int] = mapped_column()
    height: Mapped[int] = mapped_column()
    goals: Mapped[str] = mapped_column(String(300))
