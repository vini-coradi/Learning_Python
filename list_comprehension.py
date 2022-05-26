"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterávvel

# Sintaxe da List Comprehension

[ dado for dado in interável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- 1ª parte: for numero in numeros
- 2ª parte: numero *10

def funcao(valor):
    return valor*valor

res = [funcao(numero) for numero in numeros]

print(res)


# List Comprehension vs Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numeros in numeros:
    numeros_dobrado = numeros * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)

# List Comprehension

print(numero *2 for numero in numeros)

"""

# Outros Exemplos

# 1

nome = 'Vini Cesar'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print([numero *3 for numero in range(1,10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 2, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])

"""
Parte 2 !
Estruturas condicionais logicas nas List Comprehension

"""

# Exemplo 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando
# Qualquer numero par por módulo de 2 é 0, e 0 em Python é false.  // not false = true
pares  = [numero for numero in numeros if not numero % 2]
pares  = [numero for numero in numeros if  numero % 2]


# Exemplo 2

res = [numero *2 if numero % 2 == 0 else numero/2 for numero in numeros]

print(res)