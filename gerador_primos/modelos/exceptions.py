class GerarPrimosBaseException(Exception):
    status = None

    def __init__(self, *, mensagem: str, descricao: str = ""):
        self.mensagem = mensagem
        self.descricao = descricao


class NumeroNegativoException(GerarPrimosBaseException, TypeError):
    status = 422


class ZeroException(GerarPrimosBaseException, TypeError):
    status = 422
