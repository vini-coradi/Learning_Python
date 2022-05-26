""""
Modos de abertura de arquivo

'r' -> Abre para leitura - padrão
'w' -> Abre para escrita - sobescreve caso o arquivo já exista
'x' -> Abre exclusivamente para criação e escrita. Falha se o arquivo já existir.
Caso o arquivo exista, gera FileExistsError
'a' -> Abre para a escrita, adicionando o conteúdo ao final do arquivo.
Obs: Ao abrir no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o conteúdo é
adicional ao final do arquivo. Com o modo 'a', não é possível controlar o cursor.
'+' -> Abre para o módulo de atualização, leitura e escrita. (Temos o controle do cursor)


Exemplo x:

try:
    with open("python.curse.txt", 'x') as arq:
        arq.write('Testando operacoes com arquivos')
except  FileExistsError:
    print('Arquivo já existe!!')

Exemplo a:


with open("python.curse.txt", 'a') as arq:
    while True:
        fruta = input('Informe uma fruta ou sair:')
        if fruta!= 'sair':
            arq.write(fruta + '\n')
        else:
            break



"""

