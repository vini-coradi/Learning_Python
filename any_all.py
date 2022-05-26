"""
Any e All


all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplo all()

print(all([0,1,2,3,4])) # Todos os elementos são verdadeiros ? False --> possui o 0 que é  False

print(all([1,2,3,4])) # Todos os elementos são verdadeiros ? True

print(all('Vini'))

print(all([]))

nomes = ['carol', 'cesar', 'coradi', 'cleto']

print(all(nome[0] == 'c' for nome in nomes)) # Case sensitive!!


any() -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False
"""


print(any([0,1,2,3,4])) # True

print(any([0, False, {}, (), []])) # False


nomes = ['vini', 'cesar', 'coradi', 'goncalves']

print(any(nome[0] == 'c' for nome in nomes)) # Case sensitive!! - True

