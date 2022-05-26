"""
Conjuntos
 -- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria de Conjuntos
 da Matemática

 - Conjuntos tambem são chamados de sets


-- Sets (conjuntos) não possuem valores duplicados
-- Sets (conjuntos) não possuem valores ordenados
-- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
Mas não nos importamos com a ordenação. Quando não precisamos nos preocupar
com chaves, valores, e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Maps (Dicionários) em Python
    -- um dicionário tem chave/valor;
    -- um conjunto tem apenas valor;



# Definindo um conjunto:
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) #valores repetidos
# Observação ao criar um conjunto, ao add um valor existente...
# ele será ignorado sem gerar erros nem fazer parte do conjunto

# Forma 2
s = {1, 2, 3, 4, 5, 5}

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem 3')

Aceita tipos de dados totalmente misturados!

#Podemos iterar em um s normalmente

Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4) --> duplicidade não gera erro, é apenas ignorado e não adicionado

Removendo elementos de um conjunto
# Forma 1
s.remove(3) - - o 3 é o valor 3, não o indice 3
Nenhum valor é retornado
Obs caso o valor não seja encontrado, será gerado o erro KeyError

# forma 2
s.discard(2)
Obs caso o valor não seja encontrado, nenhum erro será gerado

Copiando conjuntos

s = {1, 2, 3}  -- Deep Copy
novo = s.copy()
Deep copy -- elementos totalmente diferentes

# Forma 2  -- Shallow Copy
novo  = s
qualquer modificação em s, modifica o novo também

# Podemos remover todos os itens de um conjunto
s.clear()

# Métodos matematicos de Conjuntos

# Imagine dois conjuntos: estudantes de python e estudantes de java

est_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
est_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Vemos que alguns alunos que estuda python também estudam java
# Gerando um conjunto com estudantes unico
# Forma 1
unico1 = estudantes_python.union(estudantes_java) --  o inverso da o mesmo resultado

# Forma 2 -- utilizanddo o caractere pipe
unico2 = est_python | est_java


#Gerando conjunto de estudantes que estão em ambos os cursos
#Forma 1
ambos1 = est_pyhton.intersection(est_java)

#Forma 2  -- utilizando &
ambos2 = est_python & est_java

#Gerar um grupo com estudantes exclusivos
so_python = est_python.difference(est_java)

"""

