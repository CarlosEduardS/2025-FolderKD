import pygame
import math
import serial
import time

# Inicializa a comunicação serial com Arduino
arduino = serial.Serial('COM3', 9600)  # Altere 'COM3' para sua porta
time.sleep(2)  # Aguarda conexão

# Inicializa o Pygame
pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonar Ultrassônico")

# Cores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
center = (WIDTH // 2, HEIGHT // 2)

def draw_sonar(distance_cm):
    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, center, 150, 1)
    pygame.draw.circle(screen, GREEN, center, 100, 1)
    pygame.draw.circle(screen, GREEN, center, 50, 1)
    pygame.draw.line(screen, GREEN, center, (center[0], 0), 1)

    # Converte distância para pixels (máx 150 cm → 150 px)
    distance_px = min(int(distance_cm), 150)
    angle = math.radians(90)
    x = center[0] + distance_px * math.cos(angle)
    y = center[1] - distance_px * math.sin(angle)
    pygame.draw.circle(screen, GREEN, (int(x), int(y)), 5)

    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if arduino.in_waiting:
        try:
            line = arduino.readline().decode().strip()
            distance = float(line)
            draw_sonar(distance)
        except:
            pass

    pygame.time.delay(100)

pygame.quit()
arduino.close()
