"""
Por que testar o código?

Testes Automatizados!

    - Reduzir bugs.
    - Testes garantem que novos recursos da sua aplicação não quebrem/alterem recursos antigos.
    - Testes garantem que bugs que foram corrigidos anteriormente continuam corrigidos.
    - Testes garantem que a refatoração que costumamos fazer, não tragam novos bugs.

TDD - Test Driven Development (Desenvolvimento guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento.
    - Você escreve seu teste primeiro.
    - Então você escreve o código mínimo suficiente para fazer o teste passar.
    - Então refatora o código para realizar a funcionalidade e testa novamente.
    - Uma vez que o teste passe, o recurso é considerado completo.

Estes testes de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red
    - Green
    - Refactor




"""

class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

