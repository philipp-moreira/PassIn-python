from typing import Dict

from src.models.settings.connection import db_connection_handler
from src.models.entities.event import Event


class EventRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as db:
            event = Event(
                id=eventsInfo.get("id"),
                title=eventsInfo.get("title"),
                details=eventsInfo.get("details"),
                slug=eventsInfo.get("slug"),
                maximum_attendees=eventsInfo.get("maximum_attendees"),
            )
            db.session.add(event)
            db.session.commit()
            return eventsInfo

    def get_event(self, event_id: str) -> Event:
        with db_connection_handler as db:
            event = (
                db.session
                    .query(Event)
                    .filter(Event.id == event_id)
                    .one()
            )
            return event