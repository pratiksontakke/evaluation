from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from backend.app.db.database import Base

class WorkoutPlansModel(Base):
    __tablename__ = "workout_plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    plan_name: Mapped[str] = mapped_column(String(100))
    difficulty: Mapped[str] = mapped_column(String(50))
    duration: Mapped[int] = mapped_column()
    target_muscle_groups: Mapped[str] = mapped_column(String(200))
    exercises_list: Mapped[str] = mapped_column(String(500))