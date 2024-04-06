from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repositories.checkin.check_in_repository import CheckInRepository


class CheckInHandler:
    def __init__(self) -> None:
        self.__repository = CheckInRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param.get("attendee_id")
        self.__repository.insert_check_in(attendee_id)

        return HttpResponse(body=None, status_code=201)
