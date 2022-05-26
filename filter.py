"""
Filter
filter() -> Serve para filtrar dados de uma determinada coleção


# biblioteca própria para dados estatisticos

import statistics

# Dados de um sensor qualquer
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')
# Obs: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda valor: valor > media, dados)

print(list(res))

# Obs: Assim como na função map, após ser utilizada a resposta do filter, ele é excluido da memória

# Forrma 1

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

# Forma 2 - Menos usual

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']


res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais!='', paises)


print(list(res))

# Diferença entre map() e filter()

# map() -> Recebe dois parâmetros, uma função e um iterável, e retorna um objeto mapeando a função para cada elemento do iterável

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função


# Exemplo complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"] },
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de gatos", "Vamos sair hoje ?"] },
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários inativos no twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2 -  Abaixo é testado se está vazio. O not vazio =  True... assim onde não há tweets o filtro é aplicado
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)


"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = (list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))))

print(lista)
