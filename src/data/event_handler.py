import uuid
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
