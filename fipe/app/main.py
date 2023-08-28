import json

from fastapi import FastAPI, status, HTTPException

from services.client import FipeClient
from routers import fipe

app = FastAPI()

client = FipeClient()

app.include_router(fipe.router)


@app.get("/")
async def root():
    return {"1": "Carro", "2": "Moto", "3": "Caminhão"}
