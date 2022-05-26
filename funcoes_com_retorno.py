"""
Funcoes com retorno

OBS: Em python quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções python que retornam valores, devem retornar através da palavra reservada ' return'

OBS: Não precisamos necessariamente criar uma variável pra receber o retorno de uma função
Podemos passar a execução da função para as outras funções


numeros = [1, 2, 3]

ret_pop = numeros.pop()

ret_print = print(numeros)

print(f'Retorno do pop {ret_pop}')
print(f'Retorno do pop {ret_print}')

# Exemplo de função


def quadrado_de_7():
    return (7*7)

ret = quadrado_de_7() # Criamos uma variável para receber o retorno da função

print(f'Retorno {ret}')

print(f'Retorno 2 {quadrado_de_7() +1}')


# Refatorando a primeira função


def diz_ola():
    return 'Olá!'


print(diz_ola())


                 A palavra return

# Exemplo 1 1- Ela finaliza a função, ou seja, o return termina a execução da função


def diz_ola():
    print("Estou sendo executado antes do retorno")
    return 'Olá!'
    print('Estou sendo executado pós return')

print(diz_ola())

# Exemplo 2 2- Podemos ter em uma função, diferentes returns

def nova_funcao():
    variavel =  False
    if variavel:
        return 4
    else:
        return 3.2
    return 'w'

print(nova_funcao())

# Exemplo 3 3- Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores!!

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(outra_funcao())


# Vamos criar uma função para jogar moeda

from random import random


def joga_moeda():
    # Gera um valor pseudo-randomico entre 0 e 1
    if random()<0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


"""

# Erros comuns ao utilizar o return

def eh_impar():
    num = 4
    if num % 2 != 0:
        return True
    #else --> o else não é necessário nesse caso
    return False


