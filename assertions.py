"""
Assertions -> Chegangens/Questionamentos

Em Python, utilizamos a palavra reservada assertions para realizar
simples afirmações utilizadas nos testes

Utilizamos o assertions em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira o assertions retorna um None e caso seja falsa, levanta
um erro do tipo AssertionError.

# Obs: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem
de erro personalizada.

# Obs: A palavra assert pode ser utilizada em qualquer função ou código nosso... não precisa
ser exclusivamente nos testes

Se o programa Python for executado com o parâmetro -O, nenhum assertion
será valdiado. Ou seja, todas as validações já eram. 

"""

def soma_numeros(a,b):
    assert a >0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

print(soma_numeros(a,b))

def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'

comida = input('Informe o que está comendo: ')

print(comer_fast_food(comida))

# Alerta! Cuidado ao executar o 'assert'


