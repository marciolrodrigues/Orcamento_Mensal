import pandas as pd


def verificar_id(pasta: str) -> int:
    try:
        arquivo = pd.read_excel('data/orcamento.xlsx', sheet_name=pasta)
    except ValueError:
        return 1
    except FileNotFoundError:
        return 1
    try:
        if arquivo['cod'].max() > 0:
            return arquivo['cod'].max() + 1
        else:
            return 1
    except KeyError:
        return 1
