import turtle
from random import randint

# =======
# O desenho médio e difícil foram usados com referencia de um site. Deixarei o link
# Link 01 --> https://python-with-science.readthedocs.io/en/latest/koch_fractal/koch_fractal.html
# Link 02 --> https://github.com/eqlz/fractals-by-python-turtle/blob/master/sierpinski/sierpinski.py
# =======
 
# Fácil
# No final estarei chamando a função criada
 
def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# Médio - Floco de neve de Koch

def drawKoch(t, size, nivel, angle=60):
    if nivel == 0:
        t.pencolor(randomColor())
        t.fd(size)
        return

    for turn in [angle, -2 * angle, angle, 0]:
        drawKoch(t, size / 3, nivel - 1, angle)
        t.lt(turn)
        
# Difícil - Triângulo de Sierpinski
# A forma geométrica do triângulo está separada, porém conta na contagem de linhas exigido

def drawTriangle(t, size):
    t.pd()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(3):
        t.fd(size)
        t.lt(120)
    t.end_fill()
    t.pu()
    
def drawSierpinski(t, size, nivel, angle=120):
    if nivel == 0:
        drawTriangle(t, size)
        return
    
    for i in range(3):
        drawSierpinski(t, size / 2, nivel - 1, angle)
        t.fd(size)
        t.lt(angle)
        
t = turtle.Turtle()
turtle.colormode(255)
# t.speed("slowest")
t.speed(0)
t.pu()

# Desenhando o desenho Fácil

"""
t.goto(0, -100)
t.pd()
for i in range(36):
    t.pencolor(randomColor())
    t.circle(100 - i * 2)
    t.rt(10)
"""
    
# Desenhando o desenho Médio

"""
t.goto(-150, 90)
t.pd()
for i in range(3):
    drawKoch(t, 300, 3)
    t.rt(120)
"""
    
# Desenhando o desenho Difícil

"""
t.goto(-200, -150)
drawSierpinski(t, 400, 4)
"""

turtle.done()