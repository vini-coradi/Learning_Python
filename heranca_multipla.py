"""
POO -> Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos das classes herdadas.

A Herança Múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta
    - Por Multiderivação Indireta



# Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass



Obs: Não importa se a derivação é direta ou indireta, a classe que realizará a herança
herdará todos os atributos e métodos das super classe.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e sou Aquatico'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando '

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Orca')
print(baleia.nadar())
print(baleia.cumprimentar())

macaco = Terrestre('Zobomafoo')
print(macaco.andar())
print(macaco.cumprimentar())

ping = Pinguim('Pingu')
print(ping.andar())
print(ping.nadar())
print(ping.cumprimentar()) # Method Resolution Order - MRO

# Objeto é instância de ...

print(f'Ping é uma instância de Pinguim? {isinstance(ping, Pinguim)}')
print(f'macaro é uma instância de Animal? {isinstance(macaco, Animal)}')
print(f'baleia é uma instância de Terrestre? {isinstance(baleia, Terrestre)}')


