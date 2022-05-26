"""from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Vini', 'Cesar']

versoes: Tuple[int, int, int] = (3, 7, 4)

opcoes: Dict[str, bool] = {'ar': True, 'bancos_couro': True}

valores: Set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""

import random

NAIPES = '♠ ♥ ♦ ♣'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas para jogar"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)

    return baralho

def distribuir_cartas(baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}


    for jogador, cartas in maos.items():
        carta = ' '. join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {cartas}')

if __name__ == '__main__':
    jogar()


print(NAIPES)
print(CARTAS)

print(criar_baralho())

print(jogar())