from pygame import *

"""
Exemplos de tamanhos de tela

Tamanho 4:3 -> 800 x 600
Tamanho 16:9 -> 1200 x 720
"""

init()
screen = display.set_mode((1280, 720))

runnig = True
while runnig == True:
    for ev in event.get():
        if ev.type == QUIT:
            runnig = False

    screen.fill("#97D1FA")
    draw.rect(screen, "#0D1664", (100, 200, 200, 50))
    draw.circle(screen, "#FFF251", (80, 80), 50)
    draw.polygon(screen, "#F2883B", [(400, 300), (450, 300), (425, 250)])
    draw.line(screen, "#FFF251", (10, 150), (100, 20), 4)
    display.update()