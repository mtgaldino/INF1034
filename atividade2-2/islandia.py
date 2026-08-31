from turtle import *

t = Turtle()

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

mainloop()
