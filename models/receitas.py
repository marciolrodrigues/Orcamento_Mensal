from models.contas import Conta

class Receita:
    def __init__(self: object, cod: int, fonte: str, valor: float, data: str, descricao: str, conta: Conta) -> None:
        self.__cod: int = cod
        self.__fonte: str = fonte
        self.__valor: float = valor
        self.__data: str = data
        self.__descricao: str = descricao
        self.__conta: Conta = conta

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def fonte(self: object) -> str:
        return self.__fonte

    @fonte.setter
    def fonte(self: object, fonte: str) -> None:
        self.__fonte = fonte

    @property
    def valor(self: object) -> float:
        return self.__valor

    @valor.setter
    def valor(self: object, valor) -> None:
        self.__valor = valor

    @property
    def data(self: object) -> str:
        return self.__data

    @data.setter
    def data(self: object, data: str) -> None:
        self.__data = data

    @property
    def descricao(self: object) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self: object, descricao) -> None:
        self.__descricao = descricao

    @property
    def conta(self: object) -> Conta:
        return self.__conta

    @conta.setter
    def conta(self: object, conta: Conta) -> None:
        self.__conta = conta
