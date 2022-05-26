"""
POO -> Abstracao e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico
utilizando classes.

Encapsular -> cápsula


            Classe
---------------------------------
|                               |
|       atributos e métodos     |
|_______________________________|


# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método privado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. Com Python acontece um fenômeno chamado
Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Classe__elemento

Exemplo:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados do usuário.




# Teste

conta1 = Conta('Vini', 1000, 3000)

conta1.extrato()

conta1.depositar(500)

conta1.extrato()

conta1.sacar(8000)

conta1.extrato()
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}! O número da conta '
              f'é {self.__numero}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo Insuficiente')
        else:
            print('O valor deve ser positivo')

    def transferencia(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferencia para por quem transferiou valor
        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor



# Teste

conta1 = Conta('Vini', 1000, 3000)

conta1.extrato()

conta2 = Conta('Cesar', 3000, 5000)

conta2.extrato()

conta2.transferencia(500, conta1)

conta1.extrato()

conta2.extrato()