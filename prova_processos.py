import time
class veiculo:
    def __init__(self,modelo,marca,ano,velocidade=0):
        self.mol = modelo
        self.mar = marca
        self.ano = ano
        self.vel = velocidade
    def mostra(self):
        print(f' O modelo {self.mol}, da marca {self.mar}, do ano {self.ano}')
    pass
class moto(veiculo):
    def __init__(self,cilindrada,velocidade=1,aceleraçao=1):
        self.ace = aceleraçao
        self.vel = velocidade
        self.cili = cilindrada
    def aceleraçao(self):
        while self.vel:
            print(f'Você está a uma velocidade de: {self.vel}km/h')
            self.ace += 0.84
            self.vel *= self.ace
            res = input('Deseja continuar acelerando s/n: ').lower()
            if res == 's':
                continue
            if res == 'n':
                if (res:=input('Deseja freiar s/n: ')).lower() == 's':
                    print('freiando')
                    while self.vel == 0:
                        self.vel *= 0.6
                        print(f'Sua velocidade é {self.vel:.0f}km/h')
                    print('Moto está parada')
                else:
                    while self.vel == 0:
                        self.vel *= 0.9
            else:
                continue
    pass
class carro(veiculo):
    def __init__(self,portas,velocidade=1,aceleraçao=1):
        self.ace = aceleraçao
        self.vel = velocidade
        self.pot = portas
    def aceleraçao(self):
            while self.vel:
                print(f'\rVocê está a uma velocidade de: {self.vel:.0f}km/h', end='')
                self.ace += 0.62
                self.vel *= self.ace
                #res = input('Deseja continuar acelerando s/n: ').lower()
                '''if res == 's':
                    continue
                if res == 'n':
                    if (res:=input('Deseja freiar s/n: ')).lower() == 's':
                        print('freiando')
                        while self.vel <= 0:
                            self.vel *= 0.48
                            print(f'Sua velocidade é {self.vel:.0f}km/h')
                        print('Carro está parada')
                    else:
                        while self.vel <= 0:
                            self.vel *= 0.84
                else:
                    continue'''
                time.sleep(0.2)
    pass

while True:
    res=input('Deseja moto ou carro? ').lower()
    if res == 'moto':
        vel = veiculo(input('Qual é a marca: '),input('Qual é o modelo: '),int(input('Qual é o ano: ')))
        vel.mostra()
        vel = moto(int(input('Quantos cilindros essa moto tem: ')))
        vel.aceleraçao()
    elif res == 'carro':
        vel = veiculo(input('Qual é a marca: '),input('Qual é o modelo: '),int(input('Qual é o ano: ')))
        vel.mostra()
        vel = carro(int(input('Quantas portas? ')))
        vel.aceleraçao()
    else:
        continue