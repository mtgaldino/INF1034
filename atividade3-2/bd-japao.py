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
    
    
#Desenhando a bandeira do Japão
desenha_bandeira_japao()
mainloop()
