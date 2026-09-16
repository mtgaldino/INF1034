from turtle import *

t = Turtle()

#Criando as funções
def desenha_retangulo(x, y, larg, alt, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for cont in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()
    
def desenha_retangulo_contorno(x, y, larg, alt, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.pensize(2)
    t.color(cor)
    for cont in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.pensize(2)
    
#Desenhando a bandeira da Polonia
def desenha_bandeira_polonia():
    desenha_retangulo(-255, 0, 450, 150, "red")
    desenha_retangulo_contorno(-255, 150, 450, 300, "black")

desenha_bandeira_polonia()

"""
#Desenhando a faixa branca (topo)
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(150)
    t.rt(90)
t.end_fill()

#Desenhando a faixa vermelha (base)
t.pu()
t.goto(-225, 0)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(150)
    t.rt(90)
t.end_fill()

#Desenhando o contorno preto ao redor de toda a bandeira
t.pu()
t.goto(-225, 150)
t.seth(0)
t.pd()
t.pensize(2)
t.color("black")
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.pensize(1)
"""

mainloop()
