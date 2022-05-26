"""
Geradores

-    Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdade! Ou seja, nem todo iterador é um gerador!

Outras Informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-------------------------------------------------------------------------------------
| Funções                               | Generator Functions                       |
-------------------------------------------------------------------------------------
| Utilizam return                       | Utilizam yield                            |
-------------------------------------------------------------------------------------
| Retorna uma vez                       | Podem utilizar yield múltiplas vezes      |
-------------------------------------------------------------------------------------
| Quando executada, retorna um valor     | Quando executada, retorna um generator   |
-------------------------------------------------------------------------------------


# Exemplo Função Geradora (Generator Function)

def conta_at(valor_maximo):
    contador=1
    while contador<= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um generator. Ela gera um generator!

gen = conta_at(5)

print(type(gen))

print(next(gen))


"""

# Exemplo Função Geradora (Generator Function)

def conta_at(valor_maximo):
    contador=1
    while contador<= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um generator. Ela gera um generator!

gen = conta_at(5)

print(type(gen))

print(next(gen))