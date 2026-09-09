from turtle import *

t = Turtle()

#Criando as funções
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

def desenha_bandeira_italia():
    desenha_retangulo(-225, 150, 150, 300, "green")
    desenha_retangulo()
    desenha_retangulo()

#Desenhando a faixa verde
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("green")
t.begin_fill()
for cont in range(2):
    t.fd(150)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a faixa branca
t.pu()
t.goto(-75, 150)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(150)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a faixa vermelha
t.pu()
t.goto(75, 150)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
for cont in range(2):
    t.fd(150)
    t.rt(90)
    t.fd(300)
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

#Desenhando a Bandeira da Itália


mainloop()
