from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from backend.app.db.database import Base

class ExercisesModel(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(50))
    equipment: Mapped[str] = mapped_column(String(100))
    difficulty: Mapped[str] = mapped_column(String(50))
    instructions: Mapped[str] = mapped_column(String(500))
    target_muscles: Mapped[str] = mapped_column(String(200))