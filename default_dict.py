"""
Módulo Collections - Default Dict

#Repcapitulando dicionario

dicionario = {'curso': 'Programa em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro'])

Default Dict --> Ao criar um dicionario utilizando-o, nós informaremos um valor default,
podemos utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido!
Ao tentar acessar uma chave que não existe, essa chave será criada e o valor default
será atribuido

*** Obs: Lambda são funções sem nome, que podem ou não receber parametros de entrada e
retornar valores

é necessário fazer o import

"""

# Fazendo o import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial '

print(dicionario)

print(dicionario['outro'])

print(dicionario)