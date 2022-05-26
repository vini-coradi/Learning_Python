"""
Trabalhando com deltas de data e hora

delta = data_final - data_inicial




import datetime

data_hoje = datetime.datetime.now()

# Data para um determinado evento

aniversario = datetime.datetime(2021, 5, 12, 0)

tempo = aniversario - data_hoje

print(type(tempo))

print(repr(tempo))


"""


import datetime

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = (datetime.timedelta(days=3))

print(regra_boleto)

vencimento = data_compra + regra_boleto

print(vencimento)