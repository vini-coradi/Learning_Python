"""
Generators

Em aulas anteriores, vimos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

Não vimos:
    - Tuple Comprehension... por que se chamam generators!!


# Exemplo de Generators

nomes = ['carol', 'cesar', 'coradi', 'cleto', 'goncalves']

print((nome[0] == 'c' for nome in nomes))

#  List Comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))

#  Generator
res = (nome[0] == 'c' for nome in nomes)
print(type(res))

# Os dois modos geram a mesma coisa mas o generator é mais performático, ocupa menos memória

# É utilizado o list comprehension apenas quando a lista será utilizada

# O mesmo se aplica a todos os comprehension

# Assim como map, após utilizado o resultado do generator, ele é apagado
"""

# Qual a utilidade de getsizeof()? --> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([n * 10 for n in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({n * 10 for n in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({n: n * 10 for n in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof( n * 10 for n in range(1000))

print('Para fazer a mesma tarefa, temos:')
print(f'List Comprehension {list_comp} bytes')
print(f'Set Comprehension {set_comp} bytes')
print(f'Dictionary Comprehension {dic_comp} bytes')
print(f'Generator Expression {gen} bytes')

# É possivel iterar no Generator Expression ?

gen = (x * 10 for x in range(100))

for num in gen:
    print(num)