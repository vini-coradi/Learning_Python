"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os --> Operating System - Sistema Operacional


# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd()) # C:\\Users\\acer\\PycharmProjects\\guppe

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd()) # C:\\Users\\acer\\PycharmProjects



# Fazer o import
import os

# Podemos checar se um diretório é relativo ou absoluto

# OBS para usuarios windows!!
print(os.getcwd()) # C:\\Users\\acer\\PycharmProjects
print(os.path.isabs('C:\\Users\\acer\\PycharmProjects\\guppe'))


# Fazer o import
import os

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix linux e mac, nt para windows

# Podemos ter mais detalhes sobre o sistema operacional
print(os.uname())  -- para mac e linux



# Fazer o import
import sys

# Podemos ter mais detalhes sobre o sistema operacional
print(sys.platform)



print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek')

os.chdir(res)
print(os.getcwd())

# Veja que os.path.join() recebe dois prâmetros sendo o primeiro o diretório atual e o segundo que será
# juntado ao atual



# Podemos lisar os diretórios e arquivos com o listdir()

print((os.listdir()))
"""

import os

# Podemos listar os diretórios e arquivos com mais detalhes com scandir()
scanner  = (os.scandir())

arquivos = list(scanner)
# print(arquivos)

# print(dir(arquivos[1]))

print(arquivos[2].inode()) # Numeração do arquivo no diretório
print(arquivos[2].is_dir()) # É um diretório? False
print(arquivos[2].is_file()) # É um arquivo? True
print(arquivos[2].is_symlink()) # É um link simbólico? False
print(arquivos[2].name) # Nome do arquivo
print(arquivos[2].path) # Caminho do arquivo
print(arquivos[2].stat()) # Estatisticas sobre o arquivo

# OBS: quando utilizamos a função scandir()), assim como abrimos um arquivos.

scanner.close()
