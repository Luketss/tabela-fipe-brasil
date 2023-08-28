import json
import logging

from fastapi import APIRouter, status, HTTPException

from services.client import FipeClient

router = APIRouter(
    prefix="/items", tags=["items"], responses={404: {"description": "Not found"}}
)
client = FipeClient()


@router.post("/consultar-marcas")
async def post_consultar_marcas(tipo_veiculo, cod_tabela=299):
    data = {
        "codigoTabelaReferencia": f"{cod_tabela}",
        "codigoTipoVeiculo": f"{tipo_veiculo}",
    }
    r = client.post_request(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas", payload=data
    )
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)


@router.post("/consultar-modelos")
async def post_consultar_modelos(tipo_veiculo, codigo_marca):
    data = {
        "codigoTabelaReferencia": "299",
        "codigoTipoVeiculo": f"{tipo_veiculo}",
        "codigoMarca": f"{codigo_marca}",
    }
    r = client.post_request(
        "https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos", payload=data
    )
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)


@router.post("/consultar-modelos-por-ano")
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
    if r.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail="Requisição para fipe.org falhou")
    return json.loads(r.text)
