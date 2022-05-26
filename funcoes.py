"""
    --Funcoes são pequenos trechos de código que realizam tarefas especificas!
    --Podem ou não receber entradas de dados e retornar uma saída de dados
    --Muito uteis para executar procedimentos similares por repetidas vezes


Já utilizamos várias funções desde que inciamos o curso:
-- print()
--  len()
-- max()
--  min()
-- count()

"""

# Exemplo de utilização de funções

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Bult-in) do Python print()

# print(cores)    # Print é uma função que recebe entrada de dados (cores)

# cores.append('roxo')     # Append é uma função que recebe entrada de dados

# DRY - Don't repeat yourself - Não repita seu código

# Como definir funções

"""
Em python definimos uma função como

def nome_da_funcao(parametros de entrada):
    bloco_da_funcao


Onde:
Nome da funcao --> sempre com letras minusculas
se nome composto --> separados por underline (Snake Case)
Parametros de entrada --> são opcionais, onde tendo mais de um, serão separados por virgula
bloco da funcao --> Tambem chamado de corpo da função ou implementação, é onde o processamento da função ocorre
Nesse bloco, pode ou não ter retorno da função

OBS: para definir uma função utilizamos a palavra reservada 'def' -> informando o Python que 
estamos definindo uma função. Também abrimos o bloco de código com os dois pontos ' : ' 

"""


# Definindo a primeira funcao

def diz_ola():
    print('Olá!')


"""
1 - É possivel efetuar funções dentro de funções
2- Essa função executa apenas uma tarefa
3- Se trata de uma função sem parametro de entrada
4- Veja que essa função não retorna nada

"""

# Chamada de execução

# Errado
diz_ola

# Certo
diz_ola()


# Exemplo 2
def cantar_parabens():
    print('parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


cantar_parabens()

# Em python podemos inclusive criar variaveis do tipo de uma função e executar essa função através da variável

canta = cantar_parabens

canta()
