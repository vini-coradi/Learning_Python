from typing import List
from time import sleep

from BANCOPY.models.cliente import Cliente
from BANCOPY.models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=============================')
    print('==============ATM============')
    print('=========BANCO===============')
    print('=============================')


    print('Selecione a opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(5)
        exit(0)
    else:
        print('Opção Inválida!')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    nome: str = input('Informe o nome do cliente: ')
    email: str = input('Informe o email do cliente: ')
    cpf: str = input('Informe o cpf do cliente: ')
    data_nascimento: str = input('Informe a data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)
    contas.append(Conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('================')
    print(conta)
    sleep(5)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta:'))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor a ser sacado: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Não existem contas cadastradas!!')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta:'))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor a ser depositado: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Não existem contas cadastradas!!')
        sleep(2)
        menu()

def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta:'))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da sua conta:'))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferencia: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta com o número {numero_o} não foi encontrada')
        else:
            print(f'A conta com o número {numero_o} não foi encontrada')
    else:
        print('Não existem contas cadastradas!!')
        sleep(2)
        menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')

        for conta in contas:
            print(conta)
            print('====================')
            sleep(1)
    else:
        print('Não existem contas cadastradas!!')
        sleep(2)
        menu()

def buscar_conta_por_numero(numero: int) -> None:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
        pass
    return c

if __name__ == '__main__':
    main()