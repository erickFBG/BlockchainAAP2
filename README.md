# Blockchain para transformar imóveis em ativos digitais

Esse projeto foi feito por Henrique Kalke, Rodrigo Roth e Erick França.

A API está contido em `blockchain_services.py`.

O arquivo `blockchain.py` possui os modulos necessarios para o funcionamento da API.

## Run the app

    cd AAP2
    python blockchain_services.py

# API

Os metôdos da API estão descritos abaixo.

## Obter a lista de chains

### Request

`GET /get_chain`

    http://localhost:5000/get_chain

### Response

    HTTP/1.1 200 OK
    Date: Friday, 24 Sep 2021 16:36:30 GMT-3
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {
    "chain": [
        {
            "data": {
                "city": "city",
                "owner_name": "owner_name",
                "record_number": "record_name",
                "zip_code": "zip_code"
            },
            "index": index,
            "original_index": original_index,
            "previous_hash": "previous_hash",
            "proof": proof,
            "timestamp": "timestamp"
        },
        {
            "data": {
                "city": "city",
                "owner_name": "owner_name",
                "record_number": "record_number",
                "zip_code": "zip_code"
            },
            "index": index,
            "original_index": original_index,
            "previous_hash": "previous_hash",
            "proof": proof,
            "timestamp": "timestamp"
        },
        {
            "data": {
                "city": "city",
                "owner_name": "owner",
                "record_number": "record_number",
                "zip_code": "zip_code"
            },
            "index": index,
            "original_index": original_index,
            "previous_hash": "previous_hash",
            "proof": proof,
            "timestamp": "timestamp"
        }
    ],
    "length": 3
    }
    
    
## Procurando o chain com o nome especifico.

### Request

`GET /get_names/name`

    http://localhost:5000/get_names/name

### Response

    HTTP/1.1 200 OK
    Date: Friday, 24 Sep 2021 16:36:30 GMT-3
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    [
    {
        "data": {
            "city": "city",
            "owner_name": "owner_name",
            "record_number": "record_number",
            "zip_code": "zip_code"
        },
        "index": index,
        "original_index": original_index,
        "previous_hash": "previous_hash",
        "proof": proof,
        "timestamp": "timestamp"
    },
    {
        "data": {
            "city": "city",
            "owner_name": "owner_name",
            "record_number": "record_number",
            "zip_code": "zip_code"
        },
        "index": index,
        "original_index": original_index,
        "previous_hash": "previous_hash",
        "proof": proof,
        "timestamp": "timestamp"
    }
    ]

## Validar a chain

### Request

`GET /valid`

    http://localhost:5000/valid

### Response

    HTTP/1.1 200 OK
    Date: Friday, 24 Sep 2021 16:36:30 GMT-3
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {'message': 'A cadeia é valida.'}

## Minerando o bloco

### Request

`POST /mine_block`

    {
    "owner_name": "owner_name",
    "city": "city",
    "zip_code": "zip_code",
    "record_number": "record_name"
    }

### Response

    HTTP/1.1 200 OK
    Date: Friday, 24 Sep 2021 16:36:30 GMT-3
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {
    "index": index,
    "message": {
            "owner_name": "owner_name",
            "city": "city",
            "zip_code": "zip_code",
            "record_number": "record_name"
            },
    "previous_hash": "previous_hash",
    "proof": proof,
    "timestamp": "timestamp"
    }

## Editar registro

### Request

`POST /edit_regitry/index`

    {
    "owner_name": "owner_name",
    "city": "city",
    "zip_code": "zip_code",
    "record_number": "record_number"
    }

### Response

    HTTP/1.1 200 OK
    Date: Friday, 24 Sep 2021 16:36:30 GMT-3
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {
    "index": index,
    "message": {
            "city": "city",
            "owner_name": "owner_name",
            "record_number": "record_number",
            "zip_code": "zip_code"
             },
    "original_index": "original_index",
    "previous_hash": "previous_hash",
    "proof": proof,
    "timestamp": "timestamp"
    }
