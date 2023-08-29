from models.categorias import Categoria
from models.formas_pgto import FormaPgto
from datetime import datetime


class Despesa:

    def __init__(self: object, cod: int, categoria: Categoria,
                 data: str, descricao: str, forma_pgto: FormaPgto) -> None:
        self.__cod: int = cod
        self.__categoria: Categoria = categoria
        self.__data: str = data
        self.__descricao: str = descricao
        self.__forma_pgto: FormaPgto = forma_pgto

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def categoria(self: object) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self: object, categoria: Categoria) -> None:
        self.__categoria = categoria

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
    def descricao(self: object, descricao: str) -> None:
        self.__descricao = descricao

    @property
    def forma_pgto(self: object) -> FormaPgto:
        return self.__forma_pgto

    @forma_pgto.setter
    def forma_pgto(self: object, forma_pgto: FormaPgto) -> None:
        self.__forma_pgto = forma_pgto
