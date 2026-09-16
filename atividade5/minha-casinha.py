from pygame import *

"""
Exemplos de tamanhos de tela

Tamanho 4:3 -> 800 x 600
Tamanho 16:9 -> 1200 x 720
"""

init()
screen = display.set_mode({800, 600})

runnig = True
while runnig == True:
    for ev in event.get():
        if ev.type == QUIT:
            runnig = False
    display.update()