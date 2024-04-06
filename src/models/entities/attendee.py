from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from src.models.settings.base import Base


class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(String, ForeignKey("attendees.id"),primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"))
    # fun.now() garante preenchimento DateTime UTC (fuso 0)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Attendee [id= {self.id}, name= {self.name}, email= {self.email}, event_id= {self.event_id}, created_at= {self.created_at}] "
