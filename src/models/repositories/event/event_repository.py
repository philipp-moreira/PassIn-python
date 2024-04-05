from src.models.settings.connection import db_connection_handler
from src.models.entities.event import Event
from typing import Dict
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class EventRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                event = Event(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                )
                db.session.add(event)
                db.session.commit()
                return eventsInfo
            except IntegrityError:
                raise Exception("Event already exists")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_event(self, event_id: str) -> Event:
        with db_connection_handler as db:
            try:
                event = db.session.query(Event).filter(Event.id == event_id).one()
                return event
            except NoResultFound:
                return None
