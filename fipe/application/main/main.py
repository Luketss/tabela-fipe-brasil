import json
from fastapi import FastAPI, status, HTTPException
import requests
import asyncio

from services.client import FipeClient

app = FastAPI()

client = FipeClient()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/consultar-marcas")
async def get_consultar_marcas():
    return {"1": "Carro", "2": "Moto", "3": "Caminhão"}


@app.post("/consultar-marcas")
async def post_consultar_marcas(tipo_veiculo):
    data = {"codigoTabelaReferencia": "299", "codigoTipoVeiculo": f"{tipo_veiculo}"}

    r = client.post_request(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas", payload=data
    )
    print(r)
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)


@app.post("/consultar-modelos")
async def post_consultar_modelos(tipo_veiculo, codigo_marca):
    data = {
        "codigoTabelaReferencia": "299",
        "codigoTipoVeiculo": f"{tipo_veiculo}",
        "codigoMarca": f"{codigo_marca}",
    }
    r = client.post_request(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos", payload=data
    )
    print(r)
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)


@app.post("/consultar-modelos-por-ano")
async def post_consultar_modelos_por_ano(
    codigo_marca, codigo_modelo, ano, codigo_tipo_combustivel, ano_modelo
):
    data = {
        "codigoTabelaReferencia": "299",
        "codigoModelo": f"{codigo_modelo}",
        "codigoMarca": f"{codigo_marca}",
        "ano": f"{ano}",
        "codigoTipoCombustivel": f"{codigo_tipo_combustivel}",
        "anoModelo": f"{ano_modelo}",
    }
    r = client.post_request(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno",
        payload=data,
    )
    print(r)
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)
