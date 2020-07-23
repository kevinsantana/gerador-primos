from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from gerador_primos.modelos.exceptions import (GerarPrimosBaseException,
                                               NumeroNegativoException,
                                               ZeroException)


def carregar_exception_api(app: FastAPI):
    @app.exception_handler(404)
    async def exception_handler_404(request: Request, exc: HTTPException):
        return JSONResponse(status_code=404,
                            content={"status": 404,
                                     "mensagem": "Página não encontrada",
                                     "descrição": ""})

    @app.exception_handler(500)
    async def exception_handler_500(request: Request, exc: HTTPException):
        return JSONResponse(status_code=500,
                            content={"status": 500,
                                     "mensagem": "Erro interno",
                                     "descrição": ""})

    @app.exception_handler(NumeroNegativoException)
    async def exception_handler_numero_negativo(request: Request,
                                                exc: GerarPrimosBaseException):
        return JSONResponse(status_code=exc.status,
                            content={"status": exc.status,
                                     "mensagem": exc.mensagem,
                                     "descrição": exc.descricao})

    @app.exception_handler(ZeroException)
    async def exception_handler_zero(request: Request, exc: GerarPrimosBaseException):
        return JSONResponse(status_code=exc.status,
                            content={"status": exc.status,
                                     "mensagem": exc.mensagem,
                                     "descrição": exc.descricao})
