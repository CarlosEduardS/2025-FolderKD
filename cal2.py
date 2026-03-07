import keyboard as kb
import sys

matriz = [[1,2,3,'+'], [4,5,6,'-'], [7,8,9,'*'], [' ',0,'/','=']]

WIDTH = 29
HEADER_LEN = WIDTH - 1

def imprimir_matriz(matriz, resultado='Aguardando resultado'):
    print('=' * HEADER_LEN)
    print(f'{resultado:^{WIDTH}}')
    print('=' * HEADER_LEN)
           
    for i in range(4):
        for j in range(4):
            print(f'[{matriz[i][j]:^5}]', end='')
        print()

def atualizar_resultado(novo):
    sys.stdout.write('\x1b[6A')   # sobe até a linha do resultado
    sys.stdout.write('\x1b[2K')   # limpa a linha
    sys.stdout.write(f'{novo:^{WIDTH}}\n')  # escreve novo resultado
    sys.stdout.write('\x1b[5B')   # volta para a posição original
    sys.stdout.flush()

# Inicializa a interface
imprimir_matriz(matriz)

# Armazena a expressão digitada
expressao = ''

# Loop principal
while True:
    ev = kb.read_event()
    if ev.event_type == 'down':
        tecla = ev.name

        # Ignora teclas como shift, ctrl, etc.
        if len(tecla) > 1 and tecla not in ['enter', 'backspace', 'esc']:
            continue

        if tecla == 'enter' or tecla == '=':
            try:
                resultado = str(eval(expressao))
                atualizar_resultado(resultado)
                expressao = ''  # limpa após calcular
            except:
                atualizar_resultado('Erro')
                expressao = ''
        elif tecla == 'backspace':
            expressao = expressao[:-1]
            atualizar_resultado(expressao)
        elif tecla == 'esc':
            break
        else:
            expressao += tecla
            atualizar_resultado(expressao)
