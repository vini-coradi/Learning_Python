"""
Decorators com diferentes assinaturas



# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return  f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando

print(saudacao('vini'))

print(ordenar('carne', 'queijo'))





# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.


# Refatorando com Decorator Pattern


# Relembrando

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return  f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


# Testando

print(saudacao('vini'))

print(ordenar('carne', 'queijo'))

print(ordenar(acompanhamento='purê', principal='filé'))


"""

# Decorator com argumentos

def verifica_primeiro_arg(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro valor deve ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_arg('pizza')
def comida_fav(*args):
    print(args)

@verifica_primeiro_arg(10)
def soma_dez(num1, num2):
    return  num1+num2

print(soma_dez(10,12))  #22

print(soma_dez(1,21))