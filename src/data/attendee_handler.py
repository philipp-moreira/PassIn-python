import uuid
from src.errors.error_types.http_conflict import HttpConflictError
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.attendee.attendee_repository import AttendeeRepository
from src.models.repositories.event.event_repository import EventRepository


class AttendeeHandler:
    def __init__(self) -> None:
        self.__repository = AttendeeRepository()
        self.__event_repository = EventRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param.get("event_id")

        event_attendee_count = self.__event_repository.count_event_attendees(event_id)
        if event_attendee_count.get(
            "maximumAttendees"
        ) > 0 and event_attendee_count.get(
            "maximumAttendees"
        ) == event_attendee_count.get(
            "attendeesAmount"
        ):
            raise HttpConflictError("sold out event.")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id

        self.__repository.insert_attendee(body)

        return HttpResponse(body={"attendeeId": body.get("uuid")}, status_code=201)

    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param.get("attendee_id")
        badge = self.__repository.get_attendee_badge_by_id(attendee_id)
        if not badge:
            raise HttpNotFoundError("Attendee not found")

        return HttpResponse(
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title,
                }
            },
            status_code=200,
        )

    def find_attendees_by_event_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param.get("event_id")
        attendees = self.__repository.get_attendees_by_event_id(event_id)
        if not attendees:
            raise HttpNotFoundError("Attendess not found")

        formated_attendees = []

        for attendee in attendees:
            formated_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "createdAt": attendee.createdAt,
                    "checkedInAt": attendee.checkedInAt,
                }
            )

        return HttpResponse(body={"attendees": formated_attendees}, status_code=200)
