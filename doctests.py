"""
Doctests

Doctests são testes que colocamos na docstring do python das funções/métodos Python.

Para rodar um doctest:

python -m doctest -v doctests.py


def soma(a,b):
   #   soma os números a e b

    # >>> soma(1,2)
    # 3

    return a + b

print(soma(3, 4)) # 7


# Outro exemplo aplicando o TDD

def duplicar(valores):
    #Duplica os valores em uma lista

    # >>> duplicar([1, 2, 3, 4])
    # [2, 4, 6, 8]
    # >>> duplicar([])
    # []

    # >>> duplicar(['a', 'b', 'c'])
    # ['aa', 'bb', 'cc']

    # >>> duplicar[(True, None)]
    # Traceback (most recent call last):
        ...
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'


    return [2 * elemento for elemento in valores]




# Erro inesperado

def fala():
    # Fala oi

    # >>> fala()
    # 'oi'
    #
    # return "oi"
    
# Obs: Dentro do doctest, o Python não reconhece a string com aspas duplas. Precisa ser aspas simples.

"""

def verdade():
    """Retorna a verdade

    >>> verdade()
    True
    """
    return True