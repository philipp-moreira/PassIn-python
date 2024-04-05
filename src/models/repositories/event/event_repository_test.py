import pytest
from .event_repository import EventRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_database()

@pytest.mark.skip(reason="Para não criar registro efetivamente no banco de dados.")
def test_insert_event():
    # arrange
    event = {
        "uuid": "uma-chave-uuid",
        "title": "test event",
        "slug": "test-event",
        "maximum_attendees": 2
    }

    event_repository = EventRepository()
    # act
    response = event_repository.insert_event(event)
    # asssert
    print(response.get("title"))

@pytest.mark.skip(reason="Teste criado inicialmente somente para testar repositório de events")
def test_get_event():
    # arrange
    event_id = "uma-chave-uuid"
    repository = EventRepository()
    # act
    response = repository.get_event(event_id)
    # assert
    print(response)