"""
Dicionários

Obs: Em algumas linguagens, os dicionários são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {}

Exemplo:

Sobre dicionários
                - Chave e valor são separados por dois pontos 'chave:valor';
                - Tanto chave quanto valor podem ser de qualquer tipo de dado;
                - Podemos misturar tipos de dados

Criação de dicionários

# Forma 1  -- Mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}


# Forma 2 -- Menos comum
paises = dict(br='Brazil', eua='Estados Unidos', py = 'Paraguay')


# Acessando elementos

# Forma 1 --  Acessando via chaVE
print(paises['br'])  -- Caso a chave informada não seja encontrada, retorna erro KeyError

# Forma 2 -- Recomendada
print(paises.get('br')) -- Caso a chave não seja encontrada, retorna tipo None

# Forma  2 -- Completa
print(paises.get('br', 'Não encontrado'))
-- Verifica e caso a chave não seja encontrada, ele utilizada o valor padrão que é informado(opcional)

Podemos verificar se determinada chave está em um dicionário. A busca é feita apenas por chave e não por valor
if 'br' in paises
    brasil = paises['br']

# Adicionando elementos ao dicionário ou Atualizar dados de um dicionário
# Como o acesso aos valores é feito pela chave. NÃO PODEMOS TER CHAVES REPETIDAS.
receita = {'jan': 100, 'fev': 120, 'mar': 300}

    # Forma 1 -- Mais Comum
    receita['abr'] = 350

    # Forma 2
    novo_dado  = {'mai': 500}
    receita.update(novo_dado)

# Removendo dados

    # Forma 1 --  Mais Comum
    ret = receita.pop('mar')
    Obs: é obrigatório informar a chave. Caso a chave não seja encontrada retorna KeyError
    Obs ao remover o objeto, o valor é retornado (no caso armazenado em ret)

    # Forma 2
    del receita['fev']
    Obs: Caso a chave não seja encontrada, retorna KeyError
    Obs: Nesse caso o valor removido não é retornado

Exemplo de uso: Carrinho eletrónico com produtos

carrinho = []

produto1= {'nome': 'Play 4', 'quantidade': 1, 'preço': 2350.00}
produto2= {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

# É possivel limpar um dicionário. Por exemplo, sendo receita um dicionário:
receita.clear()

            EM DICIONÁRIOS TEMOS O DEPP COPY E O SHALLOW COPY

# Forma não usual de criar dicionários:
 outro = {}.fromkeys('a', 'b')
 usuario ={}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
     Portanto o metodo fromkeys recebe dois parametros: um interável e um valor.
     Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

Se veja = {}.fromkeys('teste', 'valor')
    ele irá gerar uma chave para cada letra da primeira string( t, e, s,... o resto não vira chave pois são
    caracteres repetidos) e atribui a string como valor para as chaves.
veja = {}.fromkeys(range(1,11), 'novo')

"""