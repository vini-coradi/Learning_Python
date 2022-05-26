"""
Preservando metadata com wraps

Metadatas -> São dados intrínsecos em arquivos

Wraps -> Funções que envolvem elementos com diversas finalidades



# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função dentro da outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Você está chamando {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    # Soma dois numeros
    return a + b


# print(soma(10,30))

print(soma.__name__) #soma
print(soma.__doc__) #soma dois números

"""


# Resolução do problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função dentro da outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Você está chamando {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """Soma dois numeros"""
    return a + b


# print(soma(10,30))

print(soma.__name__) #soma
print(soma.__doc__) #soma dois números
