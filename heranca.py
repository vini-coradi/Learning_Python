"""
POO -> Herança (Inheritance)

A ideia de herança é a de reaproveitar código, mas não apenas isso!
Também extender nossas classes!

# Obs: Com a herança, a partir de uma classe existente, nós expandimos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - Nome
    - Sobrenome
    - CPF
    - Renda

Funcionário
    - Nome
    - Sobrenome
    - CPF
    - Matrícula

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e
métodos comuns a outras entidades?

Obs: Quando uma classe herda de uma class, ela herda todos os atributos e métodos da classe herdada


Quando uma classe herda de outra class, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe
    - Classe Mãe/Pai
    - Classe Base
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada por:
    [Cliente, Funcionario]
    - Sub Classe
    - Classe Filha
    - Classe Específica




class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('vni', 'cesar', '123.456.789-99', 5000)

func1 = Funcionario('coradi', 'goncalves', '987.654.321.-00', 1234)


print(cliente1.nome_completo())

print(func1.nome_completo())


# Sobrescrita de Métodos (Overrriding)
Sobrescrita de métodos ocorre quando reimplementamos/reescrevemos um método presente na super classe
em classes filhas
"""




class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf) # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        return f'{self.__matricula} {self._Pessoa__nome}'


cliente1 = Cliente('vni', 'cesar', '123.456.789-99', 5000)

func1 = Funcionario('coradi', 'goncalves', '987.654.321.-00', 1234)


print(cliente1.nome_completo())

print(func1.nome_completo())