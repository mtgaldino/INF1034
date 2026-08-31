from turtle import *

t = Turtle()

#Desenhando a faixa branca (topo)
t.pu()
t.goto(-225, 150)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(450)
    t.rt(90)
    t.fd(150)
    t.rt(90)
t.end_fill()

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

mainloop()
