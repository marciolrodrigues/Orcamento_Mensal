from typing import List
from time import sleep
from utils.helper import verificar_id
import pandas as pd


nome_aplicativo = ' CONTROLE DE ORÇAMENTO MENSAL '


# Construção do Cabeçalho de Página
def cabecalho(submenu: str) -> None:
    print(f'*' * 100)
    print(f'{nome_aplicativo:*^100}')
    print(f'*' * 100 + '\n')
    if submenu != '':
        print(f'{submenu:*^100}\n')


# Construção do Cabeçalho do Menu Principal
def menu_principal():
    cabecalho('')
    print('1 - Cadastro')
    print('2 - Consulta')
    print('3 - Edição')
    print('4 - Exclusão')
    print('0 - SAIR')

    opcao = int(input())

    if opcao == 1:
        menu_cadastro()
    elif opcao == 2:
        menu_consulta()
    elif opcao == 3:
        menu_edicao()
    elif opcao == 4:
        menu_exclusao()
    elif opcao == 0:
        exit(0)
    else:
        print('Opção digitada não é válida')
        sleep(2)
        menu_principal()


# Cosntrução do Menu de Cadastro
def menu_cadastro():
    cabecalho(' MENU DE CADASTRO ')
    print('1 - Cadastrar Categoria')
    print('2 - Cadastrar Conta')
    print('3 - Cadastrar Cartão')
    print('4 - Cadastrar Despesa')
    print('5 - Cadastrar Receitas')
    print('0 - Voltar ao menu principal')

    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        cadastrar_categoria()
    elif opcao == 2:
        cadastrar_conta()
    elif opcao == 3:
        cadastrar_cartao()
    elif opcao == 4:
        cadastrar_despesa()
    elif opcao == 5:
        cadastrar_receita()
    elif opcao == 0:
        menu_principal()
    else:
        print('Opção inválida!')
        sleep(2)
        menu_cadastro()


def menu_consulta():
    cabecalho(' MENU DE CONSULTA ')
    print('1 - Consultar Categoria')
    print('2 - Consultar Conta')
    print('3 - Consultar Cartão')
    print('4 - Consultar Despesa')
    print('5 - Consultar Receitas')
    print('0 - Voltar ao menu principal')

    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        consultas('Categorias')
    elif opcao == 2:
        consultas('Contas')
    elif opcao == 3:
        consultas('Cartões')
    elif opcao == 4:
        consultas('Despesas')
    elif opcao == 5:
        consultas('Receitas')
    elif opcao == 0:
        menu_principal()
    else:
        print('Opção inválida!')
        sleep(2)
    menu_consulta()


def menu_edicao():
    cabecalho(' MENU DE EDIÇÃO ')
    print('1 - Editar Categoria')
    print('2 - Editar Conta')
    print('3 - Editar Cartão')
    print('4 - Editar Despesa')
    print('5 - Editar Receitas')
    print('0 - Voltar ao menu principal')

    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        editar('Categorias')
    elif opcao == 2:
        editar('Contas')
    elif opcao == 3:
        editar('Cartões')
    elif opcao == 4:
        editar('Despesas')
    elif opcao == 5:
        editar('Receitas')
    elif opcao == 0:
        menu_principal()
    else:
        print('Opção inválida!')
        sleep(2)
        menu_edicao()


def menu_exclusao():
    pass


def gravar(nova_linha, sheet):
    try:
        arquivo = pd.read_excel('data/orcamento.xlsx', sheet_name=sheet)
        arquivo = arquivo._append(nova_linha, ignore_index=True)
    except FileNotFoundError:
        arquivo = pd.DataFrame(nova_linha, index=[0])
        with pd.ExcelWriter('data/orcamento.xlsx', mode='w') as writer:
            arquivo.to_excel(writer, sheet_name=sheet, index=False)
            print('Cadastro efetuado com sucesso')
            return
    except ValueError:  # caso a sheet ainda não existia
        arquivo = pd.DataFrame(nova_linha, index=[0])

    with pd.ExcelWriter('data/orcamento.xlsx', mode='a', if_sheet_exists='replace') as writer:
        try:
            # writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
            arquivo.to_excel(writer, sheet_name=sheet, index=False)
        except AttributeError:
            arquivo.to_excel(writer, sheet_name=sheet, index=False)

    print('Cadastro efetuado com sucesso')


def consultas(sheet: str, titulo=True) -> List:
    codigos = []
    if titulo:
        cabecalho(f' CONSULTA DE {sheet.upper()} ')
    try:
        arquivo = pd.read_excel('data/orcamento.xlsx', sheet_name=sheet)
        codigos = arquivo['cod'].tolist()
        arquivo = arquivo.fillna('-')
        dict_arquivo = arquivo.set_index('cod').to_dict()
        list_arquivo = list(dict_arquivo.keys())

        print('COD' + (17 * ' '), end='')

        for item in list_arquivo:
            print(item.upper(), end='')
            print(' ' * (20 - len(item)), end='')

        print()

        for item in codigos:
            print(item, end='')
            print(' ' * (20 - len(str(item))), end='')
            for col in list_arquivo:
                print(dict_arquivo[f'{col}'][item], end='')
                print(' ' * (20 - len(str(dict_arquivo[f'{col}'][item]))), end='')
            print('')
    except FileNotFoundError:
        print('Não existem categorias cadastradas!')
        sleep(2)
    except ValueError:
        print('Não existem categorias cadastradas!')
        sleep(2)
    if titulo:
        input('Digite ENTER para continuar')
    return codigos


