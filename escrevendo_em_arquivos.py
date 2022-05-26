""""
Escrevendo em arquivos

Obs: Ao abrir um arquivo para leitura, não poderemos fazer escrita nele.
De forma análoga, ao abrir um arquivo para escrita, não poderá ser feita a leitura


#Obs: Ao abrir um arquivo para escrita, caso ele não exista, será criado no sistema operacional.
Para escrevermos utilizamos a função write().
Essa função recebe uma string como parâmetro. Caso contrário, será gerado um TypeError

Abrindo um arquivo para escrita com o modo 'w', caso o arquivo ja exista, o anterior será apagado e um novo é criado.
Dessa fofrma todo o conteúdo do arquivo será perdido.

"""
# Exemplo de escrita - modo 'w' - write

with open('novo_texto.txt', 'w') as arquivo:
    arquivo.write('Escrevendo dados em um arquivo\n')
    arquivo.write('Bem tranquilo, bem facil!\n')
