from datetime import datetime
from models.formas_pgto import FormaPgto


class Cartao(FormaPgto):
    def __init__(self: object, bandeira: str, vcto: int, cod: int, limite: float) -> None:
        super().__init__(cod, limite)
        self.__bandeira = bandeira
        self.__vcto = vcto

    @property
    def cod(self: object) -> int:
        return self._FormaPgto__cod

    @property
    def limite(self: object) -> str:
        return self._FormaPgto__limite

    @limite.setter
    def limite(self: object, limite: float) -> None:
        self._FormaPgto__limite = limite

    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @bandeira.setter
    def bandeira(self: object, bandeira: str) -> None:
        self.__bandeira = bandeira

    @property
    def vcto(self: object) -> int:
        return self.__vcto

    @vcto.setter
    def vcto(self: object, vcto: datetime) -> None:
        self.__vcto = vcto
