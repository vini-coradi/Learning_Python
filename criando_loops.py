"""
Criando sua própria versão de loop



for num in [1, 2, 3, 4, 5]:
    print(num)

print(iter([1, 2, 3, 4, 5]))

"""

def meu_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Vinicius')
