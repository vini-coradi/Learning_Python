"""
Estruturas lógicas and, or, not, is

Operadores unários:
not, is

Operadores Binarios:
and, or

Para o is, um valor é comparado, Retorna true ou false de uma afirmação

"""

ativo = True
logado = False

if not(ativo and logado):
    if not ativo:
        print('Voce precisa ativar sua conta. Por favor, verifique seu email!')
    else:
        print("Voce precisa se logar")
else:
    print('Bem vindo usuário!')

#Ativo é falso ?
print(ativo is False)


