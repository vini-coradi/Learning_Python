"""
POO -> Propriedades (Properties)

Em linguagens de programação, como o Java, costumamos criar métodos públicos para
manipulação desses atributos. Esses métodos são conhecidos como getters e setters, onde
os getters retornam o valor do atributo e os setters alteram o valor do mesmo




class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
         return f'O Cliente {self.__titular} possui o seguinte Saldo:{self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self,valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get__saldo(self):
        return self.__saldo

    def get__limite(self):
        return self.__limite


conta1 = Conta('vini', 500, 1000)

conta2 = Conta('cesar', 1500, 3000)

print(conta1.get__saldo())
"""



class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite


    def extrato(self):
         return f'O Cliente {self.__titular} possui o seguinte Saldo:{self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self,valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta1 = Conta('vini', 500, 1000)

conta2 = Conta('cesar', 1500, 3000)

print(conta1.saldo +conta2.saldo)

conta1.limite = 9876
print(conta1.limite)

print(conta1.valor_total)

print(conta2.valor_total)