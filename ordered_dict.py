"""
Módulo Collections: Ordered Dict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave= {chave}: valor= {valor}')

É necessário fazer o import

OrderedDict -> É um dicionario que nos garante a ordem de inserção dos elementos


# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave= {chave}: valor= {valor}')


"""
from collections import OrderedDict

# Diferença entre dict e ordered dict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # verificando se os dicts são iguais, para o dicionario comum a ordem dos elementos não importa!!

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # A ordem dos elementos importa! Não apenas os valores !


