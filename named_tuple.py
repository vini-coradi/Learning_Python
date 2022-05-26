"""
Módulo Collections  -  Named Tuple

Recapitulando Tupla

tupla = (1, 2, 3)

print(tupla[2])

Named Tuple -> São tuplas diferenciadas onde, especificamos um nome para a mesma e parÂmetros

Necessáio fazer o import
"""

from collections import namedtuple

# Precisamos definir o nome e parametros

# Forma 1  -  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2  -  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3  -  Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando a tupla

ray = cachorro(idade=2, raca='Chow Chow', nome='Ray')

print(ray)

# Acessando os dados, Forma 1

print(ray[0]) #idade
print(ray[1]) #raca
print(ray[2]) #nome

# Acessando os dados, Forma 2

print(ray.idade) #idade
print(ray.raca) #raca
print(ray.nome) #nome

print(ray.index('Ray'))