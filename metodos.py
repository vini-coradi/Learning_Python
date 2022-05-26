"""
POO -> Métodos

-> Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que
este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos assim como os atributos, em 2 grupos: Métodos de Instância
e Métodos de Classe.

# Métodos de Instância

# O método dunder init  __init__ é um método especial chamado de contrutor e
sua função é construir o objeto a partir da classe.

# Obs: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

Obs: Os métodos/funções dunder em Python são chamados de métodos mágicos.

Atenção! Por mais que possamos criar nossas próprias funções utilizando dunder,
não é aconselhado. Python possui vários métodos com essa forma de nomenclatura e
pode ser que mudemos o comportamento dessas funções mágicas internas da linguagem.
Então evite ao máximo, de preferência, nunca o faça.

# Métodos são escritos em letra minúscula. Se o nome for composto, o nome terá as palavras separadas por underine


p1 = Produto('ps4', 'video GAMEPY',2000)

print(p1.desconto(10))

print(Produto.desconto(p1, 50))# self, desconto




#user1 = Usuario('Vini', 'Cesar', 'user@gmail.com', '123456')

#print(user1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user1 = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso')

senha = input('Informe a senha para acesso: ')

if user1.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user1._Usuario__senha}') # Acesso Errado

#Obs: Métodos de classe em Python são conhecidos como métodos estáticos em outras linguagens



# Métodos de Classe


user = Usuario('vini', 'cesar', 'user@gmail.com', '123456')

Usuario.conta_usuarios() # Forma correta
user.conta_usuarios()   # Possível mas forma incorreta
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto (self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():
        return 'uxr344'


    def __init__(self, nome,sobrenome, email, senha):
        self.__id =  Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f' {self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Método Privado
    def __gera_usuario(self):
        return self.__email.split('@')[0]


#user1 = Usuario('vini', 'cesar', 'vini@gmail.com', '123456')

# Método Estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('vini', 'cesar', 'vini@gmail.com', '123456')


print(Usuario.contador)

print(Usuario.definicao())