"""
Unittests - Antes e após hooks

Hooks -> são os testes em si, ou seja, a execução dos testes.

setup() -> É executado antes de cada método de teste. Sendo útil para criarmos
instâncias de objetos e outros dados.


tearDown() -> É executado ao final de cada método de teste. É útil para excluir dados
ou fechar conexões com banco de dados

"""

import  unittest

class ModuloTest(unittest.TestCase):

    def setup(self):
        # Configurações do setup()
        pass

    def teste_first(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar depois do teste
        pass

    def teste_second(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar depois do teste
        pass

    def tearDown(self):
        # Configurações do tearDown
        pass


