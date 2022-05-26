"""
Módulo Collections deque

Podemos dizer que o deque é uma lista de alta performance

Necessário o import
"""
# Import

from collections import deque

# Criando deques

deq = deque('geek')

print (deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona elemento no final

deq.appendleft('k')

print(deq) # Adiciona no comeco da lista

# Removendo Elementos

print(deq.pop()) # Remove e retorna o ultimo elemento

print(deq.popleft()) # Remove e retorna o primeiro elemento 

