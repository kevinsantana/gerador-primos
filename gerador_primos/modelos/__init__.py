from typing import Optional

from pydantic import BaseModel


class __MensagemAPI(BaseModel):
    status: int
    mensagem: str


class MensagemIdentificadorStr(__MensagemAPI):
    identificador: str


class MensagemIdentificadorInt(__MensagemAPI):
    identificador: int


class MensagemDescricao(__MensagemAPI):
    descricao: Optional[str] = ""


class MensagemStatus(BaseModel):
    status: int
