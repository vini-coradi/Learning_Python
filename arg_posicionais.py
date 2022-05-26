"""
Argumentos somente posicionais:


"""

def cumprimenta_v1(nome):
    return f'Olá {nome}'

#print(cumprimenta_v1('Vini'))
#print(cumprimenta_v1(nome='Vini'))

def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


#print(cumprimenta_v2('Vini'))
#print(cumprimenta_v2(nome='Vini'))


def cumprimenta_v3(nome, mensagem= 'Olá', /):
    return f'Olá {nome}'


#print(cumprimenta_v3('Vini'))
#print(cumprimenta_v3(nome='Vini'))
#print(cumprimenta_v3(mensagem='Bom dia!'))



def cumprimenta_v4(*, nome):
    return f'Olá {nome}'

print(cumprimenta_v4(nome='Vini C!'))
print(cumprimenta_v4())
