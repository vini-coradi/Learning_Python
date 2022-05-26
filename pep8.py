"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

--> import this

O ideal é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para os nomes de classes

[2] - Utilize nomes em minusculos, separados por _ para funções e variáveis

[3] Utilize 4 espaços para identação!!!  -- - -- -- IMPORTANTE -- -- - --
        Usar espaços e não TAB

[4] Separar funções e definições de classe com duas linhas em branco
    Métodos dentro de uma classe devem ser separados com uma única linha em branco

[5] Imports devem ser feitos em linhas distintas
    Não há problemas em importar itens diferentes de um mesmo pacote, ex:

    from types import StringType, ListType      ou
                        ou
from Types import(
    StringType
    ListType
    SetType
)

    Imports devem ser colocados no topo do arquivo

[6] Não deixe espaços em argumentos de funções e/ou instruções, exemplo:
funcao(algo[1], {outro[2]})



class Calculadora:
    pass


b = 4
a = 3


def soma_dois():
    pass

"""