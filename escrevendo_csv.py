"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escrever)

writerou() -> Escreve uma linha




# Writer -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writenow() para escrever cada linha. Esse método recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme !='sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

"""


# DictWriter

# As chaves do dicionário devem ser as mesmas utilizadas no cabeçalho

# Para modificar um arquivo que já existe, trocar o 'w' por 'a'

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})

