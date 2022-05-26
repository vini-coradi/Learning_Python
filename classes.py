"""
POO - Classes

Em POO, Classes são modelos dos objetos do mundo real sendo representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle de lâmpadas da sua casa

Classes podem conter:
    -Atributos -> Representam as caracteristicas do objeto. Pelos atributos conseguimos
    representar computacionalmente os estados do objeto. No caso da lampada, iriamos
    querer saber se ela é 110 ou 220, se é branca ou amarela e qual a luminosidade dela, etc.

    -Métodos (funções) -> Representam os comportamentos desse objeto. As ações que este objeto
    pode realizar no seu sistema. No caso da lâmpada, o comportamwento que iriamos querer representar
    no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

Obs: Utilizamos a palavra pass em python quando temos um bloco de código que ainda não está
implementado.

Obs: Quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial
em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiúsculo, todas juntas.


OBs: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema,
chamamos esses objetos que serão mapeados de entidades.

"""

class Lampada:
    pass

lamp = Lampada()

print(type(lamp))
