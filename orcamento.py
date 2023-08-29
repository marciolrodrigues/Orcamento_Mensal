from models.categorias import Categoria
from models.cartoes import Cartao
from models.contas import Conta
from models.receitas import Receita
from models.despesas import Despesa
from time import sleep
from utils.helper import verificar_id
import pandas as pd

cat1 = Categoria(1, 'Mercado', 'Alimentação', 'Alimentos comprados no mercado')
cartao1 = Cartao('VISA', 20, 1, 'Nu Bank', 2000)
conta1 = Conta(1, 'Itau', 130000, 2000)
receita1 = Receita(2, 'Salário', 11000, '20/08/2023', 'Pagamento de Salário', conta1)
despesa1 = Despesa(2, cat1, '20/01/2023', 'Mercado', cartao1)
despesa2 = Despesa(3, cat1, '14/12/2002', 'Seguro', conta1)


nome_aplicativo = ' Controle de Orçamento Mensal '


# Construção do Cabeçalho de Página
def cabecalho(submenu: str) -> None:
    print(f'*' * 100)
    print(f'{nome_aplicativo:*^100}')
    print(f'*' * 100 + '\n')
    if submenu != '':
        print(f'{submenu:*^100}\n')
    print('ESCOLHA UMA OPÇÃO')


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
    elif opcao == 0:
        menu_principal()
    else:
        print('Opção inválida!')
        sleep(2)
        menu_cadastro()


def menu_consulta():
    pass


def menu_edicao():
    pass


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
            writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
            arquivo.to_excel(writer, sheet_name=sheet, index=False)
        except AttributeError:
            arquivo.to_excel(writer, sheet_name=sheet, index=False)

    print('Cadastro efetuado com sucesso')


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
        print(arquivo.values)
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

    resultado = pd.merge(contas[['cod', 'nome']], cartoes[['cod', 'nome']], how='outer').sort_values('cod')
    print(resultado)


def cadastrar_conta():
    sheet = 'Contas'
    cabecalho(f' CADASTRO DE {sheet.upper()} ')
    id_atual = verificar_id(sheet)  # Busca no arquivo qual seria o id atual para cadastrar novo registro
    nome = input('Digite o nome da nova conta: ')
    banco = input('Digite o banco da nova conta: ')
    limite = float(input('Digite o limite atual da nova conta: '))
    saldo = float(input('Digite o saldo atual da nova conta: '))
    nova_linha = {
        'cod': id_atual,
        'nome': nome,
        'banco': banco,
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
    banco = input('Digite o banco do novo cartão: ')
    bandeira = input('Digite a bandeira do novo cartão: ')
    vcto = input('Digite o vencimento do novo cartão: ')
    limite = float(input('Digite o limite do novo cartão: '))
    nova_linha = {
        'cod': id_atual,
        'nome': nome,
        'banco': banco,
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


menu_principal()

