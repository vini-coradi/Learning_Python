"""
Lendo arquivos CSV

CSV - Comma Separated Values  -- Valores Separados por virgula

# Separador por vírgula

# Separador por ponto e vírgula

# Separador por espaço



# Possível de se trabalhar, mas não é o ideal (trabalhoso)

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem python possui duas formas diferentes para ler dados em arquivos csv
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo csv como OrderedDcits;




# Reader

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pular cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')


# DictReader

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)

    for linha in leitor_csv:
        # Cada linha é uma OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e  mede {linha['Altura (em cm)']} centímetros")


"""

# DictReader com outro separados

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')

    for linha in leitor_csv:
        # Cada linha é uma OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e  mede {linha['Altura (em cm)']} centímetros")

