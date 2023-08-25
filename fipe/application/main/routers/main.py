import json
from fastapi import FastAPI, status, HTTPException
import requests
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/consultar-marcas")
async def get_consultar_marcas():
    return {"1": "Carro", "2": "Moto", "3": "Caminhão"}


@app.post("/consultar-marcas")
async def post_consultar_marcas(tipo_veiculo):
    data = {"codigoTabelaReferencia": "299", "codigoTipoVeiculo": f"{tipo_veiculo}"}
    r = requests.post(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas", data=data
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
    r = requests.post(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos", data=data
    )
    print(r)
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)
