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

def desenha_triangulo(x, y, tamanho, cor, direc):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(direc)
    t.pensize(3)
    t.color(cor)
    for cont in range(3):
        t.fd(tamanho)
        t.rt(120)
    t.pensize(1)
    
#Desenhando a bandeira de Israel
def desenha_bandeira_israel():
    desenha_retangulo(-255, 150, 450, 300, "white")
    #Faixa azul superior
    desenha_retangulo(-255, 130, 450, 30, "#0038B8")
    #Faixa azul inferior
    desenha_retangulo(-255, -100, 450, 30, "#0038B8")
    #Tringulo normal
    desenha_triangulo(-80, 20, 100, "#0038B8", 0)
    #Triangulo invertido
    desenha_triangulo(-80, -45, 100, "#0038B8", 60)
    desenha_retangulo_contorno(-255, 150, 450, 300, "black")
    
desenha_bandeira_israel()

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

#Desenhando a faixa azul superior
t.pu()
t.goto(-225, 130)
t.pd()
t.seth(0)
t.color("#0038B8")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(30)
    t.rt(90)
t.end_fill()

#Desenhando a faixa azul inferior
t.pu()
t.goto(-225, -100)
t.pd()
t.seth(0)
t.color("#0038B8")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(30)
    t.rt(90)
t.end_fill()

#Desenhando o primeiro triangulo da Estrela de Davi
t.pu()
t.goto(-50, 45)
t.pd()
t.seth(0)
t.pensize(3)
t.color("#0038B8")
for cont in range(3):
    t.fd(100)
    t.rt(120)
t.pensize(1)

#Desenhando o segundo triangulo (invertido) da Estrela de Davi
t.pu()
t.goto(-50, -45)
t.pd()
t.seth(60)
t.pensize(3)
t.color("#0038B8")
for cont in range(3):
    t.fd(100)
    t.rt(120)
t.pensize(1)

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