def editar(sheet: str) -> None:
    codigos = consultas(sheet, False)
    cod_alterar = int(input('Digite o código que deseja efetuar a alteração: '))
    if cod_alterar in codigos:
        try:
            arquivo = pd.read_excel('data/orcamento.xlsx', sheet_name=sheet)
            print(arquivo.loc[arquivo['cod'] == cod_alterar])
            campo_alterar = input('Digite o nome do campo à ser alterado: ')
            if campo_alterar.lower() in arquivo:
                novo_valor = input('Digite o novo valor para o campo escolhido: ')
                arquivo.loc[arquivo['cod'] == cod_alterar, campo_alterar.lower()] = novo_valor
                with pd.ExcelWriter('data/orcamento.xlsx', mode='a', if_sheet_exists='replace') as writer:
                    arquivo.to_excel(writer, sheet_name=sheet, index=False)
            else:
                print("Campo não localizado")

        except FileNotFoundError:
            print(f'Não existem {sheet} cadastrados(as)!')
            sleep(2)
        except ValueError:
            print(f'Não existem {sheet} cadastrados(as)!')
            sleep(2)
    else:
        print('O código digitado não existe!')

    menu_edicao()


def cadastrar_categoria():
    sheet = 'Categorias'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro
    nome = input('Digite o nome da nova categoria: ')
    descricao = input('Digite a descrição da nova categoria: ')
    nova_linha = {
        'cod': id_atual,
        'nome': nome,
        'descricao': descricao,
    }
    gravar(nova_linha, sheet)

    sleep(2)
    menu_cadastro()


def listar_categorias():
    try:
        arquivo = pd.read_excel('data/orcamento.xlsx', sheet_name='Categorias')
        dict_arquivo = arquivo.set_index('cod').to_dict()
        for chave, valor in dict_arquivo['nome'].items():
            print(f'{chave}: {valor}')
    except FileNotFoundError:
        print('Não existem categorias cadastradas!')
        sleep(2)
        menu_cadastro()
    except ValueError:
        print('Não existem categorias cadastradas!')
        sleep(2)
        menu_cadastro()


def listar_formas_pgto():
    cartoes = pd.DataFrame()
    try:
        cartoes = pd.read_excel('data/orcamento.xlsx', sheet_name='Cartões')
    except FileNotFoundError:
        try:
            cartoes = pd.read_excel('data/orcamento.xlsx', sheet_name='Contas')
        except FileNotFoundError:
            print('Não existem Formas de Pagamento Cadastradas')
            sleep(2)
    except ValueError:
        cartoes = pd.DataFrame()
    try:
        contas = pd.read_excel('data/orcamento.xlsx', sheet_name='Contas')
    except FileNotFoundError:
        contas = pd.DataFrame()
    except ValueError:
        contas = pd.DataFrame()

    resultado = pd.merge(contas[['cod', 'nome']], cartoes[['cod', 'nome']], how='outer').set_index('cod').sort_values(
        'cod')

    dict_resultado = resultado.to_dict()

    for chave, valor in dict_resultado['nome'].items():
        print(f'{chave}: {valor}')


def cadastrar_conta():
    sheet = 'Contas'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro
    nome = input('Digite o nome da nova conta: ')
    limite = float(input('Digite o limite atual da nova conta: '))
    saldo = float(input('Digite o saldo atual da nova conta: '))
    nova_linha = {
        'cod': id_atual,
        'nome': nome,
        'limite': limite,
        'saldo': saldo
    }

    gravar(nova_linha, sheet)

    sleep(2)
    menu_cadastro()


def cadastrar_cartao():
    sheet = 'Cartões'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro
    nome = input('Digite o nome do novo cartão: ')
    bandeira = input('Digite a bandeira do novo cartão: ')
    vcto = input('Digite o vencimento do novo cartão: ')
    limite = float(input('Digite o limite do novo cartão: '))
    nova_linha = {
        'cod': id_atual,
        'nome': nome,
        'bandeira': bandeira,
        'vencimento': vcto,
        'limite': limite,
    }
    gravar(nova_linha, sheet)
    sleep(2)
    menu_cadastro()


def cadastrar_despesa():
    sheet = 'Despesas'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro

    listar_categorias()

    categoria = int(input('Digite o código da categoria: '))
    data = input('Digite a data da despesa: ')
    descricao = input('Digite a descrição da despesa: ')

    listar_formas_pgto()

    forma_pgto = input('Digite o código da forma de pagamento: ')
    nova_linha = {
        'cod': id_atual,
        'categoria': categoria,
        'data': data,
        'descricao': descricao,
        'forma_pgto': forma_pgto,
    }
    gravar(nova_linha, sheet)
    sleep(2)
    menu_cadastro()


def cadastrar_receita():
    sheet = 'Receitas'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro
    fonte = input('Digite a fonte da nova receita: ')
    valor = input('Digite o valor da nova receita: ')
    data = input('Digite a data da nova receita: ')
    descricao = input('Digite a descrição da nova receita: ')
    consultas('Contas', False)
    conta = input('Digite o código da conta da nova receita: ')
    nova_linha = {
        'cod': id_atual,
        'fonte': fonte,
        'valor': valor,
        'data': data,
        'descricao': descricao,
        'conta': conta
    }
    gravar(nova_linha, sheet)

    sleep(2)
    menu_cadastro()


menu_principal()
