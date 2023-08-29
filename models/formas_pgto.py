
class FormaPgto:
    def __init__(self: object, cod: int, banco: str, limite: float) -> None:
        self.__cod = cod
        self.__banco = banco
        self.__limite = limite

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def banco(self: object) -> str:
        return self.__banco

    @banco.setter
    def banco(self: object, banco: str) -> None:
        self.__banco = banco

    @property
    def limite(self: object) -> str:
        return self.__limite

    @limite.setter
    def limite(self: object, limite: float) -> None:
        self.__limite = limite
