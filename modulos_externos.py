""""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes oficiais em

http://pypi.org


colorama -> É utilizado para permitir a impressão de textos coloridos no terminal
"""

from colorama import init

from colorama import Fore, Back, Style

print(Fore.RED + 'Vinicius')
print(Fore.BLUE + 'Cesar')

print(Fore.BLUE + 'Cesar')

print(Back.BLUE + Fore.YELLOW + 'Cesar')