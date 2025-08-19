from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import DateTime
from backend.app.db.database import Base

class WorkoutsModel(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: mapped_column(ForeignKey("users.id"))
    plan_name: Mapped[str] = mapped_column(String(100))
    date_time: Mapped[DateTime] = mapped_column()
    exercises: Mapped[int] = mapped_column(String(300))
    duration: Mapped[int] = mapped_column()