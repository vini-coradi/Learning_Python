"""
Entendendo o *args

O *args é parametro como outro qualquer, isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco (*)

Exemplo:
*xis

Por convenção utilizamos  *args para defini-lo

O parametro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla, lembrando que tuplas são imutáveis


# Exemplos

def soma_todos_num(nome, email, *args):
    return sum(args)

print(soma_todos_num('vini','vini123',5,3))
print(soma_todos_num('vini','vini123'))


# Outro exemplo com *args

def verifca_info(*args):
    if 'teste' in args and 'um' in args:
        return 'teste bem sucedido'
    return 'Erro, por favor, confira!'

print(verifca_info())
print(verifca_info(1, True, 'teste', 'um', 'dois'))
print(verifca_info(3.45, 'teste', 5*4))

"""
def soma_num(*args):
    return  sum(args)

numeros = [1, 2, 3, 4, 5]


#Desempacotador

print((soma_num(*numeros)))

# Obs: O asterisco serve para informar ao python que estamos passando como argumento uma coleção de dados.
# Dessa forma ele saberá que precisará antes desempacotar os dados