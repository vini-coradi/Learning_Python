"""
PDB --> Python Debugger



# Exemplo com o PyCharm

def divisao(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu o seguinte erro: {err}')

print(divisao(4,5))


# Exemplo 1  com o PDB - Python Debugger

# Para utilizar  o Python Debugger, precisamos ***importar a bibilioteca pdb e então utilizar a função set_trace()

# Comandos básicos pdb
# l para listar onde estamos no código
# n próxima linha
# p imprime variável
# c continua a execução, finaliza o debug
import pdb

nome = 'Vinicius'
sobrenome = 'Cesar'
pdb.set_trace()
nome_total = nome + ' ' + sobrenome
idade = '24 anos'
genero = 'masculino'
final = nome_total + ' tem ' + idade + ' / genero ' + genero
print(final)



# Exemplo 2  com o PDB - Python Debugger

# Para utilizar  o Python Debugger, precisamos ***importar a bibilioteca pdb e então utilizar a função set_trace()

# Comandos básicos pdb
# l para listar onde estamos no código
# n próxima linha
# p imprime variável
# c continua a execução, finaliza o debug


nome = 'Vinicius'
sobrenome = 'Cesar'
import pdb; pdb.set_trace()
nome_total = nome + ' ' + sobrenome
idade = '24 anos'
genero = 'masculino'
final = nome_total + ' tem ' + idade + ' / genero ' + genero
print(final)

# Por que utilizar esse formato ?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# Nós colocamos somente onde será necessário debuggar, e ao finalizar já realizamos a remoção da linha.

"""

# Exemplo 3  com o PDB - Python Debugger

# Para utilizar  o Python Debugger, precisamos ***importar a bibilioteca pdb e então utilizar a função set_trace()

# A partir do python 3.7 não é mais necessário importar a biblioteca pdb. Pois o comando de debug foi
# incorporado como função built - in (integrada) chamada breakpoint()

# Os comandos continuam iguais

# Comandos básicos pdb
# l para listar onde estamos no código
# n próxima linha
# p imprime variável
# c continua a execução, finaliza o debug


nome = 'Vinicius'
sobrenome = 'Cesar'
breakpoint()
nome_total = nome + ' ' + sobrenome
idade = '24 anos'
genero = 'masculino'
final = nome_total + ' tem ' + idade + ' / genero ' + genero
print(final)

# Cuidados com conflitos entre nomes de variáveis e os comandos do pdb!
# Caso uma variável possua o mesmo nome de um comando do pdb devemos escrever assim:
# p l (imprime a variável l) --> utilizamos o comando p
# p nome_da_variavel

# É sempre melhor utilizar nomes significativos nas variáveis!!