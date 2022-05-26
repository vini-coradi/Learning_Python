"""
O operador walrus permite fazer a atribuição e retorno de valor em uma única expressão

variavel:= expressão

"""

print(nome:= 'Vinicius Goncalves')

# Python 3.8

cesta = []

while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)