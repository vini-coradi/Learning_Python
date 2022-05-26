"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas listas

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator


"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Obs: Em conjuntos, não definimos a ordem dos elementos
# Conjunto (Set)
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('vinicius goncalves'):
    print(letra,end= '')

print('\n')

# Fazendo o mesmo sem for
print(''.join(list(reversed('\nvinicius goncalves'))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('vinicius goncalves'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0,10)):
    print(n)

# Apesar de já ter visto que podemos fazer isso com o próprio range()
for n in range(9,-1,-1):
    print(n)