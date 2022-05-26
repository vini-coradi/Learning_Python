"""
Sistemas de Arquivos -- Manipulação


# Paths Relativos
# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt')) # False

print(os.path.exists('any_all.py')) # True

# Descobrindo se um diretório existe
print(os.path.exists('teste')) # True


# Criando arquivos
# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 1
open('arquivo-teste.txt', 'a').close()

with open('arquivo-teste.txt', 'w') as arquivo:
    pass


# Criando arquivos

os.mknod('arquivo-teste2.txt')  # Pode não funcionar noo sistema operacional no Mac OS - PermissionError


# Criando arquivos

os.mknod('arquivo-teste2.txt')  # Pode não funcionar noo sistema operacional no Mac OS - PermissionError

# OBS: Criando o arquivo via mknod() se o arquivo já existir, teremos o erro FileExistsError



os.mkdir('templates')

# Obs: A função mkdir() cria um novo diretório se este não existir. Caso exista teremos FileExistsError
# Obs: Se não tivermos permissão para criar o diretório, teremos um PermissionError
# Obs: Podemos criar apenas um diretório por vez



os.makedirs('templates/geek', exist_ok=True)

# Obs: Se já existir, teremos FileExistsError
# Obs: Podemos criar vários diretórios por vez


# Renomear diretórios

os.rename('geekkee', 'user12')

# Se o diretório não existir, teremos um FileNotFoundError
# Se o diretório que queremos renomear não estiver vazio, teremos um OSError


# Renomeando arquivos
os.rename('arquivo-teste.txt', 'testando.txt')



# Atenção! Tome cuidado com os comandos de deleção!
# Ao deletar un(s) arquivo(s) eles NÃO VÃO para a lixeira, eles somem!
# Removendo arquivos

os.remove('testando.txt')

# Obs: Se você estiver no windows e o arquivo que você for deletar estiver em uso, você terá um erro
# Obs: Caso o arquivo não exista teremos o FileNotFoundError
# Se você informar um diretório ao invés de um arquivo, teremos IsADirectoryError


# Removendo diretórios vazios

os.rmdir('user12')

# Obs: Se o diretório tiver qualquer conteúdo teremos um OSError
# Obs: Se o diretório não existir, teremos um FileNotFoundError

# Removendo uma árvore de arquivos
for arquivo in os.scandir('user12'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)


# Podemos remover uma árvore de diretórios vazio

os.removedirs('user12/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# sudo apt-get install lsb-core
# pip install send2trash



# Importando a biblioteca send2trash
from send2trash  import send2trash

os.removedirs('cesta1.txt') # Não vai para a lixeira. É deletado automaticamente.
send2trash('cesta2.txt') # Vai para a lixeira. Não pode ser restaurado.

# Obs: Se o arquivo não existir teremos OSError (para o send2trash)


# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporáario em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Curso de Python\n')
        input()

# Estamos criando um diretório temporário, abrindo o mesmo e criando dentro dele um
# arquivo para escrevermos um texto. No final usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro do bloco with

# Obs: Possivelmente o código acima não irá funcionar no windows por conta desse sistema trabalhar
# de forma diferente com arquivos temporários

"""

# Criando apenas o arquivo temporario

with tempfile .TemporaryFile() as a temp:
    temp.write(b'Curso de Python')
    temp.seek(0)
    print(temp.read())

# Obs: Em aruivos temporários só conseguimos escrever em binário, por isso usamos o b''