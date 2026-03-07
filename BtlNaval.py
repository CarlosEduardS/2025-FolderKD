import random, time

li = int(input('Digite o limite de linhas: '))
co = int(input('Digite o limite de colunas: '))

matriz = [[0 for _ in range(co)] for _ in range(li)]
SMatriz = [[0 for _ in range(co)] for _ in range(li)]

def GerarMapa():
    for i in range(li):
        for j in range(co):
            if random.randint(1, 3) == 1:
                SMatriz[i][j] = 1
                
def mostrarMatriz():
    print('-=' * 15)
    for i in range(li):
        for j in range(co):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()
        
def Jogada(linha, coluna,):
    if SMatriz[linha][coluna] == 1:
        matriz[linha][coluna] = 'X'
    else:
        matriz[linha][coluna] = '-'
        
GerarMapa()
time.sleep(0.5)
mostrarMatriz()
while True:
    Jogada((int(input(f'Digite a linha (1-{li}): ')) - 1), (int(input(f'Digite a coluna (1-{co}): ')) - 1))
    time.sleep(0.2)
    mostrarMatriz()