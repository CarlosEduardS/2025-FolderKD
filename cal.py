matriz = [[1, 2, 3, '+'], [5, 6, 7, 8], [9, '', '', ''], ['*', '+', '-', '/']]

def tela():
    for i in range(5):
        for j in range(4):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

def resultado_operacao(resultado):
    print('-' * 20)
    print(f'{resultado:^20}')
    print('-' * 20)
    
def valores(num1, num2):
    match res:=input('Escolha uma operação (+, -, *, /): '):
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '*':
            res = num1 * num2
        case '/':
            if num2 == 0:
                print('Erro: Divisão por zero!')
            else:
                res = num1 / num2
    resultado_operacao(res)
    
tela()
valores(int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')))