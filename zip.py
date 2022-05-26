"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega um elemento de cada um dos iteráveis passados como entrada em pares


# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar lista, tupla ou dicionário

print(list(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))

zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

lista3 = [7, 8, 9, 10, 11]

# Obs: O zip utiliza como parâmetro o menos iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor
# iterável acabar
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

zt = zip(tupla, lista, dicionario.keys())
print(zt)

# Lista de Tuplas
dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]

print(list(zip(*dados)))

"""


# Exemplos Complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))