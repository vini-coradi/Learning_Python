"""
Sorted

Obs: Não confundir com a função sort() que já estudamos em Listas. o sort() só funciona em Listas

Podemos utilizar o sorted() com qualquer iterável

Como o próprio nome já diz, sorted() serve para ordenar.

Obs: O sorted não altera o elemento principal, mas retorna uma nova lista com os elementos do iterável ordenados


# Exemplos

numeros = [6, 1, 8, 2]

print(numeros)

print(sorted(numeros)) # Ordenar do maior para o menos

print(numeros)


# Exemplos

numeros = [6, 1, 8, 2]

# Adicionando parâmetros ao sorted()

print(tuple(sorted(numeros, reverse=True))) # Ordenado do maior para o menos e Cast para tupla

print(numeros)

"""
# Exemplos mais complexos


usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"] },
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], 'cor': 'amarelo'},
    {"username": "doggo", "tweets": ["Eu gosto de gatos", "Vamos sair hoje ?"] },
    {"username": "gal", "tweets": [], 'cor': 'preto', 'musica': 'rock'}
]

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key= lambda usuario: usuario['username'],  reverse=True))

# Ordenando por número de tweets
print(sorted(usuarios, key= lambda usuario: len(usuario['tweets'])))


# Último exemplo

musicas= [
    {'titulo':'Thunderstruck', 'tocou': 3},
    {'titulo':'Dead skin mask', 'tocou': 2},
    {'titulo':'Back in Black', 'tocou': 4},
    {'titulo':'Starway to Heaven', 'tocou': 32}
]

# Ordenação em Ordem Alfabética
print(sorted(musicas, key= lambda musica: musica['titulo']))


# Ordenação da menos tocada para a mais tocada
print(sorted(musicas, key= lambda musica: musica['tocou']))