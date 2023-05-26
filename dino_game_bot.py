from time import sleep

import pyautogui
from PIL import ImageGrab

X = 315

Y_obj_baixo_1 = 655
Y_obj_baixo_2 = 676

Y_obj_alto_1 = 550
Y_obj_alto_2 = 570

def obterCapturaDeTela():
    screen = ImageGrab.grab()
    return screen

def verificarInimigoBaixo(screen):
    corDeFundo = screen.getpixel((int(X), Y_obj_baixo_1))
    for x in range(int(X), int(X+15)):
        for y in range(Y_obj_baixo_1, Y_obj_baixo_2):
            corDetectada = screen.getpixel((x, y))
            if corDetectada != corDeFundo:
                return True
            else:
                corDeFundo = corDetectada

def verificarInimigoAlto(screen):
    corDeFundo = screen.getpixel((int(X), Y_obj_alto_1))
    for x in range(int(X), int(X+15)):
        for y in range(Y_obj_alto_1, Y_obj_alto_2):
            corDetectada = screen.getpixel((x, y))
            if corDetectada != corDeFundo:
                return True
            else:
                corDeFundo = corDetectada

def pular():
    global X
    pyautogui.press("up")
    X += 0.4
    
def abaixar():
    global X
    pyautogui.keyDown('down')
    sleep(0.3)
    pyautogui.keyUp('down')
    X += 0.4

print("Começando em 3 segundos")
sleep(3)

while True:
    screen = obterCapturaDeTela()

    if verificarInimigoBaixo(screen):
        pular()

    if verificarInimigoAlto(screen):
        abaixar()


