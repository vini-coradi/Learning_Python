"""
Dunder Name e Dunder Main

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunder para criar funções, atributos, propriedades e etc, utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main() {

    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main (String[] args){

}

# Em Python, se executarmos um módulo Python diretamente da linha de comando, internamente
o Python atribuirá à variável __name__ e valor __main__ indicando que este módulo é o
módulo de execução principal

Se o programa for importado, ele tera o __name__ como o proprio nome do arquivo (sem a extensão)

"""

from funcoes_com_parametro import  soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))