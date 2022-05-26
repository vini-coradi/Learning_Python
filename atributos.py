"""
POO -> Atributos

Atributos -> representam as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python dividimos os atributos em 3 grupos:
    - Atributos de instância
    - Atributos de classe;
    - Atributos Dinâmicos;

# Atributo de Instância: São atributos declarados dentro do método construtor

# Obs: Método construtor é um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos, ficaria mais ou menos assim:

public class Lampada(){
    private Int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(Int voltagem, String cor){
        this.voltagem=voltagem;
        this.cor=cor;
    }

    public int getVoltagem(){
        return this.voltagem;
    }
}

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso desejarmos que um atributo seja tratado como privado, ou seja, que deve ser
acessado/utilizado somente dentro da própria classe, onde está declarado,
utiliza-se __ duplo underscore no inicio do seu nome.

Isso é conhecido também por Name Mangling.


# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.senha)   # AttributeError

print(user._Acesso__senha) # Temos acesso. Mas não deveríamos fazer este acesso (Name Mangling)

user.mostrasenha()

# O que significa atributos de instância?

# Significa que ao criar instâncias/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com' ,'654321')

user1.mostrasenha()
user2.mostrasenha()




# Atributos de Classe

# Atributos de Classe são atributos que são declarados diretamente na classe, ou seja,
# fora do contrutor. Geralmente já inicializamos um valor e este valor é compartilhado entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância de classe ter seus próprios
# valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias
# terão o mesmo valor para este atributo

class Produto:

    # Aributo de classe
    imposto = 1.05 # Ou seja, 0,05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor *Produto.imposto)
        Produto.contador = self.id

p1 = Produto('ps4', 'video GAMEPY', 2300)
p2 = Produto('xbox', 'video GAMEPY', 1500)

print(p1.valor)     # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)

# Obs: Não precisamos criar uma instância de classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Obs: Em linguagems como Java, os atributos conhecidos como atributos de classe aqui em Python,
# são chamados de atributos estáticos;

"""

# Classes com atributos de instância públicos
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostrasenha(self):
        print(self.__senha)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe


# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução

# Obs: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PS4', 'video GAMEPY', 2300)

p2 = Produto('xbox', 'video GAMEPY', 1500)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Note que na classe produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso:{p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso:{p1.peso}')


# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

print(Produto.__dict__)

del p2.peso
del p2.valor


print(p1.__dict__)
print(p2.__dict__)
