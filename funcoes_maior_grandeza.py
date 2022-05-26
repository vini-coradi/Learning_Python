"""
Funções de maior grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programaçãosuporte HOF - indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas

Obs: Na seção funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe ou First Class Citizen


# Exemplo - Definindo funções

def somar(a,b):
    return a + b

def diminuir(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(1,3,somar))



Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas)


# Nested Functions - Funções Aninhadas

# Exemplo

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E aí? ', 'Suma daqui! ', 'Gosto de você '))
    return humor() + pessoa

# Testando

print(cumprimento('Vini'))



# Retornando funções de outras funções

from random import choice

def faz_rir():
    def rir():
        return choice(('rs', 'haha', 'kkk'))
    return rir

rindo =  faz_rir()
print(rindo())
"""

# Inner Functions ou Nested Functions podem acessar escopos de funções mais externas

from random import choice

def faz_rir(pessoa):
    def rir():
        riso = choice (('rs', 'haha', 'kkk'))
        return f'{riso} {pessoa}'
    return rir

# Testando

rindo = faz_rir('Vini')

print(rindo())

print(rindo())