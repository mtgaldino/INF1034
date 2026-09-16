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
t.goto(-20, eleva_ao_quadrado(-20))
t.pd()

for x in range(-99, 101):
    t.goto(x, eleva_ao_quadrado(x))













mainloop()