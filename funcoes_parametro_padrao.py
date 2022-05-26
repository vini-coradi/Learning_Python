"""
Funcoes com Parâmetro Padrão ((Default Parameters)

Funcoes onde a passagem do parametro é opcional:

#Exemplo onde a passagem do parametro é opcional:
print('bom dia')
 e
print()

#Exemplo com paraametro obrigatorio !

def quadrado(numero):
    return numero ** 2

print(quadrado(3)) # caso nao informado o parametro = #TypeError


def exponencial(numero, potencia = 2):  # quando um parametro recebe um valor, ele se torna OPCIONAL
    return numero ** potencia

print(exponencial(2,3))

print(exponencial(3)) # Por padrao eleva ao quadrado
print(exponencial(2,8)) # Eleva à potência informada pelo usuário

# Obs
# Se o usuario passar apenas 1 argumento, este será atribuido ao parametro numero e será calculado o quadrado do numero
# Se o usuario passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência.

# OBS: em funções Python, os parâmetros com valores default devem sempre estar ao final da declaração

# Erro
def teste(num=2, potencia):
    return num ** potencia

# Exemplo

def mostra_informacao(nome ='vini', dia=False):
    if nome == 'vini' and dia:
        return 'Bom dia, Vini'
    elif nome == 'vini':
        return 'Eu pensei que era dia'
    return f'Adeus, {nome}'

print(mostra_informacao('cesar'))
print(mostra_informacao(dia=True))
print(mostra_informacao(True))

Vantagens de utilizar valores defaults
-- Permite maior flexibilidade nas funções
--Evita erros com parâmetros incorretor
-- Nos permite trabalhar com exemplos mais legiveis de código

Podemos utilizar qualquer tipo de código:
-- Números, strings, floats, booleanos, listas, tuplas, dicionários, funções, etc


# Exemplo

def soma(num1, num2):
    return num1+num2
def mat(num1, num2, fun=soma):
    return fun(num1,num2)
def sub(num1, num2):
    return num1-num2

print(mat(2,3))
print(mat(10,7,sub))

# Escopo

#Variaveis globais e locais

pessoa = 'vini'

def diz_ola():
    pessoa= 'cesar'
    return f'Olá, {pessoa}'

print(diz_ola())  # Se tivermos o mesmo nome em uma variável local e em uma global, a local terá preferência


# Atenção com variaveis locais, se puder evitar... Evite !

total = 0

def incrementa():
    global total
    total =total +3
    return total

print(incrementa())
print(total)


"""

# Podemos ter funções declaradas dentro de funções e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador +2
        return contador
    return dentro()

print(fora())