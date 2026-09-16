from turtle import *

t = Turtle()

#Criando as funções
def desenha_circulo(x, y, cor, tamanho):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.color(cor)
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()

def desenha_retangulo(x, y, larg, alt, cor):
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

def desenha_bandeira_japao():
    desenha_retangulo(-225, 150, 450, 300, "black")
    desenha_circulo(0, -80, "red", 80)
"""
#Desenhando o fundo branco
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()
"""
"""
#Desenhando o circulo vermelho
t.pu()
t.goto(0, -80)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
t.circle(80)
t.end_fill()
"""
"""
#Desenhando o contorno preto ao redor de toda a bandeira
t.pu()
t.goto(-225, 150)
t.seth(0)
t.pd()
t.pensize(1)
t.color("black")
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.pensize(1)
"""

#Desenhando a bandeira do Japão
desenha_bandeira_japao()
mainloop()
