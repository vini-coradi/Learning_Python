"""
POO -> Métodos Mágicos

São todos os métodos que utilizam dunder.

Dunder -> Double Underscore



# dunder init -> __init__
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas



# dunder repr -> Representação do objeto
 def __repr__(self):
        return f'{self.titulo} escrito por {self.autor} com {self.paginas} paginas'

# dunder str -> Representação do objeto por string, tem prioridade com relação ao repr


"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def __str__(self):
       return  self.autor
       #return f'{self.titulo} escrito por {self.autor} com {self.paginas} paginas'

    def __len__(self):
        return self.paginas

    def __del__(self):
        if False:
            print('O objeto do tipo livro foi deletado na memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ' '
            for n in range(outro):
                msg += ' ' + self.titulo
            return msg
        return 'Não podemos multiplicar'



livro1 = Livro('Python curse', 'Udemy', 300)
livro2 = Livro('Math curse', 'fei', 500)

print(str(livro1))

print(livro1 + livro2)

print(livro1 * 3)

