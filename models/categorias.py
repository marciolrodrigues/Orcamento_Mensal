
class Categoria:

    def __init__(self: object, cod: int, nome: str, subtipo: str, descricao: str) -> None:
        self.__cod = cod
        self.__nome = nome
        self.__subtipo = subtipo
        self.__descricao = descricao

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def nome(self: object) -> str:
        return self.__nome

    @nome.setter
    def nome(self: object, nome: str) -> None:
        self.__nome = nome

    @property
    def subtipo(self: object) -> str:
        return self.__subtipo

    @subtipo.setter
    def subtipo(self: object, subtipo: str) -> None:
        self.__subtipo = subtipo

    @property
    def descicao(self: object) -> str:
        return self.__descricao

    @descicao.setter
    def descicao(self: object, descricao: str) -> None:
        self.__descricao = descricao
