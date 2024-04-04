from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer


#  aplicado mecanismo de heranca na classe event, para
# dar visibilidade ao sqlalchemy de que esta definicao existe
class Event(Base):
    # atributo private; usando '__' define a visibilidade de um membro de uma classe
    __tablename__ = "events"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    details = Column(String)
    slug = Column(String, nullable=False)
    maximum_attendees = Column(Integer, nullable=False)

    def __repr__(self):
        return f"[id= '{self.id}', title= '{self.title}', details= '{self.details}', slug= '{self.slug}', maximum_attendees= {self.maximum_attendees}]"
