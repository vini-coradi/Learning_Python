"""
Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas

# Função em Python:

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda para a função acima

lambda x: 3 * x + 1

# E como utilizamos a expressão Lambda?

calc = lambda x: 3 * x + 1

print(calc(4))


# Podemos ter expressões Lambda com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


# Em funções Python podemos ter nenhuma ou várias entradas. Em lambda também:

amar = lambda: 'Como nao amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3/(1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ... ,xn: <expressao>

print(amar())
print(uma(6))
print(duas(5,7))
print(tres(3,6,9))

# Obs se se passarmos quantidade de parametros diferente do esperado, teremos TypeError


# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key= lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

# Função Quadrática

# f(x) = a * x **2 + b * x + c

def funcao_quadratica(a, b, c):
    """Retorna a função f(x)= a * x **2 + b * x + c"""
    return lambda x:a * x ** 2 + b * x + c

teste = funcao_quadratica(2,3,-5)

print(teste(0))
print(teste(1))
print(teste(2))

print(funcao_quadratica(3,0, 1)(2))