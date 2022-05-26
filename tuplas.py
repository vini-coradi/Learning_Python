"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas, com duas diferenças básicas:

1- As tuplas são representadas por parênteses()

2- As tuplas são imutáveis. Ao criar uma tupla, ela não muda!
    Toda alteração em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)

tupla2 = 1, 2, 3, 4, 5, 6   # Ambos são tuplas

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!

tupla4 = (4,)  # Isso é uma tupla!!

tupla5 = 4,  # Isso é uma tupla

# Conclusão -> Tuplas são definidas com virgula!


Podemos gerar uma tupla dinamicamente com o range (inicio, fim, passo)
tupla6 = tuple(range(11))


É possivel o desempacotamento da tupla

# É Possivel calcular soma, valor max e valor min, e tamanho
sum(tupla)
max(tupla)
min(tupla)
len(tupla)

#Concatenação de tuplas
É possivel concatenar tupla3 = tupla1+tupla2

#Tuplas são imutaveis mas podemos sobrescrever seus valores

# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados continudos numa seleção

#Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Mario', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)


# Por que utilizar tuplas ?

# Tuplas são mais rápidas do que listas
# Tuplas deixam o seu código mais seguro
# Trabalhar com elementos imutáveis deixa seu código mais seguro

Na tupla não há Shallow Copy

"""

