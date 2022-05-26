"""
Funcoes com parametros de entrada

-- Funcoes que recebem  dados para serem processados dentro da mesma

Em uma função, geralmente, temos:

entrada -- > processamento --> saida

# Refatorando uma funcao


def quadrado(numero):   # CASO NÃO SEJA PASSADO O VALOR DO PARAMETRO, RETORNA   TypeError
    # return numero*numero
    return numero ** 2

print(quadrado(3))
print(quadrado(4))
print(quadrado(5))

# Refatorando uma funcao

def cantar_parabens(aniversariante):
    print('parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!!')


cantar_parabens('Vini')

# Funções podem receber n parametros de entrada. Podemos receber como entrada
# quantos parametros forem necessários. Eles serão separados por virgulas!

def soma(a,b):
    return a+b

def mux(a,b):
    return a*b

def lets(m,v, f):
    return (m*v)*f

print(soma(2,3))
print(mux(4,5))
print(lets(2,8,' Go'))

# Obs ao informar uma quantidade errada de parametros ao chamar a função, resultará em TypeError

# Nomeando parametros

def nome(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'

print(nome('Vini', 'Cesar'))

# A diferença entre parametros e argumentos

# Parametros são variáveis declaradas na definição de uma função ( no ex, nome e sobrenome)
# Argumentos são dados passados durante a execução de uma função ( no ex, vini e cesar)

# Argumentos nomeados (Keyword Arguments)
#Caso utilizemos nome dos parametros nos argumentos para informa-los podemos utilizar qualquer ordem

print(nome(sobrenome='Cesar', nome='Vinicius'))


"""
# Erro comum ao usar o return

def soma_impares(numeros):
    total=0
    for num in numeros:
        if num % 2 !=0:
            total=total + num
            # return total  --> o retorno aqui não iria terminar a soma de todos os valores
    return total


if __name__ == '__main__':
    lista = (range(6))
    print(soma_impares(lista))
