"""
Loop for

Loop-> Laço de repetição

Em C/Java
for(int i=0;i<10;i++)

Python

for item in interavel
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis

Exemplos de iteráveis:

--String
--Lista
--Range

"""

nome = 'Vinicius Gonçalves'
lista = [1, 3, 5, 7, 8]
numeros = range(1,10) #temos que transformar em lista

# Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)
"""
range (valor inicial, valor final)

O valor final não está incluso!!!!
"""

for numero in range(1, 10):
    print(numero)

"""
Enumerate:
cria uma lista onde l[0] = indices, l[1]=  conteudos

((0, 'V'), (1, 'i'), (2, 'n')...

"""
# Quando não precisamos de um valor, podemos descarta-lo com enumerate
"""
ex:
 for _, letra in enumerate(nome):
 for indice, letra in enumerate(nome):

"""
for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes o loop irá rodar ?"))
soma = 0

if qtd > 1:
    for n in range(1, qtd+1):
        num = int(input(f"Informe o valor a ser somado"))
        soma += num
else:
    num = int(input(f"Informe o valor a ser somado"))
    soma += num
print(f"A soma total é {soma}")

for letra in nome:
    print(letra, end='')

# Tabela de Emojis Unicode https://apps.timwhitlock.info/emoji/tables/unicode

# Original U+1F602
# Modificado U0001F602



for num in range(1,11):
    print('\U0001F602' *num)