import pytest
from .attendee_repository import AttendeeRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_database()

@pytest.mark.skip(reason="Para não criar registro efetivamente no banco de dados.")
def test_insert_attendee():
    # arrange
    attendee = {
        "uuid": "uma-chave-uuid-attendee-1",
        "name": "philipp",
        "email": "philipp@domain.com",
        "event_id": "uma-chave-uuid"
    }
    attendee_repository = AttendeeRepository()
    # act
    response = attendee_repository.insert_attendee(attendee)
    # assert
    print(response)

@pytest.mark.skip(reason="Teste criado inicialmente somente para testar repositório de attendees")
def test_get_attendee_badge_by_id():
    # arrange
    # attendee_id = "chave-que-nao-existe"
    attendee_id = "uma-chave-uuid-attendee"
    attendee_repository = AttendeeRepository()
    # act
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)
    # assert
    print(response)