
def cabecalho(texto: str, alinhamento: bool=True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')

print(cabecalho('vini'))

print(cabecalho('vini', alinhamento=False))

# Mypy só faz sentido ao utilizar o type hinting... e ele faz o teste quando o programa é executado no
# terminal:

# ex: mypy usando_mypy.py
