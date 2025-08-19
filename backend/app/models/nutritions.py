from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from backend.app.db.database import Base

class Nutritions(Base):
    __tablename__ = "nutritions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date: Mapped[date] = mapped_column()
    meals: Mapped[str] = mapped_column(String(100))
    calories: Mapped[int] = mapped_column()
    macros: Mapped[int] = mapped_column()
