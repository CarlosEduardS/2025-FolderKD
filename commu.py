import serial
import time
import keyboard  # nova biblioteca para capturar teclas

# Configurar conexão serial
porta_serial = 'COM6'
baud_rate = 9600

try:
    arduino = serial.Serial(porta_serial, baud_rate, timeout=1)
    time.sleep(2)  # esperar estabilizar a conexão serial

    print("Pressione W, A, S ou D para controlar. Pressione ESC para sair.")

    while True:
        if keyboard.is_pressed('w'):
            arduino.write(b'W')
        elif keyboard.is_pressed('a'):
            arduino.write(b'A')
        elif keyboard.is_pressed('s'):
            arduino.write(b'S')
        elif keyboard.is_pressed('d'):
            arduino.write(b'D')
        else:
            arduino.write(b'X')

        if keyboard.is_pressed('esc'):
            print("Encerrando...")
            break

        time.sleep(0.1)

    arduino.close()

except serial.SerialException as e:
    print(f"Erro na comunicação serial: {e}")
