from src.errors.error_types.http_conflict import HttpConflictError
from src.models.entities.attendee import Attendee
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
                raise HttpConflictError("Event already exists")
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

    def count_event_attendees(self, event_id) -> Dict:
        with db_connection_handler as db:
            event_count = (
                db.session
                .query(Event)
                .join(Attendee, Event.id == Attendee.event_id)
                .filter(Event.id == event_id)
                .with_entities(Event.maximum_attendees, Attendee.id)
                .all()
            )

            if not len(event_count):
                return {"maximumAttendees": 0, "attendeesAmount": 0}

            return {
                "maximumAttendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count),
            }
