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
    
def desenha_circulo(x, y, cor, tamanho):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.color(cor)
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()
    
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
    
#Desenhando a bandeira da Turquia
def desenha_bandeira_turquia():
    desenha_retangulo(-255, 150, 450, 300, "red")
    desenha_circulo(-90, -70, "white", 70)
    desenha_circulo(-60, -55, "red", 55)
    desenha_estrela(-20, 10, 55, "white")
    
desenha_bandeira_turquia()
    
"""

#Desenhando o fundo vermelho
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando o circulo branco (parte externa do crescente)
t.pu()
t.goto(-40, -70)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
t.circle(70)
t.end_fill()

#Desenhando o circulo vermelho por cima (cria o efeito de crescente)
t.pu()
t.goto(-10, -55)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
t.circle(55)
t.end_fill()

#Desenhando a estrela branca
t.pu()
t.goto(90, -25)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(5):
    t.fd(25)
    t.rt(144)
t.end_fill()

"""

mainloop()
