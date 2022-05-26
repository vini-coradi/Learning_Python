import math

def circurferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

print(circurferencia(2))

def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

nome = 'Vini' # type: str

