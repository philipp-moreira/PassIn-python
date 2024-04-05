from src.models.settings.base import Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func


class CheckIn(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    attendeeId = Column(String, ForeignKey("attendees.id"))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"[id= {self.id}, attendeeId= '{self.attendeeId}', created_at= {self.created_at}]"
