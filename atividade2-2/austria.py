from turtle import *

t = Turtle()

#Bandeira feita por função

def desenhar_retangulo(x, y, largura, altura, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.color(cor)
    t.begin_fill()
    for cont in range(2):
        t.fd(largura)
        t.rt(90)
        t.fd(altura)
        t.rt(90)
    t.end_fill()
    
def desenhar_contorno(x, y, largura, altura, cor):
    t.pu()
    t.goto(x, y)
    t.seth(0)
    t.pd()
    t.pensize(2)
    t.color(cor)
    for cont in range(2):
        t.fd(largura)
        t.rt(90)
        t.fd(altura)
        t.rt(90)
    t.pensize(1)

#Faixa vermelha (topo)
desenhar_retangulo(-225, 150, 450, 100, "#ED2939")
#Faixa branca (meio)
desenhar_retangulo(-225, 50, 450, 100, "white")
#Faixa vermelha (base)
desenhar_retangulo(-225, -50, 450, 100, "#ED2939")
#Contorno preto ao redor de toda a bandeira
desenhar_contorno(-225, 150, 450, 300, "black")

mainloop()
