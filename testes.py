import unittest

from atividades import comer, dormir, engracada

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno de comida saudavel"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo por que quero manter a forma'
        )
    def teste_comer_gostosa(self):
        """ Testando o retorno dormindo muito"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza por que só se vive uma vez'
        )


    def test_engracada(self):
        # self.assertEqual(engracada('Sergio Malandro'), False)
         self.assertFalse(engracada('Sergio Malandro'))
         self.assertTrue(engracada('Adam Sandler'), 'Adam Sandler é bom demais')


if __name__ == 'main':
    unittest.main()