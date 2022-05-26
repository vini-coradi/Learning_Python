class Robo:

    def __init__(self, nome, bateria = 100, habilidades = []):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP BOOP BEEP BOOP. EU SOU {self.__nome.upper()}'
        return 'Bateria fraca!! Por favor, recarregue e tente novamente'
    def aprender_habilidade(self, nova_habilidade, custo):
        for skill in self.__habilidades:
            if nova_habilidade in self.__habilidades:
                'Robo já conhece a habilidade, não vai aprender de novo!'
            else:
                if self.__bateria >= custo:
                    self.__bateria -= custo
                    self.__habilidades.append(nova_habilidade)
                    return f'HABILIDADE APRENDIDA!! AGORA SEI {nova_habilidade.upperI()}'
                return 'Bateria fraca!! Por favor, recarregue e tente novamente'

