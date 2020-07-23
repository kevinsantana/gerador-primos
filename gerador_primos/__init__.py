import time
import urllib3
import uuid

from loguru import logger
from fastapi import FastAPI
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from gerador_primos.rotas import v1
from gerador_primos.rotas.exception import carregar_exception_api


urllib3.disable_warnings()

# Versão
__version__ = "0.1.0"

# Logger Requisição
logger.level("REQUEST RECEBIDA", no=21, color="<white>")
logger.level("REQUEST FINALIZADA", no=21, color="<white>")
logger.level("CELERY TASK", no=40, color="<green>")

# Arquivos log da aplicação
logger.add("gerar_primos_debug.log", level="DEBUG", rotation="512 MB")
logger.add("gerar_primos_info.log", level="INFO", rotation="512 MB")
logger.add("gerar_primos_error.log", level="ERROR", rotation="512 MB")


app = FastAPI(
    title="Gerar Primos",
    description="O projeto tem por objetivo gerar uma lista de numeros primos \
                 com um gerenciador de fila com Celery e RabbitMQ",
    version=__version__
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Versões da rota
app.include_router(v1, prefix="/v1")

# Exceções API
carregar_exception_api(app)


# Controle do tempo das requisições
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = uuid.uuid1()

    logger.log("REQUEST RECEBIDA", f"[{request.method}] ID: {id} - \
        IP: {request.client.host} - ENDPOINT: {request.url.path}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINALIZADA", f"[{request.method}] ID: {id} - \
        IP: {request.client.host} - ENDPOINT: {request.url.path} - \
             TEMPO: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)

    return response


# Correção de contorno do fastapi
def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and 
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch
