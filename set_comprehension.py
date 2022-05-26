"""
Set Comprehension

Semelhante a dictionary e list comprehension

"""

# Exemplos

numeros = {num for num in range(1,7)}
print(numeros)

# Outro Exemplo

numeros = { x ** 2 for x in range(10)}
print(numeros)

# pra finalizar

letras = {letra for letra in 'vini cesar'}
print(letras)

