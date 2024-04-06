from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError
from src.models.entities.attendee import Attendee
from src.models.entities.check_in import CheckIn
from src.models.entities.event import Event
from src.models.settings.connection import db_connection_handler
from typing import Dict, List


class AttendeeRepository:
    def insert_attendee(self, attendee_info: Dict):
        with db_connection_handler as db:
            try:
                attendee = Attendee(
                    id=attendee_info.get("uuid"),
                    name=attendee_info.get("name"),
                    email=attendee_info.get("email"),
                    event_id=attendee_info.get("event_id"),
                )

                db.session.add(attendee)
                db.session.commit()

                return attendee_info

            except IntegrityError:
                # Como eu poderia debugar para identificar a estrutura de IntegrityError e garantir que ocorreu erro pela PK ou pela FK ?
                raise HttpConflictError("attendee already exists.")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str) -> Attendee:
        with db_connection_handler as db:
            try:
                attendee = (
                    db.session.query(Attendee)
                    .join(Event, Event.id == Attendee.event_id)
                    .filter(Attendee.id == attendee_id)
                    .with_entities(Attendee.name, Attendee.email, Event.title)
                    .one()
                )
                return attendee
            except NoResultFound:
                return None

    def get_attendees_by_event_id(self, event_id: str) -> List[Attendee]:
        with db_connection_handler as db:
            attendees = (
                db.session.query(Attendee)
                .outerjoin(CheckIn, CheckIn.attendeeId == Attendee.id)
                .filter(Attendee.event_id == event_id)
                .with_entities(
                    Attendee.id,
                    Attendee.name,
                    Attendee.email,
                    Attendee.created_at.label("createdAt"),
                    CheckIn.created_at.label("checkedInAt"),
                )
                .all()
            )
            return attendees
