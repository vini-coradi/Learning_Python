"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu ruim aqui')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro


# Exemplo 2 - Tratando um erro genérico

try:
    len(5)
except:
    print('Deu ruim aqui')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro


oBS: Tratar erros de forma genérica, não é a melhor forma de tratamento de erro. O ideal é SEMPRE tratar
de forma específica.



# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')



# Exemplo 4 - Tratando um erro específico

try:
    len(5)
except TypeError:
    print('Você está utilizando a função errada')


# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação retornou o seguinte erro: {err}')


try:
    #len(5)
    #geek()
    print('vinicius'[20])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'vini'}

print(pega_valor(8, 'GAMEPY'))


print(pega_valor(dic, 'GAMEPY'))