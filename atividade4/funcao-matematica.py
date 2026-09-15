from turtle import *
import random
from time import sleep

t = Turtle()

# === Funções ===

"""
Cada função criada retornará o valor do y da função t.goto(x, y)
""" 

def desenhar_plano_cartesiano():
    t.pu()
    t.goto(-400, 0)
    t.pd()
    t.goto(400, 0)
    t.stamp()

    t.pu()
    t.goto(0, -400)
    t.pd()
    t.goto(0, 400)
    t.lt(90)
    t.stamp()
    t.rt(90)

def limpar_tela():
    sleep(3)
    t.clear()
    t.color("black")
    desenhar_plano_cartesiano()

def soma_10(x):
    return x + 10   

def eleva_ao_quadrado(x):
    return x ** 2

def raiz_quadrada(x):
    return x ** 0.5

def x_sobre_1(x):
    return 1 / x

def potencia_de_2(x):
    return 2 ** x

def cinco_menos_x_quadrado(x):
    return 5 - x ** 2

def fn_quadratica(x):
    return x ** 2 - 5 * x + 6

def fn_cubica(x):
    return x ** 3 - x ** 2 - x + 1

# === programa ===
desenhar_plano_cartesiano()

t.color("blue")
t.pu()
t.goto(-200, soma_10(-200))
t.pd()

for x in range(-99, 101):
    t.goto(2 * x, soma_10(2 * x))

limpar_tela()

t.color("red")
t.pu()
t.goto(10 * -20, eleva_ao_quadrado(-20))
t.pd()

for x in range(-20, 21):
    t.goto(10 * x, eleva_ao_quadrado(x))

limpar_tela()

# A.

# - y = √x
t.color("green")
t.pu()
t.goto(0, 40 * raiz_quadrada(0))
t.pd()

for x in range(0, 41):
    t.goto(10 * x, 40 * raiz_quadrada(x))

limpar_tela()

# B.

# - y = 1/x
t.color("purple")

# x sendo negativo
t.pu()
t.goto(10 * -40, 200 * x_sobre_1(-40))
t.pd()
for x in range(-40, 0):
    t.goto(10 * x, 200 * x_sobre_1(x))

# x sendo positivo
t.pu()
t.goto(10 * 1, 200 * x_sobre_1(1))
t.pd()
for x in range(1, 41):
    t.goto(10 * x, 200 * x_sobre_1(x))

limpar_tela()

# C.

# - y = 2^x
t.color("orange")
t.pu()
t.goto(40 * -10, potencia_de_2(-10))
t.pd()

for x in range(-10, 9):
    t.goto(40 * x, potencia_de_2(x))

limpar_tela()

# D.
 
# - y = 5 - x^2
t.color("brown")
t.pu()
t.goto(10 * -20, cinco_menos_x_quadrado(-20))
t.pd()

for x in range(-20, 21):
    t.goto(10 * x, cinco_menos_x_quadrado(x))

limpar_tela()

# E.

# - y = x^2 - 5x + 6
t.color("navy")
t.pu()
t.goto(10 * -15, fn_quadratica(-15))
t.pd()

for x in range(-15, 21):
    t.goto(10 * x, fn_quadratica(x))

limpar_tela()

# F.

# - y = x^3 - x^2 - x + 1
t.color("magenta")
t.pu()
t.goto(40 * -7, fn_cubica(-7))
t.pd()

for x in range(-7, 8):
    t.goto(40 * x, fn_cubica(x))

limpar_tela()

mainloop()