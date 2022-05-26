import unittest

from robo import Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega man', bateria=50)
        print('Setup sendo executado')

    def test_carregar(self):

        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)


    def test_dizer_nome(self):

        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'a bateria deveria estar com 49%')

    def tearDown(self):
        print('tearDown sendo executado')

if __name__ == '__main__':
    unittest.main()