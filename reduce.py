"""
Reduce

Obs: A partir do Python3+ a função reduce() não é mais uma função integrada (bult-in). Agora temos:
que importar e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2 ..an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y)
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros:a função e o iterável.

reduce( funcao, dados)

A função reduce() funciona da seguinte forma:

    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 e o terceiro elemento de dados e guarda o res

    Isso é repetido até o final

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final reduce() irá retornar o resultado final


Alternativamente, podemos definir o reduce() como:

funcao(funcao(funcao(a1,a2), a3)


"""

# Como funciona na prática

# Utilizando o reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que recebe dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)

print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)