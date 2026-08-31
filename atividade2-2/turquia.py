from turtle import *

t = Turtle()

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

mainloop()
