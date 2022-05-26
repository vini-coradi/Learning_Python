"""
POO -> Polimorfismo

Poli -> Muitas

Morfis -> Formas

Quando um método presente na classe pai é implementada em classes filhas, estamos realizando
uma sobrescrita de método (Overrriding).

O overriding é a essência do polimorfismo.  
"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo ..')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Au Au')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala Miau Miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testando

mia = Gato('Mia')
mia.comer()
mia.falar()

rex = Cachorro('Rex')
rex.comer()
rex.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()