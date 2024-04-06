from src.models.settings.base import Base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.sql import func
# import é necessário para que não ocorra erro de insert onde o ORM não localiza a chave estrageira via 'attendees.id'
from src.models.entities.attendee import Attendee  # noqa: F401


class CheckIn(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey("attendees.id"))

    def __repr__(self):
        return f"CheckIn [id= {self.id}, attendeeId= '{self.attendeeId}', created_at= {self.created_at}]"
