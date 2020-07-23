from fastapi import APIRouter

from gerador_primos.rotas.v1 import gerar_primos


v1 = APIRouter()
v1.include_router(gerar_primos.rota, prefix="/primos", tags=["Gerar Primos"])
