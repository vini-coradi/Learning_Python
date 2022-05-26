"""
JSON e Pickle

JSON -> Javascript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
e terceiros




ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2300)}])

print(type(ret))

print(ret)




import json


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


mia = Gato('Mia', 'Sphinx')

ret = json.dumps(mia.__dict__)

print(ret)




# Integrando o Json com o pickle

# precisamos instalar uma biblioteca
# pip install jsonpickle


import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


mia = Gato('Mia', 'Sphinx')

ret = jsonpickle.encode(mia)

print(ret)



# Escrevendo no arquivo json/pickle

# precisamos instalar uma biblioteca
# pip install jsonpickle


import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


mia = Gato('Mia', 'Sphinx')

with open ('mia.json', 'w') as arquivo:
    ret = jsonpickle.encode(mia)
    arquivo.write(ret)
"""




# lendo no arquivo json/pickle

# precisamos instalar uma biblioteca
# pip install jsonpickle


import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


mia = Gato('Mia', 'Sphinx')

with open ('mia.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
