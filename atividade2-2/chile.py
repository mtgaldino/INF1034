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
    t.begin_fill()
    for cont in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.pensize(2)
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
    
def desenha_estrela(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(0)
    t.color(cor)
    t.begin_fill()
    for cont in range(5):
        t.fd(tamanho)
        t.rt(144)
    t.end_fill()
    
def desenha_quadrado(x, y, tamanho, cor):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(0)
    t.color(cor)
    t.begin_fill()
    for cont in range(4):
        t.fd(tamanho)
        t.rt(90)
    t.end_fill()
    
#Desenhando a bandeiro do Chile
def desenha_bandeira_chile():
    desenha_retangulo(-255, 150, 450, 150, "white")
    desenha_retangulo(-255, 0, 450, 150, "red")
    desenha_quadrado(-255, 150, 150, "blue")
    desenha_estrela(-165, 95, 25, "white")
    desenha_retangulo_contorno(-255, 150, 450, 300, "black")
    
desenha_bandeira_chile()

"""
#Desenhando a faixa branca (topo)
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("black")
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(150)
    t.rt(90)

#Desenhando a faixa vermelha (base)
t.pu()
t.goto(-225, 0)
t.pd()
t.seth(0)
t.color("#D52B1E")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(150)
    t.rt(90)
t.end_fill()

#Desenhando o quadrado azul (canto)
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("#0033A0")
t.begin_fill()
for cont in range(4):
    t.fd(150)
    t.rt(90)
t.end_fill()

#Desenhando a estrela branca
t.pu()
t.goto(-165, 95)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(5):
    t.fd(25)
    t.rt(144)
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
