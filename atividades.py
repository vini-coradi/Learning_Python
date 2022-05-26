def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma'
    else:
        final = 'só se vive uma vez'

    return f'Estou comendo {comida} por que {final}'

def dormir(horas):
    pass

def engracada(pessoa):
    comediantes = ['Adam Sandler', 'Danilo Gentili']
    if pessoa in comediantes:
        return True
    return False

