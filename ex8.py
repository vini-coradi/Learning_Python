def pesquisa(sexo,idade, **kwargs):

    for olho, cabelo in kwargs.items():
       max(idade)



"""
if kwargs['olho'] == 'C' and kwargs['cabelo'] =='P':
                print(idade)
                global total
                global count
                type(idade)
                idadex = int(idade)
                total = idadex/2 + total
                count = count +1/2
                counter=0"""








#total = 0
#count = 0
joao = {'sexo':'masc','idade': '30', 'olho':'C', 'cabelo':'P'}
maria = {'sexo':'fem','idade': '3', 'olho':'C', 'cabelo':'C'}
edu = {'sexo':'masc','idade': '9', 'olho':'C', 'cabelo':'L'}
vini = {'sexo':'masc','idade': '2', 'olho':'C', 'cabelo':'P'}
luis = {'sexo':'masc','idade': '7', 'olho':'A', 'cabelo':'P'}

pesquisa(**joao)
pesquisa(**maria)
pesquisa(**edu)
pesquisa(**vini)
pesquisa(**luis)

#print(count)
#print(total/2)