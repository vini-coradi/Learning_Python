"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois os mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 128]
print(max(lista))       # 128

# Funciona analogamente para tuplas, conjuntos

# Para dicionario

dic = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':128}
print(max(dic.values()))       # 128

# Faça um programa que recebe dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1,val2))

print(max('a', 'ab', 'abc'))

print(max('vinicius'))

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos


# Exemplos

lista = [1, 8, 4, 99, 34, 128]
print(min(lista))       # 1

# Funciona analogamente para tuplas, conjuntos

# Para dicionario

dic = {'a':1, 'b':8, 'c':4, 'd':99, 'e':34, 'f':128}
print(min(dic.values()))       # 1

# Faça um programa que recebe dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1,val2))

print(min('a', 'ab', 'abc'))

print(min('vinicius'))


# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivandor']

print(max(nomes))       # Leva em consideração a ordem alfabética!

print(min(nomes))       # Leva em consideração a ordem alfabética!

print(max(nomes, key = lambda nome: len(nome)))     # Tamanho do Nome

print(min(nomes, key = lambda nome: len(nome)))     # Tamanho do Nome

# max e min aceitam lambda, na dúvida, podemos consultar via terminal ( help(max) )
# Ou então segurar o botão Cntrl e clicar na função max
"""


musicas= [
    {'titulo':'Thunderstruck', 'tocou': 3},
    {'titulo':'Dead skin mask', 'tocou': 2},
    {'titulo':'Back in Black', 'tocou': 4},
    {'titulo':'Starway to Heaven', 'tocou': 32}
]

# Imprimindo apenas o titulo da música mais e menos tocada

print(max(musicas, key = lambda musica: musica['tocou'])['titulo'])

print(min(musicas, key = lambda musica: musica['tocou'])['titulo'])

# Desafio como encontrar a música mais tocada sem usar max, min e lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])