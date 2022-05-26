
"""
# correto

texto: str

# Incorreto

texto:str

texto : str

# Correto

) -> str

# Correto

alinhamento: bool = True
"""

import math

def circuferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(circuferencia.__annotations__)


class Pessoa:
    # A classe pessoa não tem anotations mas os métodos tem anotations

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f'{self.__nome} está caminhando'

p = Pessoa(nome = 'Vinicius Cesar', idade=25, peso=69.5)

print(p.__dict__)



nome: str = 'Vini'

peso: float = 69.5

ativo: bool = True

print(__annotations__)