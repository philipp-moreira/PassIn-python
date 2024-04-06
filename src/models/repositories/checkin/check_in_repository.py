from src.errors.error_types.http_conflict import HttpConflictError
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_in import CheckIn
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class CheckInRepository:

    def insert_check_in(self, attendee_id: str) -> None:
        with db_connection_handler as db:
            try:
                check_in = CheckIn(attendeeId=attendee_id)
                db.session.add(check_in)
                db.session.commit()
                return

            except IntegrityError:
                raise HttpConflictError("Checkin already exists.")
            except Exception as exception:
                db.session.rollback()
                raise exception

    def get_check_in(self, check_in_id: int) -> CheckIn:
        with db_connection_handler as db:
            try:
                check_in = (
                    db.session.query(CheckIn).filter(CheckIn.id == check_in_id).one()
                )
                return check_in
            except NoResultFound:
                return None
