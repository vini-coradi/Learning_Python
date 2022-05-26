"""
Pacotes

Módulo -> apenas um arquivo Python que pode ter diversas funções para utilizarmos

Pacote -> É um diretório contendo uma coleção de módulos

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado _init_.py

Nas versões do Python 3.x não é mais necessário a utilização do arquivo, porém
ainda é utilizado para manter a compatibilidade


"""

from teste import teste1, teste2

from teste.exemplo import  teste3, teste4

print(teste1.pi)

print(teste1.funcao_1(2,4))

print(teste2.curso)

print(teste3.funcao3())

print(teste4.funcao4())

print(teste2.funcao2())
