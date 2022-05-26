"""
Escrevendo um iterador customizado


for n in range(11):
    print(n)

"""

class Contador:
    def __init__(self, menor, maior):
        self.menor=menor
        self.maior=maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor+1
            return numero
        raise StopIteration




con = Contador(1, 6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))