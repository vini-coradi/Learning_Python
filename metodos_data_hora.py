"""
métodos de Data e Hora



# Com o now podemos especificar um timezone
agora = datetime.datetime.now()

print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()

print(hoje)
print(type(hoje))
print(repr(hoje))



# Mudanças ocorrendo à meia noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())


print(manutencao)
print(type(manutencao))
print(repr(manutencao))


# Encontrar o dia da semana, weekday()
# Os dias da semana do método weekday começam em 0, sendo esta a segunda feira
# 0 -> segunda feira

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())




import datetime

aniversario = input('Qual a data de aniversario? dd/mm/yyyy: ')

aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month =int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira')

if aniversario.weekday() == 1:
    print('Você nasceu em uma terça-feira')

if aniversario.weekday() == 2:
    print('Você nasceu em uma quarta-feira')

if aniversario.weekday() == 3:
    print('Você nasceu em uma quinta-feira')

if aniversario.weekday() == 4:
    print('Você nasceu em uma sexta-feira')

if aniversario.weekday() == 5:
    print('Você nasceu em uma sabado')

elif aniversario.weekday() == 6:
    print('Você nasceu em uma domingo')




def format_data(data):
    if data.month ==1:
        return f'{data.day} de Janeiro de {data.year}'
    if data.month ==2:
        return f'{data.day} de Fevereiro de {data.year}'
    if data.month ==3:
        return f'{data.day} de Março de {data.year}'
    if data.month ==4:
        return f'{data.day} de Abril de {data.year}'
    if data.month ==5:
        return f'{data.day} de Maio de {data.year}'
    if data.month ==6:
        return f'{data.day} de Junho de {data.year}'
    if data.month ==7:
        return f'{data.day} de Julho de {data.year}'
    if data.month ==8:
        return f'{data.day} de Agosto de {data.year}'
    if data.month ==9:
        return f'{data.day} de Setembro de {data.year}'
    if data.month ==10:
        return f'{data.day} de Outubro de {data.year}'
    if data.month ==11:
        return f'{data.day} de Novembro de {data.year}'
    if data.month ==12:
        return f'{data.day} de Dezembro de {data.year}'

# Formatando datas/horas com strftime() (String Format Time)

hoje = datetime.datetime.today()

print(hoje)

hoje_format = hoje.strftime('%d/%m/%Y')

print(hoje_format)

from textblob import TextBlob

def format_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"




hoje = datetime.datetime.today()

print(format_data(hoje))



nascimento = datetime.datetime.strptime('14/02/1996', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)


# Somente hora

almoco = datetime.time(12,30,0)

print(almoco)


# Marcando tempo de execução do nosso código com timeit

# loop for

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(tempo)


# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=1000)
print(tempo)

"""



import timeit, functools

def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma

print(timeit.timeit(functools.partial(teste, 2), number=100))

