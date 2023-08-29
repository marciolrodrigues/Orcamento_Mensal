from models.formas_pgto import FormaPgto


class Conta(FormaPgto):
    def __init__(self: object, cod: int, banco: str, saldo: float, limite: float) -> None:
        super().__init__(cod, banco, limite)
        self.__saldo = saldo

    @property
    def cod(self: object) -> int:
        return self._FormaPgto__cod

    @property
    def banco(self: object) -> str:
        return self._FormaPgto__banco

    @banco.setter
    def banco(self: object, banco: str) -> None:
        self._FormaPgto__banco = banco

    @property
    def limite(self: object) -> str:
        return self._FormaPgto__limite

    @limite.setter
    def limite(self: object, limite) -> None:
        self._FormaPgto__limite = limite

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, saldo: float) -> None:
        self.__saldo = saldo
