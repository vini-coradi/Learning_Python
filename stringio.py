"""
StringIO

Atenção: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:

Permissão de leitura para ler o arquivo
Permissão de escritura para escrever arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.


"""

# Primeiro é necessário o import

from io import StringIO

mensagem =  'Este é apenas uma string comum de teste'

# Podemos criar um arquivo em memória com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora podemos utilizar operacoes com o arquivo
print(arquivo.read())