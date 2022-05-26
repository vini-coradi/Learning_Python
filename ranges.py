"""
Ranges

--> Necessário conhecer o for para usar os ranges
--> Necessário conhecer o range para melhor uso do for

Ranges são utilizados para gerar sequencias numericas, de uma menira especifica.

Formas gerais:

            # Formula 1

range(valor_de_parada)

Obs: Valor de parada não incluso, inicio padrão 0... e passo de 1 em 1

for num in range(11):
    print(num)

            # Formula 2

range(valor_de_inicio, valor_de_parada)

for num in range(4, 11):
    print(num)

            # Formula 3

range(valor_de_inicio, valor_de_parada, passo)

Obs: Passo pode ser especificado pelo usuário

for num in range(1, 10, 2):
    print(num)

            # Formula 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

for num in range(10, -1, -1):
    print(num)

Exemplo bonus de criação de lista

lista=list(range(10))

"""