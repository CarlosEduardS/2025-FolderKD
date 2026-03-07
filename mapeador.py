import pygame
import serial
import time

# Conecta à porta serial
arduino = serial.Serial('COM6', 115200)

# Inicializa Pygame
pygame.init()
WIDTH, HEIGHT = 1200, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapeamento estilo robô aspirador")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Estado do robô
x, y = CENTER
direcao = 'N'
pontos = []

def cm_to_pixels(cm):
    return cm * 4

def atualizar_posicao(movimento):
    global x, y, direcao
    passo = 20
    if movimento == 'F':
        if direcao == 'N': y -= passo
        elif direcao == 'S': y += passo
        elif direcao == 'L': x += passo
        elif direcao == 'O': x -= passo
    elif movimento == 'T':
        if direcao == 'N': y += passo
        elif direcao == 'S': y -= passo
        elif direcao == 'L': x -= passo
        elif direcao == 'O': x += passo
    elif movimento == 'D':
        direcao = {'N': 'L', 'L': 'S', 'S': 'O', 'O': 'N'}[direcao]
    elif movimento == 'E':
        direcao = {'N': 'O', 'O': 'S', 'S': 'L', 'L': 'N'}[direcao]

def registrar_obstaculo(distancia):
    escala = 4
    dx, dy = 0, 0
    if direcao == 'N': dy = -distancia * escala
    elif direcao == 'S': dy = distancia * escala
    elif direcao == 'L': dx = distancia * escala
    elif direcao == 'O': dx = -distancia * escala
    ponto_x = x + dx
    ponto_y = y + dy
    pontos.append((ponto_x, ponto_y))

def desenhar_mapa():
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT), 1)
    pygame.draw.circle(screen, GREEN, (int(x), int(y)), 5)
    for px, py in pontos:
        pygame.draw.circle(screen, RED, (int(px), int(py)), 3)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if arduino.in_waiting:
        try:
            linha = arduino.readline().decode().strip()
            partes = linha.split(',')
            if len(partes) == 2:
                direcao = partes[0]
                distancia = float(partes[1])
                if 1 <= distancia <= 50:
                    registrar_obstaculo(distancia)
                    atualizar_posicao('F')
        except:
            pass

    desenhar_mapa()
    pygame.display.flip()
    time.sleep(0.2)

pygame.quit()
