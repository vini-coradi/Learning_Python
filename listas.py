"""
Listas em Python funcionam como vetores (arrays), com a diferença de serem
dinâmicos e também podemos colocar QUALQUER tipo de dado

Linguagens C/Java: Arrays
    -Possuem tamanho do tipo fixo;
    -Ou seja se criar uma array do tipo int e com tamanho 5, ese array SEMPRE será do tipo int
    e terá SEMPRE no maximo 5 valores

- Dinâmico:
    -Não possui tamanho fixo, ou seja, pode ser criada a lista e ir adicionando elementos!
    - QUALQUER TIPO DE DADOS: não possuem tipo de dado fixo!

As listas em Python são representadas por []

# Podemos checar se há um valor em uma lista:
num = 18

if num in lista4:
    print(f"Existe o número {num} na lista4")
else:
    print(f"Não exite o {num} na lista4")

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Podemos facilmente contar o n. de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('i'))

# Adicionar elementos em lista

Para adicionar elementos em lista, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# Para passar mais elementos de uma vez
lista1.append([8, 3, 1])                # Coloca a lista como elemento unico - sublista
print(lista1)

if [8, 3, 1] in lista1:
    print("Lista Encontrada")
else:
    print("lista não encontrada")

lista1.extend([123, 44, 67])            # Acrescenta como valores da lista primaria
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# Não substitui o valor daquela posição, mas é deslocado para a direita
lista1.insert(2, 'new value')
print(lista1)

# Para juntar duas listas:

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)

Para inverter uma lista podemos usar o reverse
ou
print(lista1[::-1])

Para saber o tamanho de uma lista:
print(len(lista1))

lista1.pop(x) --> retorna o  elemento  x de uma lista e o remove da lista (como default usa o ultimo elemento)
Os elementos à direita, são deslocados para a esquerda
Se não houver elemento no indice informado, teremos IndexError


Podemos zerar todos os elementos de uma lista:
lista1.clear()

Podemos repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova*3
print(nova)

-- Convertendo String para lista
split()
Obs: Por padrao separa os elementos da lista pelo espaço entre palavras
split(',')
Nesse caso, o separador é a virgula

-- Convertendo lista pra String
curso = ' '.join(lista6)   #No exemplo, é inserido espaço entre os elemestos da lista na String

# Exemplo de while

carrinho = []
produto = ''
while produto!= 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair :")
    produto =  input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#Variaveis em lista

num1 = 1
num2 = 2
num3 = 3
num4 = 4
numeros = [num1, num2, num3, num4]

# Gerar um enumerate em um for
for indice, cor in enumerate(cores):
    print(indice, cor)


# Encontrar  o indice de um elemento em uma lista, caso o elemento não exita retorna ValueError
# Se possuir mais de um elemento igual, ele retorna o indice do primeiro
# se não informado o valor de x, ele começará desde o elemento 0
# se não informado o valor de y, ele terminará a busca apenas ao achar o elemento

print(lista1.index(27, x, y))

Para valores inteiros ou reais
int(sum(lista))
int(max(lista))
int(min(lista))

É possivel transformar uma lista em tupla
tupla= tuple(lista)

----> Desempacotamento de lista
lista[1, 2, 3]
num1, num2, num3 = lista

# Copiando uma lista (Shallow Copy e Deep Copy)

# Forma 1

lista [1, 2, 3]
nova = list.copy()     -- veja que ao utilizarmos lista.copy() criando duas listas independentes!!
nova.append(4)              -- Deep Copy

#Forma 2

lista [1, 2, 3]
nova = lista          -- Utilizamos a copia via atribuição e após realizar modificação em uma das listas
nova.append(4)        --essa modificação refletiu em ambas as listas!
                      -- Shallow Copy



"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['V', 'i', 'n', 'i', ' ', 'C', 'e', 's', 'a', 'r']

lista3 = []

lista4 = list(range(11))
print(lista4)

lista5 = list("vini cesar")

cores = ['verde', 'amarelo', 'azul', 'branco']




