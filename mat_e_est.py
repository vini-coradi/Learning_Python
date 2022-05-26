# math.prod = retorna o produto de um container numérico
import math

nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}

# print(math.prod(nums_v1))
# print(math.prod(nums_v2))
# print(math.prod(nums_v3))

# math.isqrt -> Retorna a parte inteira da raiz quadrada de um número

# print(math.isqrt(9))
# print(math.sqrt(9))
# print(math.isqrt(17))
# print(math.sqrt(17))

#math.dist -> Retorna a distância euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D:
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D:

p2d1 = [12, 50]
p2d2 = [6, 7]

# print(math.dist(p3d1, p3d2))
# print(math.dist(p2d1, p2d2))


# math.hypot -  Retorna a hipotenusa, ou a norma Euclidiana

print(math.hypot(*p3d1))
print(math.hypot(*p2d2))

# Estatistica

# statistics.fmean -  Calcula a média de números reais

import statistics

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# statistics.geometric_mean - calcula a média geométrica de números reais


print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))

# statistics.multimode - retorna o valor mais frequente de uma sequencia

seq1 = 'Vinicius Cesar Coradi Goncalves'
seq2 = [1, 3, 5, 7, 9, 11, 3]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))