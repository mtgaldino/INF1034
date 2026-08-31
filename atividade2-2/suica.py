from turtle import *

t = Turtle()

#Desenhando o fundo vermelho (quadrado)
t.pu()
t.goto(-150, 150)
t.pd()
t.seth(0)
t.color("red")
t.begin_fill()
for cont in range(4):
    t.fd(300)
    t.rt(90)
t.end_fill()

#Desenhando a barra vertical da cruz
t.pu()
t.goto(-30, 100)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(60)
    t.rt(90)
    t.fd(200)
    t.rt(90)
t.end_fill()

#Desenhando a barra horizontal da cruz
t.pu()
t.goto(-100, 30)
t.pd()
t.seth(0)
t.color("white")
t.begin_fill()
for cont in range(2):
    t.fd(200)
    t.rt(90)
    t.fd(60)
    t.rt(90)
t.end_fill()

mainloop()
