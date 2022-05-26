"""
Trabalhando com módulos Built-in
São módulos integrados, que já vem instalados no Python.


________________________
|Python|Módulos builtin|
------------------------


# Utilizando alias (apelidos) para módulos/ funções

import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Utilizando alias (apelidos) para funções

from random import randint as rdi, random as rdm

print(rdi(5, 15))
print(rdm())



http://docs.python.org/3/py-modindex.html

"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo


from random import(
    random,
    randint,
    choice,
    shuffle
)

print(random())

print(randint(4, 8))

lista = ['vini', 'cesar', 'coradi', 'gonçalves']

print(lista)

shuffle(lista)

print(lista)

print(choice(lista))