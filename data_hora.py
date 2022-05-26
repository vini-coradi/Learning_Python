"""
Manipulando Data e Hora

Python tem um módulo built-in para se trabalhar com data e hora
chamado datetime



import  datetime

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente

print(datetime.datetime.now())

# datetime.datetime (year, month, day, hour, minute, second, microsecond)

print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para as 16 horas, 0 minutos, 0 segundos, 0 microsegundo

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)


# Recebendo dados do usuário e convertendo para data

import datetime

evento = datetime.datetime(2021, 1, 1, 0)

print(type(evento))

aniversario = input('Informe sua data de nascimento (dd/mm/yy): ')

print(aniversario)

aniversario = aniversario.split('/')

aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))

print(aniversario)

print(type(aniversario))

"""

import datetime

evento = datetime.datetime.now()


print(evento.year)
print(evento.month)
print(evento.day)
print(evento.second)
print(evento.microsecond)
