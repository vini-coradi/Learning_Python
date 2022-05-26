"""def cumprimentar(nome: str) -> str:
    return 'Olá!'

print(cumprimentar('Teste'))"""

def cabecalho(texto: str, alinhamento: bool=True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('vini'))

print(cabecalho('vini', alinhamento=False))