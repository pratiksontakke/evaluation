from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.app.db.database import Base

class Progress(Base):
    __tablename__ = "progress"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    workout_id: Mapped[int] = mapped_column(ForeignKey("workouts.id")) 
    sets: Mapped[int] = mapped_column()
    reps: Mapped[int] = mapped_column()
    weight: Mapped[int] = mapped_column()
    notes: Mapped[str] = mapped_column(String(300))