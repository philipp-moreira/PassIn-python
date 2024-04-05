from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_in import CheckIn
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


class CheckInRepository:

    def insert_check_in(self, check_in_info: Dict) -> Dict:
        with db_connection_handler as db:
            try:
                print("{} --> {}".format("INPUT", check_in_info))
                check_in = CheckIn(
                    attendeeId=check_in_info.get("attendeeId")
                )

                db.session.add(check_in)
                db.session.commit()
                return check_in_info

            except IntegrityError as exception:
                print("{} --> {}".format("ERROR/EXCEPTION", exception))
                raise Exception("Checkin already exists.")
            except Exception as exception:
                print("{} --> {}".format("ERROR/EXCEPTION", exception))
                db.session.rollback()
                raise exception

    def get_check_in(self, check_in_id: int) -> CheckIn:
        with db_connection_handler as db:
            try:
                check_in = (
                    db.session.query(CheckIn)
                    .filter(CheckIn.id == check_in_id)
                    .one()
                )
                return check_in
            except NoResultFound:
                return None
