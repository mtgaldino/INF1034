from turtle import *

t = Turtle()

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

mainloop()
