from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# transformado a classe para visibilidade privada para que ela não
# seja exportada deste módulo e os repositórios possam criar mais de
# uma instância desta classe
class __DbConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}:///{}".format("sqlite", "./database/storage.db")
        self.__engine = None
        self.session = None

    def connect_to_database(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close_all()


# Habilita o mecanismo de criação de apenas uma instancia da classe de conexão com o banco de dados
# Design Pattern: Singleton ?
db_connection_handler = __DbConnectionHandler()
