from BANCOPY.models.cliente import Cliente
from BANCOPY.models.conta import Conta


vini: Cliente = Cliente('Vinicius Cesar',  "vinicius@gmail.com", '123.456.789-98', '14/02/1996')

print(vini)

contaf: Conta = Conta(vini)

print(contaf)