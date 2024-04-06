import uuid
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.event.event_repository import EventRepository


class EventHandler:
    def __init__(self) -> None:
        self.__repository = EventRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__repository.insert_event(body)

        return HttpResponse(body={"event_id": body.get("uuid")}, status_code=201)

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param.get("event_id")
        event = self.__repository.get_event(event_id)
        if not event:
            raise HttpNotFoundError("Event not found")
        
        event_attendess_count = self.__repository.count_event_attendees(event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.details,
                    "maximumAttendees": event.maximum_attendees,
                    "attendeesAmount": event_attendess_count.get("attendeesAmount")
                }
            },
            status_code=200
        )
