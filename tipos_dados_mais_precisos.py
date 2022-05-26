"""

from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#    pass



from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#    pass

def calcula_v1(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')

calcula_v1('+', 6, 10)
calcula_v1('-', 8, 2)
calcula_v1('*', 8, 2)


from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
    if resultado > 50:
        f'O valor {resultado} é gigante'
    else:
        return resultado




from typing import Final

NOME: Final = 'Vini'

print(NOME)




from typing import final

@final
class Pessoa:
    pass

class Estudante(Pessoa):        # Errado pois a classe pessoa é final e nenhuma classe deveria herdar dela
    pass

    @final
    def estudar(self):
        print('Estou estudando...')

class Estagiario(Estudante):
    pass

    def estudar(self):          # Errado pois o método estudar não pode ser sobreescrito pois é final
        print('Estudando e estagiando...')




from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

"""




from typing import Protocol

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')

class venda:
    titulo = 'Oi'

v1 = venda()

estudar(v1)

