"""
Len, Abs, Sum e Round

                                                        # Len



len() -> Retorna o tamanho, ou seja, o número de itens de um iterável


print(len('vinicius goncalves'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len
print('vinicius goncalves'.__len__())

                                               # Abs



abs() -> Retorna o valor absoluto de um valor inteiro ou real.

print(abs(-10))
print(abs(-4.5))
print(abs(10))
print(abs(4.5))


                                                # Sum


sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial

Obs: O valor inicial default é 0

# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([1.45, .5, 2.5]))

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))



                                            # Round


round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada

"""

# Exemplos de Round

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1/3, 2))

print(round(10/9, 4))

