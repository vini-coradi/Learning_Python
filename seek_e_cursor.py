""""
Seek e Cursor

seek() -> É utilzado para movimentar o cursor pelo arquivo.

A função seek recebe um parâmetro que indica onde queremos posicionar o cursor



arquivo = open('texto.txt')

print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(15)

print(arquivo.read())


arquivo = open('texto.txt')

# readLine() -> Função que lê o arquivo linha a linha

print(arquivo.readline())

arquivo.readline()

ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split(' '))




arquivo = open('texto.txt')

# readlines()

linhas = arquivo.readlines()

print(len(linhas))


obs: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco de computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar
essa conexão. Para isso utilizamos a função close()



# 1- Abrir o arquivo
arquivo = open('texto.txt')

# 2- Trabalhando com o Arquivo
print(arquivo.read())

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado


# 3- Fechando o arquivo
arquivo.close()

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado


# Obs ao tentar manipular o arquivo após o fechamento, teremos um ValueError

"""
arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo.
print(arquivo.read(10))