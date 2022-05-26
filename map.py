"""
Map

Com o map, fazemos mapeamento de valores para a função



import math

def area(r):
    #Calcula a area de um circulo de raio r
    return math.pi * (r ** 2)

print(area(2))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: o primeiro é a função e o segundo um iterável. Retorna um map object

areas = map(area, raios)
print(list(areas))

# Acima foi feito o cast para lista


# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r **2), raios)))

# Obs após utilizar a função map(), depois da primeira utilização do resultado, ele zera

"""
# Para fixar - Map

# dados: a1, a2... an

# Funcao f(x)

# Utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função

# O Map Object: f(a1), f(a2)... f(an)

# Exemplo !

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27), ('Nova York', 28),
           ('Londres', 22)]
print(cidades)

# f = 9/5 *c + 32  --> tranformando celsius em farenheit

c_to_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_to_f, cidades)))

