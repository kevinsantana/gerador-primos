from typing import List, Optional

from gerador_primos.modelos import MensagemStatus


class EstadoGerarPrimosResponse(MensagemStatus):
    estado: str
    lista_primos: Optional[List[int]]


class GerarPrimosResponse(MensagemStatus):
    task_id: str
