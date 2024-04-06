
# Pass.In

## Resumo
Aplicação com o objetivo de viabilizar a gestão de eventos presenciais.

## Especificação

- ####  Backend
    - #### Requisitos
        - ##### 1 - Funcionais
            - 1.1 Cadastrar evento;
            - 1.2 Cadastrar um participante em um evento;
            - 1.3 Realizar check-in de um participante em um evento;
            - 1.4 Consultar um evento;
            - 1.5 Consultar uma participação;
            - 1.6 Consultar lista de participantes de um evento;
            - ##### - Regras de Negócio
                - O participante deve poder se inscrever em um evento apenas uma vez;
                - O participante deve poder ser inscrever em um evento que possua vaga disponível;

                >>**Nota**: Check-In: Confirmação de presença no evento
        - ##### 2 - Não Funcionais
            - N/C*

- #### Frontend
    *Não é escopo desta solução implementar a solução para frontend.*

    - #### Requisitos
        - ##### 1 - Funcionais
            - ~~1.1 Cadastrar evento;~~
            - ~~1.2 Cadastrar um participante em um evento;~~
            - ~~1.3 Realizar check-in de um participante em um evento;~~
            - ~~1.4 Consultar um evento;~~
            - ~~1.5 Consultar uma participação/visualizar o crachá de inscrição;~~
            - ~~1.6 Consultar lista de participantes de um evento;~~
            - ##### - Regras de Negócio
                - O participante deve poder se inscrever em um evento apenas uma vez;
                - O participante deve poder ser inscrever em um evento que possua vaga disponível;
                >>**Nota**: Check-In: Confirmação de presença no evento
        - ##### 2 - Não Funcionais
            - ~~2.1 O check-in no evento será realizado através de um QRCode;~~

- #### Diagrama(s) 
    - UML
    - DER (Diagrama Entidade Relacionamento)

- #### Stack
    - Banco de Dados
        - ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
    - Aplicação/Web API RestFull
      - ![Static Badge](https://img.shields.io/badge/Python-3.12-green?logo=python&logoColor=%233776AB)
      - Depências
        - ![Static Badge](https://img.shields.io/badge/flask-v3.0.2-green?logo=flask&logoColor=%23000000&link=https%3A%2F%2Fpypi.org%2Fproject%2FFlask%2F)
        - ![Static Badge](https://img.shields.io/badge/SQLAlchemy-v2.0.29-green?logo=sqlalchemy&logoColor=%230C0C0E&link=https%3A%2F%2Fpypi.org%2Fproject%2FSQLAlchemy%2F)
        - ![Static Badge](https://img.shields.io/badge/Pytest-v8.1.1-green?logo=pytest&logoColor=%230A9EDC&link=https%3A%2F%2Fpypi.org%2Fproject%2Fpytest%2F)
        

- #### Swagger / openApi / Endpoints
 - Adicionado ao projeto a pasta [requests__by_client_http](https://github.com/philipp-moreira/PassIn-python/tree/main/requests__by_client_http)
   contendo todas as requests http; Geradas utilizando plugin do [Visual Studio Code](https://code.visualstudio.com/download) [Thuder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)


