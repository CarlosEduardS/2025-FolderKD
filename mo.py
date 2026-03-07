import random
import time
class bac:
    def __init__(self,saldo):
        self.saldo = saldo
    
    def sac(self,valor):
        self.valor = valor
        self.saldo = self.saldo - self.valor
        print(f'o valor {self.valor:.2f} foi retirado do valor {self.saldo-self.valor:.2f} e ficou {self.saldo:.2f}')

    def dep(self,valor):
        self.valor = valor
        self.saldo = self.saldo + self.valor
        print(f'o valor {self.valor:.2f} foi acrecentado ao valor {self.saldo-self.valor:.2f} e ficou {self.saldo:.2f}')

    def apo(self,valor,):
        self.valor = valor
        color = {'zero':'\033[m','red':'\033[31m','yellow':'\033[33m'}
        print(f'Seu saudo {color['yellow']}{self.saldo:.2f}{color['zero']}')
        match valor:
            case _ if 1<=valor<=100:
                print('Jogando\n')
                time.sleep(0.2)
                print(f'Você ganhou\nO valor {color['yellow']}{self.valor*1.9:.2f}{color['zero']} sera acresentado a sua conta')
                time.sleep(0.2)
                self.saldo = self.saldo + self.valor*1.9
                print(f'Seu saldo atual é {color['yellow']}{self.saldo:.2f}{color['zero']}')
            case _:
                print('Jogando\n')
                time.sleep(0.2)
                if 2<= (ran:=random.randint(1,100)) <= 10:
                    print(f'Você ganhou\nO valor {color['yellow']}{self.valor:.2f}{color['zero']} sera acresentado a sua conta')
                    time.sleep(0.2)
                    self.saldo = self.saldo + self.valor*1.5
                    print(f'Seu saldo atual é {color['yellow']}{self.saldo:.2f}{color['zero']}')
                else:
                    self.saldo = self.saldo - self.valor
                    print(f'{color['red']}Voce perdeu{color['zero']}\nO valor {color['yellow']}{self.valor:.2f}{color['zero']} sera descontado de sua conta\nSeu saudo {color['yellow']}{self.saldo:.2f}{color['zero']}')
    pass

#luis = bac(float(input('Qual é seu saldo? ')))
luis = bac(1000)
print('Seu saldo é 1000')
while True:
    match (res:=input('Deseja depositar, sacar ou apostar: ').lower()):
        case 'depositar':
            luis.dep(float(input('quanto deseja depositar? ')))
        case 'sacar':
            luis.sac(float(input('Quanto deseja sacar? ')))
        case 'apostar':
            luis.apo(float(input('Quanto deseja apostar? ')))