"""
Decoradores (Decorators)

O que são Decorators?

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seu comportamento
- Decorators são exemplos de High Order Functions
- Decorators tem uma sintaxe própria, usando "@" (Syntax Sugar)





\---------------------------------------- --\
\           Function Decorator              \
---------------------------------------------


----------------------------------------------
\\---------------------------------------- --\\
\\           Função Decorada                 \\
\\-------------------------------------------\\
-----------------------------------------------




# Decorators como funções (Sintaxe não recomendada / Sem Syntact Sugar)

def seja_educado(funcao):
    def sendo():
        print('Seja bem vindo')
        funcao()
        print('Bom dia!')
    return sendo

def saudacao():
    print('Olá!')

# Testando 1

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('ódio!')

raiva_educada = seja_educado(raiva)

raiva_educada()




# Decorators com Syntax Sugar

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Bom dia!')
    return sendo

@seja_educado
def apresentando():
    print('Meu nome é Vini')

# Testando

apresentando()

@seja_educado
def dormir():
    print('Quero dormir')


dormir()
"""

# Não confundir Decorator com Decorator function