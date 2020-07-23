from fastapi import APIRouter

from gerador_primos.modelos.gerar_primos import (EstadoGerarPrimosResponse,
                                                 GerarPrimosResponse)
from gerador_primos.servicos.queue_manager import gerar_primos_task

rota = APIRouter()


@rota.get("/{task_id}", response_model=EstadoGerarPrimosResponse)
def buscar_estado(task_id: str):
    estado = gerar_primos_task.AsyncResult(task_id).state
    lista_primos = []
    if estado == "SUCCESS":
        lista_primos = gerar_primos_task.AsyncResult(task_id).result
    return {"status": 201, "estado": estado, "lista_primos": lista_primos}


@rota.get("/", summary="Gerar lista de numeros primos até n",
          response_model=GerarPrimosResponse, status_code=200)
def rota_gerar_primos(n: int) -> GerarPrimosResponse:
    task_id = gerar_primos_task.apply_async(queue="primos", args=[n]).id
    return {"status": 200, "task_id": task_id}
