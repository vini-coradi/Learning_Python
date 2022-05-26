"""
Documentando funções com Docstrings


Obs: Podemos ter acesso a uma documentação de uma função em Python
Utilizando a propriedade especial __doc__

 print(diz_ola.__doc__)

"""

# Exemplos

def diz_ola():
    """Uma funcao que exibe na tela Ola"""
    return 'Olá!'

print(diz_ola())

print(help(diz_ola()))


def exponencial(num, pot):
    """
    Função que retorna o quadrado de um numero ou o numero a potencia informada
    :param num: numero que sera elevado ao expoente
    :param pot: potencia que queremos gerar o exponencial, por padrao 2
    :return:retorna o exponencial de um numero pela potencia
    """
    return num ** pot