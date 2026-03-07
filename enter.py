import pyautogui as gui
import keyboard as kb
import os

console = False

def command():
    while True:
        gui.sleep(2)
        gui.hotkey('ctrol','tab')
        gui.write('test')
        gui.hotkey('ctrol','tab')
        gui.write('10')
        gui.hotkey('ctrol','tab')
        gui.write('1000')
        gui.hotkey('ctrol','tab')
        gui.write('100')
        gui.hotkey('ctrol','tab')
        gui.hotkey('space')
        gui.hotkey('ctrol','tab')
        gui.hotkey('ctrol','tab')

while True:
    if kb.is_pressed('f'):
        console = not console
        gui.sleep(0.2)

    if console:
        command()

