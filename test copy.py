class fabrica:
    def __init__(self,chasi,portas,rodas,estrutura,motor,tanque,cambio):
        self.ch = chasi
        self.pot = portas
        self.rod = rodas
        self.struc = estrutura
        self.mot = motor
        self.tan = tanque
        self.cam = cambio

    def carro(self,velocidade_max,rpm,marchas,velocidade=0):
        self.velmax = velocidade_max
        self.rpm = rpm
        self.vel = velocidade
        self.mac = marchas

        print(f'Seu carro de {self.pot} portas, {self.rod} rodas, motor de {self.mot}, tanque de {self.tan}L')
        match self.mac:
            case 1:
                while self.rpm < 2300:
                    self.velmax *= self.velmax // self.velmax
                    self.vel += self.velmax
                print('RPm Maximo, necessario a troca de macha')
                self.mac = int(input('Deseja subir para a segunda macha? s/n: '))
            case 2:
                while self.rpm < 3500:
                    self.velmax *= self.velmax // self.velmax
                    self.vel += self.velmax ** 2
                print('RPm Maximo, necessario a troca de macha')
                self.mac = int(input('Deseja subir para a terceira macha? s/n: '))
            case 3:
                while self.rpm < 4700:
                    self.velmax *= self.velmax // self.velmax
                    self.vel += self.velmax ** 3
                print('RPm Maximo, necessario a troca de macha')
                self.mac = int(input('Deseja subir para a terceira macha? s/n: '))
            case 4:
                while self.rpm < 4700:
                    self.velmax *= self.velmax // self.velmax
                    self.vel += self.velmax ** 4
                print('RPm Maximo, necessario a troca de macha')
                self.mac = int(input('Deseja subir para a terceira macha? s/n: '))
            case 5:
                while self.rpm < 4700:
                    self.velmax *= self.velmax // self.velmax
                    self.vel += self.velmax ** 5
                print('RPm Maximo, necessario a troca de macha')
                self.mac = int(input('Deseja subir para a terceira macha? s/n: '))
    pass
def inputs():
    fab = fabrica(input('Possui chasi'))