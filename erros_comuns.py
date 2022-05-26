"""
Erro Comum em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erro geradas pelaa execução do nosso código

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem

Exemplos SytaxError

a)

def funcao:
    print('vinicius')

b)
    def = 1

c)

return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
print(teste)

b)
teste()

c)
a = 18
if a<10:
    msg = 'é menor que 10'

print(msg)


3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado

Exemplos TypeError

a)
print(len(5))

b)
print('Vini' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento ou outro tipo de dado indexado utilizando um indice inválido

Exemplos IndexError

a)
lista = ['vini']

print(lista[5])

ou

print(lista[0][5])


5 - ValueError -> Ocorre quando uma função ou operação bult-in (integrada) recebe um argumento com tipo correto e
valor inapropriado

Exemplos ValueError

a) print(int('vini')) -> o casting  de int espera receber uma string mas não é possivel converter a string vini em numero

6 - KeyError -> Ocorre quando tentamos acionar um dicionário com uma chave inexistente

Exemplos KeyError

a)
dic = {'vini': 'cesar'}
print(dic['teste'])

7 -  AttributeError -> Ocorre quando uma variavel não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
tupla.sort()

8 - IndentationError -> Ocorre quando não respeitamos a indentação do python (4 espaços)

Exemplos de IndentationError

a)
def nova():
 print('vini')

for i in range(10):
i + 2


Obs: Exceptions e Erros são sinônimos na programação

"""

printf('vinicius')