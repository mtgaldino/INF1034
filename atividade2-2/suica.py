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
    
def desenha_cruz(x, y, larg, alt, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(0)
    t.color(cor)
    t.begin_fill()
    for cont in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()
    
    
#Desenhando a bandeira da Suiça
def desenha_bandeira_suica():
    desenha_retangulo(-255, 150, 450, 300, "red")
    desenha_cruz(-60, 100, 60, 200, "white")
    desenha_cruz(-130, 30, 200, 60, "white")
    
desenha_bandeira_suica()

"""

#Desenhando o fundo vermelho (quadrado)
t.pu()
t.goto(-150, 150)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
for cont in range(4):
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a barra vertical da cruz
t.pu()
t.goto(-30, 100)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(60)
    t.rt(90)
    t.fd(200)
    t.rt(90)
t.end_fill()

#Desenhando a barra horizontal da cruz
t.pu()
t.goto(-100, 30)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(200)
    t.rt(90)
    t.fd(60)
    t.rt(90)
t.end_fill()

"""

mainloop()
