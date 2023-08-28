# Tabela Fipe Brasil

<p>O objetivo desse repositório é criar uma api para trabalhar com os dados da tabela fipe</p>

## Como utilizar

```
poetry install
```

Navegue ate a pasta app dentro de /fipe e execute o seguinte comando
```
uvicorn main:app --reload
```


Ideias:

    - Gerar um csv com todas as informações puxadas da api
    - Buscar por modelo e receber o código (id)
    - Buscar por marca e receber o código (id)
    - Pesquisa por código fipe
    - Buscar outras infos do site além de preço de veículo
    - Consulta IPC
    - Consulta Preço Máquinas Agrícolas
    - Salarios -> https://salarios.org.br/home
