"""
**kwargs

Poderiamos chamar este parametro de **xis mas por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do * args que coloca valores extras em uma tuplas
o **kwargs exige que utilizemos parametros nomeados, e transforma esses parametros extras em um dicionário


# Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# os parametros **kwargs não são obrigatorios


# Outro exemplo:

def comprimento(**kwargs):
    if 'linguagem' in kwargs and kwargs['linguagem'] == 'python':
        return ("A linguagem é python!")
    elif 'linguagem' in kwargs:
        return f"A linguagem é {kwargs['linguagem']} "
    return ("Não é uma linguagem")


print(comprimento(linguagem='c'))
print(comprimento(linguagem='java'))
print(comprimento(linguagem='python'))
print(comprimento(teste='c'))


    # As funções podem ter (NESSA ORDEM)

-Parametros obrigatórios
- *args
-Parametros Default
-- *kwargs

# Exemplo

def main_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade}')
    print(*args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(**kwargs)

main_funcao(8,'Vini')
main_funcao(8, 'cesar', 4, 5, 3, solteiro=True)
main_funcao(8, 'coradi', 4, 5, 3, solteiro=True)
main_funcao(8, 'Vinicius', eu='Never', voce='chablau')
main_funcao(8, 'O Vini', 1, 2,3 ,java=False, voce='chablau')


# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return  f"{kwargs['nome']} {kwargs['sobrenome'] }"

nomes = {'nome': 'Jão', 'sobrenome': 'Grilo'}

print(mostra_nomes(**nomes))

"""
def soma_num(a,b,c):
    print(a +b+ c)

lista = [1,2,3]
tupla = 1,2,3
conj = {1,2,3}
dic = dict(a=1,b=2,c=3)

soma_num(*lista)
soma_num(*tupla)
soma_num(*conj)
soma_num(**dic)

# OBS: Os nomes das chaves em um dicionário devem ser os mesmos dos parametros da função, caso contrário retorna erro

