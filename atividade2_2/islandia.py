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
    
#Desenhando a bandeira da Islandia
def desenha_bandeira_islandia():
    #fundo azul
    desenha_retangulo(-225, 150, 450, 300, "#02529C")
    #Faixa vertical branca
    desenha_retangulo(-65, 150, 70, 300, "white")
    #Faixa horizontal branca
    desenha_retangulo(-225, 40, 450, 80, "white")
    #Faixa vertical vermelha
    desenha_retangulo(-45, 150, 30, 300, "#DC1E35")
    #Faixa horizontal vermelha
    desenha_retangulo(-225, 15, 450, 30, "#DC1E35")
    
desenha_bandeira_islandia()

"""
#Desenhando o fundo azul
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("#02529C")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a barra vertical branca
t.pu()
t.goto(-65, 150)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(70)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a barra horizontal branca
t.pu()
t.goto(-225, 40)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(80)
    t.rt(90)
t.end_fill()

#Desenhando a barra vertical vermelha (mais fina, por cima)
t.pu()
t.goto(-45, 150)
t.pd()
t.seth(0)
t.color("#DC1E35")
t.begin_fill()
for cont in range(2):
    t.fd(30)
    t.rt(90)
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a barra horizontal vermelha (mais fina, por cima)
t.pu()
t.goto(-225, 15)
t.pd()
t.seth(0)
t.color("#DC1E35")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(30)
    t.rt(90)
t.end_fill()
"""
mainloop()
