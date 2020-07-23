from celery import Celery
from loguru import logger

from gerador_primos.config import BROKER
from gerador_primos.modulos.eh_primo import eh_primo


celery_task = Celery("queue_manager", broker=BROKER, backend="amqp")


@celery_task.task(acks_late=True, ignore_result=False, track_started=True)
def gerar_primos_task(n):
    logger.log("CELERY TASK", f"GERANDO LISTAS DE PRIMOS ATÉ {n}")
    primos = [x for x in range(n) if eh_primo(x)]
    gerar_primos_task.update_state(state="SUCCESS")
    return primos
