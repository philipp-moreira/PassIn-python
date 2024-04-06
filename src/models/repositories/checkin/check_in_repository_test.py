import pytest
from src.models.repositories.checkin.check_in_repository import CheckInsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_database()

@pytest.mark.skip(reason="Para não criar registro efetivamente no banco de dados.")
def test_insert_check_in():
    # arrange
    check_in = "d9524136-54b5-40f9-b89a-053621f3b2f0"

    check_in_repository = CheckInsRepository()
    # act
    response = check_in_repository.insert_check_in(check_in)
    # assert
    print(response)

@pytest.mark.skip(reason="Teste criado inicialmente somente para testar repositório de checkins")
def test_get_check_in():
    # arrange
    check_in_id = 1
    check_in_repository = CheckInsRepository()
    # act
    response = check_in_repository.get_check_in(check_in_id)
    #assert
    print(response)