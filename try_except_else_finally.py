"""
Try  // Except // Else // Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA

Principalmente entradas de usuário. Já que o usuário pode estar mal intencionado

# Else -> executado apenas se não ocorrer o erro (except)

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor Incorreto !!')
else:
    print(f'Voce digitou {num}')

# Finally

try:
    num = int(input('Informe o número: '))
except ValueError:
    print('Valor Incorreto!!')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o programa!!')

# O bloco finally é sempre executado, ocorrendo exceção ou não!

# O finally geralmente é utilizado para fechar ou desalocar recursos!


# Exemplo mais complexo Forma Errada
# Obs: voce deve ser responsavel pelas entradas de suas funções, por isso trate-as!


def divisao(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu o seguinte erro: {err}')



num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')


print(divisao(num1, num2))


"""

