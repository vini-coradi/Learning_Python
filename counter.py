"""
Módulo Collections -- Counter (Contador)

Collections --> High- Performance Container Datetypes

Counter --> recebe um iterável como parametro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências do elemento

# Realizando o import

from collections import Counter  #  necessário o import de uma biblioteca

# podemos utilizar qualquer iteravel, no caso uma lista
lista = [1, 1, 2, 3, 4, 5, 2, 4, 5, 2, 3, 4, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 2, 4, 5, 6, 6, 6, 3]

# Utilizando o Counter
res = counter(lista)

print(type(res))

print (res)

# EM UM TEXTO PODEMOS TER:
textto = """

"""
palavras= texto.split()
res = Counter (palavras)

comum = (res.most_commom(5)) - identifica as 5 palavras mais comuns do texto

"""
