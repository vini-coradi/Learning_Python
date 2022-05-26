"""
Levantando os próprios erros com raise

raise -> Lança exceções

Obs: O raise não é uma função e sim uma palavra reservada como def ou qualquer outra em Python

Para simplificar, pense no raise como sendo útil para que possamos  criar nossos próprias exceções e mensagens de errro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')


# Exemplo Real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError ('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('vinicius', 'azul')

# Exemplo Real - Continuação

def colore(texto, cor):
    cores = ('verde', 'azul', 'amarelo', 'branco')
    if type(texto) is not str:
        raise TypeError ('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar em {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('vinicius', 'preto')

Obs: O raise assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""


# Exemplo Real

def colore(texto, cor):
    cores = ('verde', 'azul', 'amarelo', 'branco')
    if type(texto) is not str:
        raise TypeError ('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar em {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('vinicius', 'preto')
