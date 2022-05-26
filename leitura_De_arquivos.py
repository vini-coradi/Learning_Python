"""
Leitura de Arquivos

Para ler um arquivo ou ler o conteudo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização, é passado apenas um parâmetro de entrada. No caso
é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos!

https://docs.python.org/3/library/functions.html#open


Obs: por padrão a função open() abre o arquivo para leitura. Caso contrário será gerado o erro
FileNotFoundError

io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252

mode r -> Modo de leitura. r -> read() -> ler


"""

# Exemplo

arquivo =  open('texto.txt')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteudo de um arquivo, após a sua leitura, devemos utilizar a função read()

ret = (arquivo.read())

print(type(ret))

print(arquivo.read())

# Obs: o Python utiliza um recurso para trabalhar com arquivos chamado cursor!
# Funciona semelhante ao cursor quando estamos escrevendo!
# A Função read() lê todo o conteúdo do arquivo!
